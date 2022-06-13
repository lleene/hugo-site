---
title: "Autonomous SoC for neural local field potential recording in mm-scale wireless implants"
date: 2018-07-23T15:26:46+01:00
draft: false
toc: true
type: posts
math: true
tags:
  - publication
  - CMOS
  - wireless
  - system-on-chip
  - biomedical
---

Lieuwe B. Leene, Peilong Feng, Michal Maslik, Katarzyna M. Szostak, Federico Mazza, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

Next generation brain machine interfaces fundamentally need to improve the information transfer rate and chronic consistency. This needs them to be highly scalable but also to observe signals that are stable over time. Towards this aim, this paper presents a novel System-on-Chip (SoC) for a mm-scale wireless neural recording node that can be implanted in a distributed fashion. The proposed self-regulating architecture allows each implant to operate autonomously and adaptively load the electromagnetic field to extract a precise amount of power for full-system operation. This can allow for a large number of recording sites across multiple implants extending through cortical regions without increased control overhead in the external head-stage. By observing only local field potentials (LFPs), chronic stability is improved and good coverage is achieved whilst reducing the spatial density of recording sites. The system features a \\(\Delta\Sigma\\) based instrumentation circuit that digitises high fidelity signal features at the sensor interface thereby minimising analogue resource requirements while maintaining exceptional noise efficiency. This has been implemented in a 0.35 μ m CMOS technology allowing for wafer-scale post-processing for integration of electrodes, RF coil, electronics and packaging within a 3D structure. The presented configuration will record LFPs from 8 electrodes with a 825 Hz bandwidth and an input referred noise figure of 1.23μ V<sub>rms<sub>. The resulting electronics has a core area of 2.1 mm²  and a power budget of 80 μW.

# 2 Introduction

There has been significant effort in developing integrated circuits for Brain Machine Interfaces (BMIs)[^1]. These systems enable a wide range of applications from recording neural signals for scientific study to treating neurological conditions. They integrate a multitude of functions for sensing, processing, telemetry and power management. There is a drive to develop wireless modules that are hermetically packaged for chronic implant applications[^2]. Moreover, any reduction in size can substantially improve device efficacy by reducing the impact on surrounding tissue. Any reduction in weight is also highly desirable for behaving animal studies. While a number of proposed systems have relied on PCB[^3] or flexible [^4] technologies that allow low cost, rapid development. This approach leads to substantially larger implants when compared to silicon-based integration[^1]. This is because the silicon substrate enables a large number of electrodes to be integrated directly onto the active die in the shape of an implantable shank[^5]. In contrast, making a large number of intra-device connections has a significant impact on device footprint as well as fabrication complexity with added bio-compatibility constraints [^6]. For this reason a number of groups are investigating millimetre-scale solutions for recording[^7] and stimulation[^8] with all aspects of the implant integrated within the silicon die or micro-machined package.

{{< figure src="Figures/ENGINI.pdf" title="Figure 1: The ENGINI concept showing: (a) multiple freely floating probes being wirelessly interrogated by a headstage unit; (b) schematic representation." width="500" >}}

The 'Empowering Next Generation Implantable Neural Interfaces' (ENGINI) project achieves its scalability by utilising multiple mm-scale probes that are each implanted and 'freely floating' in the cortex. These observe field potentials along the cortical column but also laterally through different probes. These are wirelessly coupled to an external headstage with trancutanious and transdural inductive links to deliver power and exchange data. This is illustrated in Fig. 1.

This particular system relies on the autonomous behaviour of each probe such that a downlink is not required and each probe simply backscatters recorded activity using load shift keying (LSK) modulated at different preconfigured frequencies derived from the carrier. This allows each probe to be uniquely identified without increased control overhead for larger ensembles of probes. The probe circuit additionally includes all front-end instrumentation. An aggressive strategy is thus needed to reduce system complexity to enable package miniaturisation. Such a system may therefore not be able to incorporate more advanced functionality found in the state-of-the-art[^9]. Instead the electronics will perform direct quantization of the 1-825 Hz local field potential (LFP) signal bandwidth that is transmitted directly without compression to allow long term recordings with sub-millimetre spacial resolution for chronic BMI applications. The rest of this paper is organised as follows: Section 3 details the overall system operation and high level implementation; Section 4 describes the circuit implementation; Section 8 presents simulation results and system characteristics; and Section 9 concludes this work with respect to the achieved performance.

# 3 System Architecture


The integrated system architecture is shown in Fig. 2. This shows a single recording unit which is inductively coupled to a primary coil L<sub>1<sub> that provides power using a 433 MHz carrier to leave sufficient bandwidth for frequency division multiplexing multiple recording units. In fact the receiving coil L<sub>2<sub> will be located on a passive undoped silicon interposer that is flip-chip bonded to the active instrumentation IC. The resonant tank L<sub>2<sub> C<sub>2<sub> receives the transmitted power and establishes a DC voltage on V<sub>DD<sub> once the rectifier down-converts the carrier. First a biasing circuit is powered that generates digital flags that indicate the supply voltage level. These flags assist the self-tuning control algorithm to adjust the loading capacitance C<sub>T<sub> to tune or detune the resonant tank L<sub>2<sub>C<sub>2<sub> and receive a specific amount of power to establish 1.5 V on the V<sub>DD<sub> supply. This feedback regulates the supply voltage in a course manner without needing active control from the primary side (external controller). This implies the analogue circuits need to accommodate for any fluctuations without diminishing sensor precision. The continuous-time fully-differential modulator topology will further prevent these supply noise aggressors from being aliased in-band during sampling. The system clock can be directly extracted from the resonant tank using adiabatic logic elements to implement a series of frequency dividers before passing the clock to the digital core[^10].

{{< figure src="Figures/SYS.pdf" title="Figure 2: ENGINI system architecture for recording LFP at high resolution. This tunes the receiving resonant tank L<sub>2<sub>C<sub>2<sub> to regulate V<sub>DD<sub>." width="500" >}}


# 4 Circuit Implementation


This ENGINI prototype has been developed for a 0.35 μ m CMOS technology such that assembly of the 3D probe can be performed in-house using low-cost micro-fabrication and micro-packaging techniques. The implementation of each subsystem will be detailed below.

## 5 Self-Regulated Power Harvesting


This provides a stable power supply for the electronics and back-scatters digitised recordings. The circuit architecture is shown in Fig. 3. This contains a binary weighted capacitor bank C<sub>T<sub>, a passive full wave rectifier, and a sensing circuit which are all digitally-controlled. The principle of operation can be described as follows. First, the cross-coupled rectifier converts the induced AC voltage to a DC power on V<sub>x<sub>. Then, the low voltage amplifier A<sub>2<sub> performs auto-zeroing by shorting C<sub>F<sub> and simultaneously sampling the rectified voltage onto C<sub>I<sub>. After sampling, the parallel binary-weighted capacitor bank C<sub>T<sub> is adjusted to tune or de-tune LC tank on the secondary side. There is therefore a voltage fluctuation at node V<sub>x<sub>. The change in V<sub>x<sub> is amplified 30\\(\times\\) by A<sub>2<sub> which corresponds to the ratio C<sub>I<sub>/C<sub>F<sub>. The polarity of the resulting change is digitised using the comparator, instructing the digital control to add or remove parallel capacitors in the next cycle of regulation. Two supply voltage level indicators from the biasing circuit further assist this feedback to increase or reduce the supply voltage and whether to perform LSK respectively. The resistor R<sub>z<sub> is added after the output of rectifier such that the speed at which V<sub>X<sub> can be controlled is not dependent on the load capacitance C<sub>L<sub> which may be quite large. This allows fast regulation with a clock speed of 846 kHz at the cost of some reduction in power efficiency due to the voltage drop from V<sub>X<sub> to V<sub>DD<sub>.

{{< figure src="Figures/REG.pdf" title="Figure 3: Adaptive power conversion and regulation circuit using full-wave rectifier, tunable LC tank, auto-zeroing amplifier and strong arm comparator" width="500" >}}
%

## 6  \\(\Delta\Sigma\\) Instrumentation Circuit



The instrumentation circuit used to acquire the electrode recordings is based on the time-domain \\(\Delta\Sigma\\) modulator in [^11]. This uses differential oscillators as the integration element with an asynchronous signal quantizer. However the implementation presented here introduces an additional Gm-C integrator and a feed-forward path to realise second-order noise shaping. This reduces the oversampling ratio (OSR) requirement and substantially increases the dynamic range of the system. A single-ended equivalent of the fully-differential structure used here is shown in Fig. 4.

{{< figure src="Figures/SDM.pdf" title="Figure 4: Simplified equivalent of the second-order \\(\Delta\Sigma\\) modulator using time-domain signal quantization exhibiting a bandpass response due to the switched current DAC which removes any electrode offset." width="500" >}}
%

Note that this is a DC-coupled configuration where the analogue node V<sub>O<sub> tracks the electrode potential. An electrode offset larger than \\(\pm\\)100 mV can be accommodated without saturating the modulator by adding the digitally switched and duty cycled current in the feedback path. The quantized signal Q is AC coupled onto V<sub>O<sub> with a relatively large attenuation factor due to capacitive division α=1/(C<sub>0<sub>/C<sub>C<sub>+1) which will allow the in-band signal gain. This can be confirmed using the small signal model for this circuit described in Eq. 1-4 where H(s) represents the second-order loop filter and C(s) the charge pump with capacitive feed-forward. The factor k1=OSR f<sub>smp<sub>/2 reflects the modulator bandwidth in terms of the target sampling frequency f<sub>smp<sub>. The factor k2=2\\(\pi\\) f<sub>hp<sub> represents the integration constant of the charge pump in terms of the high-pass cut-off frequency f<sub>hp<sub>. This approach is inspired by the first order modulator in [^12]. The implemented circuit uses an OSR of 64, a 1 Hz high-pass corner frequency, and third order CIC filter to decimate the output. This leads to the noise and signal transfer functions shown in Fig. 5.

$$  STF(s) = \frac{H}{1+\alpha C H} $$

$$  H(s) = \left( 2 + \frac{k1}{s} \right)  \frac{k1}{\alpha   s} $$

$$  NTF(s) = \frac{1}{1+\alpha C H} $$

$$  C(s) = 1 + \frac{k2}{s} $$

{{< figure src="Figures/BODE.pdf" title="Figure 5: Analytical quantisation noise and signal transfer functions of the proposed modulator configuration." width="500" >}}

## 7 Reference and Biasing Circuit

The reference circuit loosely based on [^13] is used to establish the required noise shaping and precision in the \\(\Delta\Sigma\\) modulators. This provides a stable bias current using the structure shown in Fig. 6. Its core entails a β-multiplier generating a reference current of 800 nA flowing through resistor R<sub>1<sub>. This is scaled and mirrored to generate 8 current sinks for the front-end. Generation of a nominal 1.2 V reference is achieved by passing the reference current through a diode-connected PNP BJT B<sub>1<sub> and multiplying the BE (base-emitter) voltage using amplifier A<sub>2<sub> with resistive feedback. As the output voltage V<sub>REF<sub> primarily depends on the BJT BE voltage and ratio of R<sub>2<sub> and R<sub>3<sub> it is possible to achieve a very accurate voltage output independent of process variation.

Since the circuit is going to be operated in a neural implant it is expected that its operating temperature is going to remain stable and it is therefore not necessary to optimise the circuit for temperature independence. The main design target therefore lies in maximisation of the achieved PSRR (Power Supply Ripple Rejection) and minimisation of power consumption. The PSRR of the β-multiplier is maximised by cascoding both PMOS and NMOS current mirrors (M<sub>1<sub>\&M<sub>2<sub>, M<sub>3<sub>\&M<sub>4<sub>) [^14]. The same is achieved for V<sub>REF<sub> by employing a regulated cascode for BJT current generation.

In addition, the reference circuit generates logic levels indicating that the supply voltage has reached \\(\approx\\) 1 V, 1.3 V and 1.5 V used by the control loop of the SoC. The first indicator (1 V) is designed using a current source inverter as described in [^15]. The remaining two indicators are derived from V<sub>REF<sub> to ensure good tolerance to process variations.

{{< figure src="Figures/refc.pdf" title="Figure 6: Schematic of the reference and biasing circuit (start-up circuit not shown)." width="500" >}}

# 8 Simulation Results

The circuit was designed and validated using PSP models from the commercially available AMS 0.35 μ m CMOS technology (C35B4C3 4M/2P/HR/5V).

Preliminary simulation results show the instrumentation achieves a thermal noise floor of 45 nV<sub>rms<sub>/\\(√{\text{Hz}}\\) and uses 2.25μ A of current from a 1.5 V supply including also the decimation filter. This indicates a 3.4 μ W power budget per recording channel. The decimated output is shown in Fig. 7, achieving a dynamic range larger than 80 dB since the maximum modulator input range is \\(\pm\\)6 mV excluding the \\(\pm\\)100 mV linear range of the charge pump feedback.

The designed reference circuit consumes a bias current of 5 μ A and generates an output nominal voltage V\tss{REF,μ}=1.208 V with a standard deviation of σ =10.87 mV as shown by post-layout Monte Carlo simulation of 500 runs. Similarly, the output bias current was found to be I\tss{REF,μ}=150.4 nA and σ <sub>IREF<sub>=15.6 nA. The mismatch between two different bias currents has a standard deviation of σ \tss{\\(\Delta\\)IREF}=5.35 nA. The PSRR of the reference voltage with respect to frequency can be seen in Fig. 8. This shows that the reference circuit features an almost flat frequency response and a PSRR higher than 70 dB at small and high frequencies.

The overall system specifications are summarised in Table 1. Comparing the ENGINI system with other SoCs for brain machine interfaces demonstrates an increase in dynamic range and reduction in core size for equivalent noise performance as a result of the proposed architecture. The active silicon CMOS is currently being fabricated and will be flip-chip bonded onto a silicon based carrier. The two dies are illustrated and annotated in Fig. 9. Both dies are 16 mm² in size however the interposer is passive and only needs to embed the seal, coil, and electrode interconnect metallisation. Preliminary characterisation has shown that the L<sub>2<sub> can have an inductance of 5 nH with a Q-factor \textgreater12.

{{< figure src="Figures/SPEC.pdf" title="Figure 7: Output spectrum of the \\(\Delta\Sigma\\) instrumentation circuit from transient simulation using a 10 mVpp sinusoidal input tone at 210 Hz." width="500" >}}

{{< figure src="Figures/PSRR.pdf" title="Figure 8: PSRR (Power Supply Ripple Rejection) at V<sub>REF<sub>. This shows a PSRR of μ =78.29 dB & σ =1.58 dB, μ =69.94 dB & σ =1.59 dB and μ =79.95 dB & σ =0.52 dB at DC, 64 kHz and 433 MHz respectively." width="500" >}}

Table 1: System Characteristics and Comparison with State-of-the-Art
|		Parameter  [unit]	| This Work \\(\dagger\\)  | [^1] | [^16] | [^3]|
|----|----|----|----|----|
|		Year 				| **2017** | 2017 | 2015 | 2016 |
|		Application				| **LFP** | ECoG | ECoG | EAP |
|		Tech.[nm]		| **350**	 | 180  | 65 | 350 |
|		Supply-V[V]	| **1.5**   | 0.8 | 0.5 | 1.8|
|		Total-P[W]	| \textbf{80 μ}(\star) | 0.1 m | 0.2 m | 51 m |
|    Core-A[mm²]	| **2.1** |	9 | 5.8 | 12.5 |
|    \# Channels				| **8** | 16 | 64 | 8|
|    Bandwidth[Hz]		| **825** | 1 k | 500	| 11 k|
|    DR[dB] 			| **85**	|	55 | 52 | 50 |
|    IRN  [μ V<sub>rms<sub>] | **1.3** | 1.5 | 1.3 | 2.9 |
\\(\dagger\\) Based on preliminary simulation results. \\(\star\\) Includes rectifier loss.

{{< figure src="Figures/D2D.pdf" title="Figure 9: Annotated design for each silicon die that will be flip-chip bonded together. This shows the bonding pads, inductive coil, seal ring, and core ENGINI system to scale." width="500" >}}

# 9 Conclusion

This work demonstrates a compact system on chip architecture for LFP based recording systems that aims to distribute several implantable probes into the cortical tissue in a scalable fashion by relying on autonomous sensor operation. Using the resonant tuning for supply regulation and \\(\Delta\Sigma\\) modulator instrumentation has lead to a significant reduction in system complexity typically seen in BMI SoCs. Moreover this configuration is able to operate at high efficiency without much constraint on technology requirements since the overall system power budget is estimated to be 80 μ W from preliminary simulation results. The approach to brain machine interfaces presented here will lead to safer and simpler systems while delivering high fidelity multi-electrode recordings which is essential for applications in a clinical environment.%

# 10 Acknowledgement

This work was supported by EPSRC grant EP/M020975/1.

# References:

[^9]: M.A.B. Altaf, C.Zhang, and J.Yoo, ''A 16-channel patient-specific seizure  onset and termination detection SoC with impedance-adaptive transcranial  electrical stimulator,'' IEEE J. Solid-State Circuits, vol.50,  no.11, pp. 2728--2740, Nov 2015.
[^1]: S.Ha etal., ''Silicon-integrated high-density electrocortical  interfaces,'' Proc. IEEE, vol. 105, no.1, pp. 11--33, Jan 2017.
[^16]: R.Muller etal., ''A minimally invasive 64-channel wireless $\mu$ECoG  implant,'' IEEE J. Solid-State Circuits, vol.50, no.1, pp.  344--359, 2015.
[^8]: A.Khalifa, J.Zhang, M.Leistner, and R.Etienne-Cummings, ''A compact,  low-power, fully analog implantable microstimulator,'' in IEEE Proc.  ISCAS, May 2016, pp. 2435--2438.
[^7]: E.Moradi etal., ''Backscattering neural tags for wireless  brain-machine interface systems,'' IEEE Trans. Antennas Propag.,  vol.63, no.2, pp. 719--726, Feb 2015.
[^6]: Y.K. Lo etal., ''A fully integrated wireless SoC for motor function  recovery after spinal cord injury,'' IEEE Trans. Biomed. Circuits  Syst., vol.11, no.3, pp. 497--509, June 2017.
[^11]: L.Leene, T.Constandinou etal., ''A 0.5 V time-domain  instrumentation circuit with clocked and unclocked operation,'' in  IEEE Proc. ISCAS, May 2017, pp. 2619--2622.
[^5]: C.M. Lopez etal., ''A neural probe with up to 966 electrodes and up to  384 configurable channels in 0.13$\mu$m SOI CMOS,'' IEEE Trans.  Biomed. Circuits Syst., vol.11, no.3, pp. 510--522, June 2017.
[^4]: S.A. Mirbozorgi etal., ''A single-chip full-duplex high speed  transceiver for multi-site stimulating and recording neural implants,''  IEEE Trans. Biomed. Circuits Syst., vol.10, no.3, pp. 643--653,  June 2016.
[^12]: H.Kassiri etal., ''27.3 all-wireless 64-channel 0.013mm$^2$/ch  closed-loop neurostimulator with rail-to-rail DC offset removal,'' in  IEEE Proc. ISSCC, Feb 2017, pp. 452--453.
[^2]: D.A. Schwarz etal., ''Chronic, wireless recordings of large-scale  brain activity in freely moving rhesus monkeys,'' Nature Methods,  vol.11, pp. 670--676, April 2014.
[^15]: M.H. Cho etal., ''Development of undervoltage lockout (UVLO) circuit  configurated schmitt trigger,'' in IEEE Proc. ISOCC, Nov 2015, pp.  59--60.
[^14]: G.Giustolisi and G.Palumbo, ''A detailed analysis of power-supply noise  attenuation in bandgap voltage references,'' IEEE Trans. Circuits  Syst. I, vol.50, no.2, pp. 185--197, Feb 2003.
[^13]: Y.Osaki, T.Hirose, N.Kuroki, and M.Numa, ''1.2-V supply, 100-nW,  1.09-V bandgap and 0.7-V supply, 52.5-nW, 0.55-V subbandgap reference  circuits for nanowatt CMOS LSIs,'' IEEE J. Solid-State Circuits,  vol.48, no.6, pp. 1530--1538, June 2013.
[^10]: S.Houri etal., ''Limits of CMOS technology and interest of NEMS  relays for adiabatic logic applications,'' IEEE Trans. Circuits Syst.  I, vol.62, no.6, pp. 1546--1554, June 2015.
[^3]: S.B. Lee etal., ''An inductively-powered wireless neural recording  system with a charge sampling analog front-end,'' IEEE Sensors J.,  vol.16, no.2, pp. 475--484, Jan 2016.
