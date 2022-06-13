---
title: "Synthesizing Sinusoids"
date: 2022-05-17T13:17:04+02:00
draft: false
toc: true
math: true
tags:
  - signal-processing
  - delta-sigma-modulation
  - digital-circuits
  - python
---

Here I will go over a hardware efficient digital-technique for synthesizing a
high-fidelity sinusoidal tone for self-test and electrical characterization
purposes. This will be a application of several state-of-the-art hardware
techniques to minimize hardware complexity while readily
generating a precise tone with well over 100 dB of dynamic range. Further more
the resulting output bit-stream is delta-sigma modulated enabling the use of a
low-complexity 4 bit digital-to-analogue-converter that employs
dynamic-element-matching.

## Synthesizer

``` goat
    +-----------------------+  16b  +--------------+  16b  +-------------+  4b                         
    |   32 bit Recursive    |    /  |     1:16     |    /  |  3rd Order  |    /                        
    |    Discrete-Time      +---+-->| Rotated CIC  +---+-->| Delta-Sigma +---+--> Output Bitstream     
    | Sinusoidal Oscillator |  /    | Interpolator |  /    |  Modulator  |  /                          
    +-----------------------+       +--------------+       +-------------+                             
```

The overall system composition is illustrated above and consists of three
modules. The first module is a recursive digital oscillator and operates at a
higher precision but lower clock rate to generate the target test-tone. The
proceeding modules encode this high-resolution digital signal into a low
resolution digital bit-stream there the quantization noise is shaped towards
the high-frequency band that can then be filtered out in the analogue-domain.

## Digital Oscillation

There are numerous all-digital methods for synthesizing a sinusoidal signal
precisely. The most challenging aspect here is the trigonometric functions that
are difficult compute given limited hardware resource. A common approach to
avoid this is to use a look-up table representing `cos(x)` for mapping phase to
amplitude but this generally requires a significant amount of memory.
Alternatively a recursive feedback mechanism can be used that will oscillate
with a known frequency and amplitude given a set of parameters. The later
approach has negligible memory requirements but instead requires full-precision
multiplication. However considering that we are required to perform delta-sigma
encoding at the output this feedback mechanism can run at a reduced clock-rate
allowing this multiplication to be performed in a pipelined fashion which is
considerably more affordable.

``` goat
                  - .-.               .-.                                    
                .->| Σ +------*----->| Σ +---> Digital Sinusoid              
               |    '-'       |       '-'                                    
               |     ^        v        ^                                     
               |     |     .-----.     |                                     
               |     |     | z⁻¹ |      '----- Offset                        
               |     |   . '--+--'                                           
               |     |  /|    |                                              
               |      '+ |<---*                                              
               |      K \|    |                                              
               |         '    v                                              
               |           .-----.                                           
                '----------+ z⁻¹ |                                           
                           '-----'                                           
```

The biquad feedback configuration shown above is one of several oscillating
structures presented in [^1] with the equivalent a python model presented below.
The idea here is to perform full-precision synthesis at 64 or 32 bit with a
pipelined multiplier such that this loop runs at 1/M times the modulator clock
speed where M is the oversampling ratio that is chosen to optimize the
multiplier pipeline. In this case M=16 and we will be using 32 bit frequency
precision.

``` python3
class Resonator:
    def __init__(self, frequency: float = 0.1, amplitude: float = 0.5):
        K = 2 * np.cos(2 * np.pi * frequency)
        self.A = 0.0
        self.B = amplitude * np.sqrt(2.0 - K)
        self.K = K
    def update(self) -> int:
        self.A, self.B = (self.A * self.K - self.B, self.A)
        return self.A
```

The coefficient K determines the frequency of oscillation as a ratio relative to
the operating clock speed. Using \\( K = 2 cos( 2 \pi freq )\\) such that the
oscillation occurs as \\( freq \cdot fclk \\). The initial condition of the two
registers will determine the oscillation amplitude. Setting the first register
to zero and the second to \\( A \sqrt{2 - K} \\) will yield amplitude of \\(A\\)
around zero. We can then offset this signal to specify the level around which
tone oscillates.

## Band-Select Interpolation

The main drawback of not synthesizing the sinusoid at a fractional clock rate
is that we must take care of the aliased components when we increase the
data-rate. Fortunately there are a family of filters that are extremely
efficient at up-sampling a signal while rejecting the aliasing components known
as cascaded integrator-comb filters (CIC)[^2]. These filters consist of several
simple accumulators and differentiators that can be configured to reject
aliasing components.

$$ H(z) = \left( \frac{ 1 - z^{-M} }{ 1 - z^{-1} } \right)^N $$

The transfer function of such a filter is formulated above. This shows that a
CIC structures of order \\( N \\) operating at a oversampling ratio
\\( M \\) will distribute M zeros uniformly around the unit circle. This
completely removes any DC components that end up at the aliasing tones at
multiples of \\( fclk / M\\). However we know priori that we will introduce
aliasing components at integer multiples of the input tone when up-sampling:
\\( freq \cdot fclk / M \\). Making a slight modification to this structure
as discussed in [^3] allows us to further optimize a second-order CIC filter to
specifically reject these components instead.

$$ H(z) = \frac{ 1 - K \cdot z^{-M} + z^{-2M} }{ 1 - K_M z^{-1} + z^{-2} } $$

Notice that the coefficient K from the resonator structure is reused here and
we introduce a new scaling coefficient \\(K_M = 2 \cdot 2 * cos(2 \pi * freq / M )\\)
which we will approximate by tailor expansion to avoid the multiplication
requirement as this factor does not require high precision. Again a python
implementation is shown below for reference.

``` python3
class Interpolator:
    def __init__(self, frequency: float = 0.1, osr: int = 32):
        K = 2 * np.cos(2 * np.pi * frequency)
        KM = 2 * np.cos(2 * np.pi * frequency / osr )
        self.fir_coef = np.array([1, -K, 1]) # FIR coefficients
        self.irr_coef = np.array([-KM, 1]) # IRR coefficients
        self.comb_integrator = np.zeros((2,), dtype=float)
        self.comb_decimator = np.zeros((3,), dtype=float)
        self.osr = osr
        self.count = 0

    def update(self, new_val: float) -> float:
        self.comb_integrator = np.append(
            np.dot(self.fir_coef, self.comb_decimator)
            + np.dot(-self.irr_coef, self.comb_integrator),
            self.comb_integrator[:-1],
        )
        if self.count == 0:
            self.comb_decimator = np.append(new_val, self.comb_decimator[1:])
        self.count = (self.count + 1) % self.osr
        return self.comb_integrator[0]
```

Combing the two feedback mechanisms we can construct a second-order CIC based
digital resonator with a interpolated output that fully rejects aliasing
components. This configuration is shown below. Now let us use Taylor
approximation to resolve the coefficient KM such that it is reduced to
two-component addition. The first two non-zero coefficients for cos are
\\( cos(x) = 1 - x^2 / 2 \\). Hence we can approximate as follows
\\( KM = 2 - 1 >> \lfloor 2 \log_2( 2 \pi * freq / M ) \rfloor \\) where
\\(>>\\) is the binary shift-left operator.

``` goat
              Fractional Clock Rate <+  +> Full Clock Rate
        - .-.                    .-.        .-.                   
      .->| Σ +------*---------->| Σ +----->| Σ +-------*-------> Interpolated Sinusoid  
     |    '-'       |            '-'        '-'        |           
     |     ^        v         - ^ ^      - ^ ^   .     v          
     |     |     .-----.       /  |       /  |  /|  .--+--.       
     |     |     | z⁻ᴹ |      |   |      |    '+ |<-+ z⁻¹ |       
     |     |   . '--+--' .    |   |      |   KM \|  '--+--'       
     |     |  /|    |    |\   |   |      |       '     |          
     |      '+ |<---*--->| +-'    |      |             v          
     |      K \|    |    |/ K     |      |          .--+--.       
     |         '    v    '        |       '---------+ z⁻¹ |       
     |           .-----.          |                 '-----'       
      '----------+ z⁻ᴹ +---------'                                                                    
                 '-----'                                          

```

The resulting configuration only requires one multiplication to be computed at
a fractional clock-rate. Note that practically a hardware implementation will
stagger the computation in time for each of the processing stages.

## Sigma-Delta Modulation

The purpose of digital sigma-delta modulation is primarily to reduce the
hardware requirements for signal-processing in the analogue-domain. Digitizing
a high resolution 16 bit signal is exceedingly expensive once we consider
component variation requirements if we want to preserve the fidelity of our
signal. The main idea here is the reduce the resolution of the output bitstream
while modulating the quantization noise such that accuracy is preserved in the
lower frequencies while noise due to the truncation of the digital bits is only
present at higher frequencies. This allows us to use a low resolution
digital-to-analogue converter that employs mismatch cancellation techniques
at low cost to further remove the impact of component imperfection from
corrupting the precision in-band.

A popular approach here is the use of multistage noise-shaping modulator
topologies. Here we will employ a special maximum-sequence-length configuration
from [^4] which avoids any unwanted periodicity commonly found in the output
of conventional modulators when processing certain static signals. A python
realization of this modulation process is shown below in the case of a first
order modulator.

``` python3
class Modulator:
    def __init__(self, resolution: int = 16, coupling: int = 0) -> None:
        self.acc = 0
        self.coupling = coupling
        self.resolution = resolution

    def update(self, new_val: int) -> bool:
        last_val = self.acc & 1
        pre_calc = self.acc + new_val + (self.coupling if last_val else 0)
        self.acc = pre_calc % (2 ** self.resolution)
        return last_val
```

The third-order configuration of the modulator is shown below. Here the Nx[n]
components represent the coupling factor α and simply use the Cx[n-1] bitstream
from the last cycle. This factor is a small integer chosen such that
2^N-α is a prime number given a fixed modulator resolution N.

``` goat
               .  C1[n]                              .-.                    
          D[n] |\ .-------------------------------->| Σ +--> Q[n]           
           --->+ +                                   '-'                    
               |  \                                 ^ ^                     
                \  |       .  C2[n] .-------.      /  |                     
            N1[n]| | S1[n] |\ .---->+ 1-z⁻¹ +-----'   |                     
             --->+ +--*--->+ +      '-------'         |                     
                 | |  |    |  \                       |                     
                /  |  |     \  |       .  C3[n] .-----+----.                
               |  /   | N2[n]| | S2[n] |\ .---->+ (1-z⁻¹)² |                
            .->+ /    |  --->+ +--*--->+ +      '----------'                
           |   |/     |      | |  |    |  \                                 
           |   '      |     /  |  |     \  |                                
           |  .-----. |    |  /   | N3[n]| | S3[n]                          
            '-+ z⁻¹ +'  .->+ /    |  --->+ +-.                             
              '-----'  |   |/     |      | |  |                             
                       |   '      |     /  |  |                             
                       |  .-----. |    |  /   |                             
                        '-+ z⁻¹ +'  .->+ /    |                             
                          '-----'  |   |/     |                             
                                   |   '      |                             
                                   |  .-----. |                             
                                    '-+ z⁻¹ +'                             
                                      '-----'                               
```

The output Q[n] will represent a multi-bit quantization result that increases in
bit-depth as the modulator order increases as the derivative components of CX[n]
increase in dynamic range for higher order derivatives. This has a rather
unfortunate side-effect that the signal dynamic range is only a fraction of the
total output dynamic range in this case 1/8. Fortunately these components are
exclusively high-frequency and so including a 3-tap Bartlett-Window FIR a the
output alleviates this problem by amplifying the signal-band and rejecting
the quantization-noise. In that scenario the signal dynamic range uses a little
under half the full dynamic range of the signal seen at the output.

## References:

[^1]: C. S. Turner, ''Recursive discrete-time sinusoidal oscillators,'' IEEE Signal Process. Mag, vol. 20, no. 3, pp. 103-111, May 2003. [Online]:  http://dx.doi.org/10.1109/MSP.2003.1203213.

[^2]: E. Hogenauer, ''An economical class of digital filters for decimation and interpolation,'' IEEE Trans. Acoust., Speech, Signal Process., vol. 29, no. 2, pp. 155-162, April 1981. [Online]:  http://dx.doi.org/10.1109/TASSP.1981.1163535.

[^3]: L. Lo Presti, ''Efficient modified-sinc filters for sigma-delta A/D converters,'' IEEE Trans. Circuits Syst. II, vol. 47, no. 11, pp. 1204-1213, Nov. 2000. [Online]:  http://dx.doi.org/10.1109/82.885128.

[^4]: K. Hosseini and M. P. Kennedy, ''Maximum Sequence Length MASH Digital Delta–Sigma Modulators,'' IEEE Trans. Circuits Syst. I, vol. 54, no. 12, pp. 2628-2638, Dec. 2007. [Online]:  http://dx.doi.org/10.1109/TCSI.2007.905653.
