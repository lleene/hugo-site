---
title: "A Compact Recording Array for Neural Interfaces"
date: 2013-09-13T15:26:46+01:00
draft: false
toc: true
type: posts
math: true
tags:
  - publication
  - instrumentation
  - CMOS
  - biomedical
  - sensor
---

Lieuwe B. Leene, Yan Liu, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

This paper presents a 44-channel front-end neural interface for recording both Extracellular Action Potentials (EAPs) and Local Field Potentials (LFPs) with 60 dB dynamic range. With a silicon footprint of only 0.011 mm² per recording channel this allows an unprecedented order of magnitude area reduction over state-of-the-art implementations in 0.18 μm CMOS. This highly compact configuration is achievable by introducing an in-channel Sigma Delta assisted Successive Approximation Register (\\(\Sigma\Delta\\)-SAR) hybrid data converter integrated into the analogue front-end. A pipelined low complexity FIR filter is distributed across 44-channels to resolve a 10-bit PCM output. The proposed system achieves an input referred noise of 6.41 μVrms with a 6 kHz bandwidth and sampled at 12.5 kS/s, with a power consumption of 2.6 μW per channel.

# 2 Introduction

The recent trend in on-chip instrumentation for neural electrophysiological recording has largely been motivated by the growing interest in observing large scale neuronal activity using small chronic implants. Such tools are crucial in the quest to better understand the brain, but also in revealing fundamental mechanisms behind neurological and psychiatric diseases for developing new diagnostics and therapeutic devices. Microelectronic bio-instrumentation systems currently have the capacity for profoundly impact such key scientific efforts [^1].

State-of-the-art neural recording systems have made significant progress over past years by objectively improving figures of merit, most notably that of the Noise Efficiency Factor (NEF) [^2]. This progress has not however generally had the same impact on silicon footprint, which is also critical for the long term increase in recording capacity and System-on-Chip (SOC) platforms. Although a number of compact circuits including analogue amplifiers and data converters have been proposed for biomedical applications, less attention has been given to area reduction from a system perspective apart from the typical multiplexing of the Analogue-to-Digital Converter (ADC). This is partly due to the challenge in multiplexing ultra low power analogue without significantly degrading performance (i.e. due to parasitics and inter-channel interference). The work presented herein applies a number of ideas aimed at collectively reducing the silicon area towards highly scalable systems. Through a combination of novel structures and circuit level implementations that allow for hardware reuse (and thus area reduction), this work demonstrates the capacity for unprecedented area efficiency at the system level.

The target system specifications herein apply to a Brain Machine Interface (BMI) recording the (raw) signal including both LPFs and EAPs. Furthermore, such a system can provide undistorted EAP recordings which are typically due to a high pass filter centred around 100--500 Hz. This implies an input-referred signal amplitude ranging from 10 μV to 10 mV, which has a dynamic range equivalent to that of a10-bit converter with a frequency bandwidth of 100 mHz to 3 kHz for optimal data post processing [^1]. This system aims towards a robust SOC platform, utilising a fully-differential structure to reject supply noise, as well as even order distortion harmonics, for the integration of a very large number of recording channels with wireless and digital post-processing systems.

This organisation of this paper is as follows: Section 3 outlines the proposed system-level architecture; Section 4 details the circuit level implementation; Section 9 presents simulated system and circuit level results; and finally, Section 10 compares the overall system characteristics to the current state-of-the-art and concludes the paper.

# 3 System Architecture

{{< figure src="/images/biocas2013/I1.png" title="Figure 1: Top level architecture of the proposed system." width="500" >}}

The top level system is illustrated in Fig 1, showing the in-channel architecture consisting of two multiplexed low noise amplifiers, a hybrid data converter, and two ultra compact digital filters. The system integrates 44-channels together with the primary objective being to combine state-of-the-art instrumentation techniques to achieve a substantial reduction in area through a novel implementation. The Front End Amplifier (FEA) utilises a chopper technique to alleviate the need for very large transistors and a Sigma Delta assisted Successive Approximation Register (\\(\Sigma\Delta\\)-SAR) is developed to significantly reduce the size of the capacitor bank typically required for a 10-bit resolution output. This capacitor bank is also used to implement a switched-capacitor digital filter to reject the unwanted chopper harmonics thus avoiding the requirement for additional analogue filter blocks. Finally, the filter needed to decimate the \\(\Sigma\Delta\\)-SAR modulator output is shared in the digital domain through a pipeline structure that require only a low resolution accumulator, thereby mitigating the computational costs typically associated with \\(\Sigma\Delta\\) decimation.

# 4 Circuit Implementation

## 5 Chopper Modulated Analog Front End

{{< figure src="/images/biocas2013/I2.png" title="Figure 2:FEA structure illustrating the feedback and chopper configuration." width="500" >}}

The AFE is illustrated in Fig. 2. This Capacitively-Coupled Chopper Instrumentation Amplifier (CCIA) [^3] consists of a Miller compensated 2-stage design with capacitive feedback. Using a single analogue block for amplification naturally has its trade-off as the high gain requirement implies a large input capacitance C<sub>in<sub> = 6.5 pF) but at the same time reduces the value of the Miller capacitor that introduces the dominant pole of the system for a given thermal noise floor. The feedback network is configured to introduce 34 dB of differential gain and improve the input impedance of the amplifier through positive feedback where C<sub>fp<sub> = C<sub>fb<sub>, Zin=\\( \frac{Gain}{2 \cdot f_{chop} \cdot C_{in}}\\) = 77 MΩ, and f<sub>chop<sub> = 50 kHz.

{{< figure src="/images/biocas2013/I5.png" title="Figure 3:Circuit level schematic of the FEA." width="500" >}}

The circuit level schematic of the FEA is shown in Fig. 3. This implementation uses the complementary input pair to allow good current efficiency for the 1.8 V analogue supply together with a class-AB, low output resistance, cascade gain stage to drive the large switching capacitance loading the output from the feedback network. The circuit also includes the common mode feedback and ADC sampling capacitors. A MOS capacitor is used to introduce the dominant pole at 6 kHz while the feedback network is implemented using MIM capacitors. The overall high pass behaviour of this structure is implemented through the periodic reset of the input and the output which also auto-zeros the input pair offset. This offset compensation is maintained outside the reset phase by biasing the gate of the reset switch at the mid-rail voltage such that it behaves as a traditional MOS-based pseudo-resistor. This reset mechanism benefits due to the improved noise characteristic over a DC-servo loop implementation that also requires a significant amount of additional area. However, the signal distortion introduced though this technique can be compensated in the digital domain [^4]. All current sourcing transistors (M5-M10) have cascode implementations (not shown in Fig. 3) to provide adequate common mode rejection and common mode input range of \\(\pm\\)200 mV, which is biased and filtered through the reset switch.

## 6 Hybrid \\(\Sigma\Delta\\) assisted SAR ADC

The data converter is based on extending the resolution of a small 6-bit SAR ADC with a continuous time \\(\Sigma\Delta\\) modulator that resolves the remaining quantisation error residue from the SAR algorithm. The primary components of the modulator are integrated into the pre-gain stage structure of the comparator as illustrated in Fig. 4. During initial SAR operation the gm-C filter is switched out and the input pair directly feeds into a diode-connected load for wideband operation while the filter capacitors are reset. Once the last SAR bit is resolved the loop filter is enabled implementing a second-order chain of integrators with a weighted feedforward summation modulator topology that allows low power operation with minimised signal distortion. Note that in Fig. 4 during SAR operation V\\(\Sigma\Delta\\) is at the common mode and is then modulated between ±V<sub>ref<sub> such that the feedback is necessarily always twice as large as the residue error to ensure modulator stability and optimal residue quantisation.

{{< figure src="/images/biocas2013/I3.png" title="Figure 4: Circuit level schematic of the hybrid \\(\Sigma\Delta\\)-SAR converter." width="500" >}}

The general organisation and operation of the ADC is illustrated in Fig. 7. Given that N=6 is the resolution of the SAR DAC and OSR=44 is the conventional oversampling ratio of the modulator. It can be observed that both SAR and \\(\Sigma\Delta\\) operation is at 5 MHz and takes N+OSR cycles to finish or a total of 10 μs for a sampling rate of 25 kHz at the 25 % duty cycle. In addition to using 5 reference voltages this topology makes a extreme reduction in size by a factor of 32 and will allow large 8 by 8 μm² unit capacitors to reduce the sensitivity of process variation thereby achieving a 10-bit resolution without any in-channel calibration.

## 7 Chopper Rejection

In order to reject chopper harmonics introduced by the up-modulated offset aggressors, the capacitive array is used as a switched capacitor network to implement a notch filter centred around the odd harmonics of the chopper frequency when the data converter is not operational. The output of the AFE is sampled in the time domain and weighted using different sets of capacitors to implement a 3<sup>rd<sup> order Bartlett window filter before ADC conversion. This technique avoids the need for a ripple reduction loop which typically also requires an analogue filter with large capacitors. Fig. 5 shows the 4-phase sampling sequence that operates at 50 kHz. The net charge, Q<sub>total<sub>, quantised by the converter is expressed as follows.

$$ \frac{Q_{total}}{C_{unit}} = 8 V_{diff} \left[ n-1 \right]  + 16 V_{diff} \left[ n-2 \right] + 8 V_{diff} \left[ n-3 \right] $$

Where V<sub>diff<sub> is the sampled differential output voltage of the amplifier and C<sub>unit<sub> is the 120 fF unit capacitance of the converter that also averages sampling noise during conversion. This allows the notch filter characteristic illustrated in Fig. 5, to reject a significant amount of high frequency aggressors.

{{< figure src="/images/biocas2013/F2.png" title="Figure 5:Switched capacitor filter timing diagram (left) and frequency response (right)" width="500" >}}

## 8 Digital Filter

The filter structure used to process the \\(\Sigma\Delta\\) output is illustrated in Fig. 6. This structure distributes the overall structure across all channels such that each channel requires only a 7-bit register, a 12-bit registered add/subtract accumulator as well as the two 7-bit registers from the SAR to implement the hybrid functionality demonstrated here. The filter coefficients are hardwired into each channel's 7-bit register such that it is loaded during reset and circulated through all channels.

{{< figure src="/images/biocas2013/I6.png" title="Figure 6:Implementation of the pipelined FIR structure." width="500" >}}

The \\(\Sigma\Delta\\) output sign modulates the accumulator which integrates over a 44-point hanning window, implementing a FIR filter without multipliers. A more traditional decimation filter implemented using a cascaded integrator comb (CIC) filter is much less effective here. This is because the structures cannot be shared (across channels) and will require a larger number of samples than the OSR to evaluate the residue error which due to the intermediate SAR process being continuously disrupted. Fortunately the resolution only needs to be extended by 4-bits to achieve the required 60 dB dynamic range. Therefore a compact 44<sup>th<sup> order window at 7-bit unsigned resolution suffices. The structure has shown to make a good estimate of the stationary input to the modulator even with high levels of quantisation noise allowing us to decrease to resolution of the stored coefficients that are given by the following expression.

$$ w[n] = C \cdot \left[ 1 - cos \left( \frac{2 \pi n}{N-1}\right) \right]^{0.7} $$

The coefficients, w[n], represent a modified hanning window that results in a better Differential Non-Linearity (DNL) characteristic over other FIR windows when quantised to 7-bits. Note that C=0.024, N=46, and $n \in \left[1, 2, ..., N-2 \right]$ represent the normalisation constant, effective filter order, and the non-zero coefficient index respectively.

{{< figure src="/images/biocas2013/example.png" title="Figure 7: Transient operation of the ADC conversion." width="500" >}}

{{< figure src="/images/biocas2013/os.png" title="Figure 8: Output of the analogue channel with a 19 mV peak to peak 1 kHz input." width="500" >}}

# 9 Simulation Results

Preliminary validation of the proposed implementation has been done through schematic level simulations in the Cadence IC 6.1.5 Design Environment using industry provided PSP models for the commercially available 6 Metal 0.18 μm CMOS technology (AMS/IBM C18A6/7SF). The entire channel has been stimulated with 19 mV peak to peak 1 kHz differential signal for full swing at the ADC input of which a single ADC conversion is illustrated in Fig. 7. The quantised output spectrum of this simulation is shown in Fig. 8 which indicates a 1.2% total harmonic distortion for a full swing output that is due to the AFE. Fig. 10 illustrates the characteristics of the FIR filter in time and frequency domain respectively. Fig. 11 presents 10.2 ENOB performance through the 0.5 LSB bounded integral and differential non-linearities of the converter. The channel level layout is shown in Fig. 12 indicating a 440 μm by 50 μm area requirement for 2 recording channels.

{{< figure src="/images/biocas2013/noise.png" title="Figure 9: Noise density simulated at the output of the FEA" width="500" >}}

{{< figure src="/images/biocas2013/F1.png" title="Figure 10: 7-bit quantised Hanning FIR filter showing frequency (top) and time (bottom) domain responses." width="500" >}}

{{< figure src="/images/biocas2013/F3.png" title="Figure 11: \\(\Sigma\Delta\\)SAR non-linearities showing INL (top), DNL (bottom)" width="500" >}}

{{< figure src="/images/biocas2013/Area2.png" title="Figure 12: Layout of 4 Channels integrated together with CMIM capacitors overlaying the 440 μm by 100 μm silicon footprint." width="500" >}}

# 10 Conclusion

The ultra compact topology presented has demonstrated the means by which the recording channel can scale down below a 0.01 mm² area while maintaining its recording fidelity and advanced spectral filtering characteristics. In addition the proposed 10 bit hybrid data converter achieves a factor of 32 reduction in area over equivalent data converters through pipelining and \\(\Sigma\Delta\\) modulation. With an input referred noise of 6.4 μVrms this system consumes 2.6 μW resulting in excellent Noise Area product of 0.007 μVrms mm². The overall system characteristics are shown in Table 1 demonstrating respectable performance particularly with respect to the order of magnitude reduction in area per channel and the 60 dB dynamic range for the given power budget.

Table 1: Performance per channel of Neural Recording Arrays
|Reference | [^5] | [^6] | [^7] | [^8] | This work |
|----|----|----|----|----|----|
|Year | 2011 | 2012 | 2012 | 2012 | 2013 |
|Tech. [nm]  | 180 | 250 | 130 | 130 | 180 |
|Power [μW] | 10.1 | 3.96 | 68 | 5.9 | 2.59 |
|High Pass [Hz] | 126m | 100m | 1 | 200 | 100m |
|Low Pass [Hz] | 12k | 17k | 10K | 6.9K | 6K |
|Noise [μVrms]  | 5.4 | 4.8 | 2.2 | 3.8 | 6.41 |
|NEF |  4.4 | 2.9 | 4.5 | 2.16 | 2.27 |
|Area [mm²]  | 0.31 | 0.07 | 0.19 | 0.16 | 0.011 |
|ADC Res. | 8 | 9 | 10 | 8 | 10 |
|Sample [kS/s]  | 125 | 60 | 31 | 27 | 12.5 |

# 11 Acknowledgment

This work was supported by the UK EPSRC (grants EP/I000569/1 and EP/K015060/1).

# Refernces:

[^1]: F.K. etal., ''Drug discovery: A jump-start for electroceuticals,''  Nature, vol. 496, pp. 159--161, 2013.
[^2]: R.Rieger, Y.-Y. Pan, and J.Taylor, ''Design strategies for multi-channel  low-noise recording systems,'' in Circuits and Systems, 2007. ISCAS  2007. IEEE International Symposium on, 2007, pp. 561--564.
[^3]: Q.Fan, F.Sebastiano, J.Huijsing, and K.Makinwa, ''A 1.8 w 60 nv hz  capacitively-coupled chopper instrumentation amplifier in 65 nm cmos for  wireless sensor nodes,'' Solid-State Circuits, IEEE Journal of,  vol.46, no.7, pp. 1534--1543, 2011.
[^4]: Y.Chen, A.Basu, and M.Je, ''A digitally assisted, pseudo-resistor-less  amplifier in 65nm cmos for neural recording applications,'' in Circuits  and Systems (MWSCAS), 2012 IEEE 55th International Midwest Symposium on,  2012, pp. 366--369.
[^5]: W.Wattanapanitch and R.Sarpeshkar, ''A low-power 32-channel digitally  programmable neural recording integrated circuit,'' Biomedical Circuits  and Systems, IEEE Transactions on, vol.5, no.6, pp. 592--602, 2011.
[^6]: K.Al-Ashmouny, S.-I. Chang, and E.Yoon, ''A 4 $\mu$w/ch analog front-end  module with moderate inversion and power-scalable sampling operation for 3-d  neural microsystems,'' in Biomedical Circuits and Systems Conference  (BioCAS), 2011 IEEE, 2011, pp. 1--4.
[^7]: H.Gao, R.Walker, P.Nuyujukian, K.Makinwa, K.Shenoy, B.Murmann, and  T.Meng, ''Hermese: A 96-channel full data rate direct neural interface in  0.13 m cmos,'' Solid-State Circuits, IEEE Journal of, vol.47, no.4,  pp. 1043--1055, 2012.
[^8]: A.Rodriguez-Perez, J.Masuch, J.Rodriguez-Rodriguez, M.Delgado-Restituto,  and A.Rodriguez-Vazquez, ''A 64-channel inductively-powered neural recording  sensor array,'' in Biomedical Circuits and Systems Conference (BioCAS),  2012 IEEE, 2012, pp. 228--231.
