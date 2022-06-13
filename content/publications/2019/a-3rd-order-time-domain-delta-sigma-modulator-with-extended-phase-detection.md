---
title: "A 3rd order time domain delta sigma modulator with extended-phase detection"
date: 2019-05-26T15:26:46+01:00
draft: false
toc: true
type: posts
math: true
tags:
  - publication
  - CMOS
  - time-domain
  - instrumentation
  - circuit
---

Lieuwe B. Leene, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

This paper presents a novel analogue to digital converter using an oscillator-based loop filter for high-dynamic range bio-sensing applications. This is the first third-order feed-forward ΔΣ  modulator that strictly uses time domain integration for quantisation noise shaping. Furthermore we propose a new asynchronous extended-phase detection technique that increases the resolution of the 4 bit phase quantiser by another 5 bits to significantly improve both dynamic range and reduce the noise-shaping requirements. Preliminary simulation results show that this type of loop-filter can virtually prevent integrator saturation and achieves a peak 88 dB SNDR for kHz signals. The proposed system has been implemented using a 180 nm CMOS technology occupying 0.102 mm²  and consumes 13.7 μ W of power to digitise the 15 kHz signal bandwidth using a 2 MHz sampling clock.

# 2 Introduction

Time and frequency based circuit techniques have received considerable interest in the recent years as a means to solve key challenges with integrating traditional analogue functionality into digital systems and take advantage of technology scaling [^1]. A feature in many of these developments relies on the ease by which an analogue voltage or current can be converted into time encoded signals using a simple digital ring oscillator that interfaces directly with standard logic elements. Generally time encoding implies that the analogue signal is represented by the time interval between digital events where we may use the frequency or phase difference to encode digital bit streams that are termed continuous time binary value (CTBV) signals.

In ADCs specifically, frequency readout carefully counts the number of oscillations relative to a precise reference clock period[^2] while phase readout digitises the relative phase difference of two matched oscillators using an array of phase detectors [^3]. Seemingly the advantage of using a counter is that the dynamic range of the output is more flexible in the sense that the counter depth is adjustable to realise low or high precision readout. In contrast phase readout directly relates the number of delay stages to the number of quantisation levels which makes high resolution phase quantisation resource intensive in the analogue sense as these delay stages should be matched to avoid off-sets and spurious tones. The advantage of the later is that the output is unary encoded with inherent mismatch averaging properties that simplifies the feedback circuitry during digital to analogue conversion [^3]. That said, effort has been made to improve the phase digitisation in other ways but has been limited to single bit improvements [^4] or constrains the system to use synchronous operation [^5].

Both readout techniques conventionally use synchronous circuits where the the timing information is latched which makes it difficult to further process signals in the time-domain without incurring quantisation noise. This can obstruct higher order noise shaping schemes although several solutions have already been proposed. For instance [^6] uses gated ring oscillators to realise a multi-stage noise shaping (MASH) topology and [^7] uses a higher-order analogue loop-filter to precede the oscillator to improve dynamic range. However both have yet to demonstrate the feasibility for high dynamic range data conversion and the analogue reliance limits the scalability of time-based operation in a way that is characteristically more useful for digital systems.

More recent work considers the use of asynchronous readout that may be able to process signals entirely in the time-domain with reduced analogue complexity [^10][^8][^9]. This is promising as a variety of specialised loop filter topologies can not be realised using synchronous prior art. Moreover asynchronous digital systems can utilise a number of power-saving techniques such as signal-activity dependent processing [^11] or event driven control to reduce complexity and speed up operation [^12].

{{< figure src="/images/iscas2019/td_sdm.svg" title="Figure 1: Block diagram of the third-order \\(\Sigma\Delta\\) instrumentation loop that uses time-domain integrator for noise shaping and an extended phase detector for high-resolution phase digitisation." width="500" >}}

The system proposed here is shown in Fig. 1. This represents a third-order time domain ΔΣ  modulator that uses capacitive feedback to linearise the digitisation process similar to [^9]. The primary contributions here aim to make improvements in the overall dynamic range of time based ADCs that use oversampled noise shaping. The negative feedback mechanism uses the error signal appearing on V<sub>x<sub> to feed a cascade of oscillator-based integrators inside the continuous-time (CT) loop filter H(s) that accumulates quantisation errors. This is followed by a phase detector that digitises the phase difference of a pseudo-differential oscillator. The distinction is that the loop filter uses a feed-forward topology with better noise-shaping dynamics than prior-art together with an extended-phase-detector (EPD) that asynchronously accounts for phase overflow without incurring distortion. Both of these innovations result in higher dynamic range by performing higher-order quantisation noise-shaping and resolving the baseline phase state with a total precision of 9 bits.

This paper is organised as follows: Sec 3 will present the operating principle of oscillator-based ΔΣ  modulation which guides the design for the proposed circuit described in Sec 4. Sec 5 will then demonstrate operating characteristics followed by Sec 7 that concludes this work.

# 3 Oscillator Based \\(\Delta\Sigma\\) Conversion

The design procedure of an oscillator based loop filter follows closely to that of conventional Gm-C based CT modulators as the anti-aliasing properties are retained with similar concerns for paracitic pole locations. The difference is that the small-signal currents are integrated by modulating the phase of a current controlled oscillator (CCO) instead of the voltage on a capacitor. This results in better output dynamic range as the oscillator based integrator can be full swing while Gm-C integrators usually have limited voltage-swing for intermediate stages to avoid non-linear behaviour of the proceeding stage. The large signal swing can be tolerated by using a digital current DAC inside intermediate integration stages that exhibit better linearity with a full-swing input. Arguably Gm-C integrators will exhibit better noise performance than current DACs which is why the first stage of the oscillator-based loop filter also uses a transconductor in sub-threshold operation to maximise noise efficiency of the overall system.

$$  \phi (t) = \frac{f_{osc}}{I_{bias}} \int_{-\infty}^{t} i_{\Delta}(\tau) \: d\tau $$

As a basis for oscillator based circuits, Equation 1 formulates the small-signal phase response φ(t) of a CCO in terms of the oscillation frequency f<sub>osc<sub>, the static bias current I<sub>bias<sub>, and the small-signal current input i\tss{Δ}[^13]. This simply tells us that the total amount of charge injected over time is accumulated and scaled by an integration factor. It is interesting to note that φ\: is dimensionless and represents a unit of time relative to the oscillator period. The signal driving this circuit is typically a transconductor or a current-steering DAC while the output φ\: can be read using a phase detector. Realising the loop filter uses the coefficients from an optimised CT-ΔΣ  signal flow-graph for a 16 level quantiser and scales the transconductive elements according for a given set of oscillator frequencies.

While this integration property is well established, it is important to point out that the oscillator output is inherently discretised in the value domain in a non-linear fashion before it is clocked. This process generates distortion tones at harmonics of the oscillation frequency and can be interpreted in terms of a pulse-width-modulation process. Consolidating the impact of these out-of-band spurs does not have an established framework for analysis for more complex oscillator configurations and extensively relies on simulator based validation. Some progress has been made for analysing open loop configurations[^14] that use frequency readout. In a closed loop environment however the oscillator frequency is not stationary but instead modulated by the signal and quantisation errors which is in turn dithered by the oscillation. The main concern here is down conversion of tones into the signal band although they are actively suppressed during closed loop operation. Choosing co-prime frequency ratios through scaled bias currents such as 2:3:13 as is used here is best way to avoid undesirable oscillator interaction.

# 4 Circuit Implementation

The proposed instrumentation circuit can be split into three sub-circuits and will be detailed following the sequence by which the analogue input signal is processed. The first stage is the capacitive feedback structure shown in Fig. 2. This figure shows the input analogue signal being chopped and coupled though C<sub>IN<sub> while a capacitor array also feeds the chopped digital codes which will allow the flicker noise of the input-transconductor to be modulated out of the signal-band. The digitised output Q\tss{9-5} uses binary weighting while the PWM signals \\(\Phi\\)\tss{1-15} use unary weighting and together they evaluate the quantisation error. The PWM encoded signals \\(\Phi\\)\tss{1-15} are used to compute the remaining binary least-significant codes for Q\tss{4-1} seen at the ADC output. The unary weighting averages out any mismatch components and will also assist in performing foreground calibration of binary weighted DAC by correlating the output derivative code transitions in Q\tss{9-5}[^15].

{{< figure src="/images/iscas2019/td_cdac.svg" title="Figure 2: Capacitive feedback network that resolves the error signal when comparing the analogue input with the digitised output." width="500" >}}

The error signal on the capacitive DAC can be directly applied to the loop filter used here. This structure is shown in Fig. 3. The first stage of the feed-forward topology is a high-power transconductor that boosts the noise efficiency factor of this structure and dominates the overall noise performance as it directly drives the first and last differential oscillator through the current biasing terminal. All oscillating taps of X\tss{1-2} are buffered and processed by a XOR phase-detector to evaluate the phase-state. This controls the current-output from each DAC and enables us to cascade several time-based integrators without inducing quantisation errors or requiring strict digital timing requirements. It is important to point out that in this case the extended phase-detection is only applied to the last integrator and thus the limited dynamic range of X\tss{1-2} can result in undesirable modulator dynamics for high-frequency inputs. For this reason the second-order integration component is derived by feeding the first integration state forward instead of the input component. In addition the last oscillator presents a \\(4\times\\) smaller integration load thereby inducing additional gain at the output. This strategy is also found in conventional CT-\\(\Delta\Sigma\\) modulators as its allows the integration constants for the first two stages to be reduced giving more headroom for signal dynamics.

{{< figure src="/images/iscas2019/td_lf.svg" title="Figure 3: Configuration of the third-order modulator that uses a cascade of integrators with feed-forward compensation." width="500" >}}

Fig. 4 shows the circuit implementation of the EPD that similarly monitors each oscillating tap of X<sub>3<sub>. Clearly the phase difference is also being detected using an XOR gate however this circuit also generates overflow and underflow events as UP and DN signals. These are generated by combining a double-edge sensitive flip-flop with time-domain processing to perform level detection[^13]. The principle of operation here is that the Q<sub>5<sub> will always track whichever oscillator in the differential structure is leading. When the XOR gate indicates a change has occurred, a phase-overflow will be triggered when the AND level detector is high otherwise the NOR level detector triggers a phase-underflow. These events trigger a counter that will increment or decrement accordingly thereby also correcting Q<sub>5<sub> and setting the overflow event indicators low. In high-speed scenarios a unary counter can also be used to generate thermometer codes directly at the cost of added circuit complexity to speed up code transitions in the feedback DAC.

{{< figure src="/images/iscas2019/td_epd.svg" title="Figure 4: Schematic of the extended-phase read-out circuit that extracts both phase information and detects cycle over-flow for the N<sup>th<sup> section." width="500" >}}

Fig. 5 shows the internal EPD signals during closed loop operation to clarify the circuit behaviour. This also shows that several phase-overflow events can be generated as X<sub>3<sub> undergoes cycle slipping. Note that only the digital output is clocked and the internal counter state generates Q asynchronously in response to these events. Due to quantisation noise modulation multiple UP/DN events can be generated but this configuration processes the digital control in a feed-forward manner allowing tight timing control to guarantee a glitch free output. This is done by using a 2 ns window during every rising clock edge that holds the UP/DN signal in a tri-state to prevent latching invalid counter codes.

{{< figure src="/images/iscas2019/transition.svg" title="Figure 5: Transient waveform showing from top to bottom the pseudo differential oscillator output in volts, the phase-overflow trigger signal, and the two digital output codes \\(\Phi\\)1-15 & Q9-5." width="500" >}}

Table 1: Performance summary and comparison with state of the art
|		Specification       	| This Work | [^9] | [^8] | [^7] | [^16] | [^4] | [^17] | [^3] |
|----|----|----|----|----|----|----|----|----|
|		Year									| 2018						|  2018				| 2018 				| 2018 				| 2017 				| 2017 				| 2015 				|	2008 |
|		Tech.[nm] 			| 180 						|  65					| 130					| 65	 				| 40	 				| 130	 				| 180  				|	130	|
|		Supply[V]      	| 1.8/1.2    			|  0.5				| 1.8					| -						| 0.6 		 		| 1.2 				| 5/1.8 	 		|	1.2	|
|		Power[W]      	| 13.6μ  					|  1.28μ		| 0.56m				| 51.8m 			| 3.3μ			| 1.05m				| 140μ			|	40m	|
|		Phase/Freq.	 					| Φ-VCO 			|  Φ-VCO 	| F-VCO 		| Φ-VCO		| -						| Φ-VCO		| F-VCO		 	|	Φ-VCO	|
|		Calibration 					| Yes 						|  No					| No 					| Yes		 			| No		 			| No		 			| No					|	No	|
|		NS-Order 			 				| 3								|  1					| 2 					| 3						| 1		 				| 1		 				| 2						|	1	|
|		OSR 			 						| 64 							|  128    		| 500					| 15	 				| 83k					| 313	 				| 64k    			|	100	|
|		BW[Hz] 					| 15.6k  					|  11k  			| 20k					| 50M	 				| 150	 				| 0.4M 				| 1.25				|	10M	|
|		SNDR[dB]      	| 88		 					|  54					| 77					| 72	 				| 56					| 83	 				| 73 					|	72	|
|		Area[mm²] 	| 0.102						|  0.006			| 0.04				| 0.35				| 0.015				| 0.13 				| 0.36				|	0.01	|
|		FoM<sub>S<sub>[dB]  | 178(^\star) 		|  153				| 152					| 162	 				| 133	 				| 169	 				| 97					|	156	|

\\(^\star\\) Estimated based on simulation results where FoM<sub>S<sub> = SNDR + 10log<sub>10<sub>(BW/P).

# 5 Simulation Results

The time domain modulator presented here has been designed and validated using a commercially available 180 nm TSMC technology (1P6M HV BCD GEN II). The ADC core is configured to use a 1.8 V analogue supply to power the low noise transconductor as well as perform current biasing for each of the switched current DAC while using a 500 nA external reference current. The 1.8 V supply is also used as reference voltage when the digital codes are coupled onto V<sub>X<sub> using an array of level shifters since all the digital logic runs at 1.2 V to save power. A differential 2 kHz sinusoid at -3 dBFS (900 mVpp) is used during transient simulations to show preliminary performance characteristics. Fig. 6 shows one cycle where all three integrators are processing quantisation errors that are accumulated in X<sub>3<sub>. This also shows X<sub>3<sub> rapidly overflowing multiple times while triggering increments in the binary codes. At maximum input swing the speed is limited due to the slewing of X<sub>3<sub> but we do not expect such rapid signal dynamics for our application. Instead this extended dynamic range will capture drift and electrode offset components while the artefacts are typically 10 to 100 mV that the modulator can track at full-speed. The photo in Fig. 7 shows the floor plan as well as the layout of the fabricated prototype.

{{< figure src="/images/iscas2019/sim_tran.svg" title="Figure 6: Simulation result transient behaviour of the time based integration where each phase state is asynchronously PWM encoded but only the output X<sub>3<sub> uses extended phase detection to allow overflow." width="500" >}}

{{< figure src="/images/iscas2019/floor_plan.svg" title="Figure 7: Micro-photograph showing labelled blocks in relation to the schematics in Sec. 4." width="500" >}}

The spectral characteristics are summarised in Fig. 8. We can observe that third-order noise shaping can be achieved but some of the oscillator spurs are still present in high-frequency bands. However the components close to the signal band are significantly suppressed. The oscillator frequencies have also been annotated where X1 is around 78 kHz, X2 is around 117 kHz, and X3 is around 507 kHz. The chopper tones are still present outside the signal band since no off-set cancellation is performed which will be considered at a later point. The performance metrics are compared with other time based data converters in Table 1. While the figure of merit (FOM) seems to favour this work, the calibration mechanism is not yet integrated and measurements will need to confirm the these figures using a prototype that is currently in the process of being fabricated.

{{< figure src="/images/iscas2019/sim_thd.svg" title="Figure 8: Simulation result showing the noise-shaped output spectrum from a -3 dBFS  input sinusoid at 2 kHz." width="500" >}}

# 6 Acknowledgement

This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC) grants EP/M020975/1 & EP/R024642/1.

# 7 Conclusion

We have presented the implementation and operation of a third-order ΣΔ  ADC that uses an oscillator based loop filter with extended phase detection. As a result this work shows a significant improvement in precision over prior-art that strictly uses time-based signal processing. While the preliminary results show the performance for an analogue 180 nm CMOS technology, the digital operation of these circuits will enable these ideas to easily be adopted in a modern digital process or target high-speed applications. More importantly this work demonstrates that asynchronous time domain systems can be configured to achieve well over 80 dB dynamic range and realise intergrators that will not induce distortion due to saturation or phase-overflow.

# Refernces:

[^17]: P.Prabha etal., ''A highly digital VCO-based ADC architecture for  current sensing applications,'' IEEE J. Solid-State Circuits,  vol.50, no.8, pp. 1785--1795, Aug 2015. [Online]:  http://dx.doi.org/10.1109/JSSC.2015.2414428
[^7]: S.Dey, K.Reddy, K.Mayaram, and T.S. Fiez, ''A 50 MHz BW 76.1 dB  DR two-stage continuous-time delta-sigma modulator with VCO quantizer  nonlinearity cancellation,'' IEEE J. Solid-State Circuits, vol.53,  no.3, pp. 799--813, March 2018. [Online]:  http://dx.doi.org/10.1109/JSSC.2017.2777455
[^2]: R.Naiknaware, H.Tang, and T.S. Fiez, ''Time-referenced single-path multi-bit  $\Delta \Sigma$ ADC using a VCO-based quantizer,'' IEEE Trans.  Circuits Syst. II, vol.47, no.7, pp. 596--602, July 2000. [Online]:  http://dx.doi.org/10.1109/82.850418
[^3]: M.Z. Straayer and M.H. Perrott, ''A 12 bit, 10 MHz bandwidth,  continuous-time $\Sigma\Delta$ ADC with a 5 bit, 950 MS/s VCO-based  quantizer,'' IEEE J. Solid-State Circuits, vol.43, no.4, pp.  805--814, April 2008. [Online]:  http://dx.doi.org/10.1109/JSSC.2008.917500
[^16]: R.Mohan etal., ''A 0.6 V, 0.015 mm	sqrd, time-based ECG readout  for ambulatory applications in 40 nm CMOS,'' IEEE J. Solid-State  Circuits, vol.52, no.1, pp. 298--308, Jan 2017. [Online]:  http://dx.doi.org/10.1109/JSSC.2016.2615320
[^10]: S.Ziabakhsh, G.Gagnon, and G.W. Roberts, ''A time-mode LDI-based resonator  for a band-pass $\Delta\Sigma$ TDC,'' Aug 2017, pp. 1296--1299. [Online]:  http://dx.doi.org/10.1109/MWSCAS.2017.8053168
[^8]: F.Cardes etal., ''0.04 mm	sqrd  103 dB-A dynamic range  second-order VCO-based audio $\Sigma\Delta$ ADC in 0.13 $\mu$m  CMOS,'' IEEE J. Solid-State Circuits, vol.53, no.6, pp.  1731--1742, June 2018. [Online]:  http://dx.doi.org/10.1109/JSSC.2018.2799938
[^9]: L.B. Leene and T.G. Constandinou, ''A 0.006 mm	sqrd  1.2 $\mu$W  analog-to-time converter for asynchronous bio-sensors,'' IEEE J.  Solid-State Circuits, vol.53, no.9, pp. 2604--2613, Sept 2018. [Online]:  http://dx.doi.org/10.1109/JSSC.2018.2850918
[^1]: G.W. Roberts and M.Ali-Bakhshian, ''A brief introduction to time-to-digital  and digital-to-time converters,'' IEEE Trans. Circuits Syst. II,  vol.57, no.3, pp. 153--157, March 2010. [Online]:  http://dx.doi.org/10.1109/TCSII.2010.2043382
[^13]: L.B. Leene and T.G. Constandinou, ''Time domain processing techniques using  ring oscillator-based filter structures,'' IEEE Trans. Circuits Syst.  I, vol.64, no.12, pp. 3003--3012, Dec 2017. [Online]:  http://dx.doi.org/10.1109/TCSI.2017.2715885
[^14]: E.Gutierrez, L.Hernandez, F.Cardes, and P.Rombouts, ''A pulse frequency  modulation interpretation of VCOs enabling VCO-ADC architectures with  extended noise shaping,'' IEEE Trans. Circuits Syst. I, vol.65,  no.2, pp. 444--457, Feb 2018. [Online]:  http://dx.doi.org/10.1109/TCSI.2017.2737830
[^12]: J.Beaumont, A.Mokhov, D.Sokolov, and A.Yakovlev, ''High-level asynchronous  concepts at the interface between analog and digital worlds,'' IEEE  Trans. Comput.-Aided Design Integr. Circuits Syst., vol.37, no.1, pp.  61--74, Jan 2018. [Online]: http://dx.doi.org/10.1109/TCAD.2017.2748002
[^11]: B.Schell and Y.Tsividis, ''A continuous-time ADC/DSP/DAC system with no  clock and with activity-dependent power dissipation,'' IEEE J.  Solid-State Circuits, vol.43, no.11, pp. 2472--2481, Nov 2008. [Online]:  http://dx.doi.org/10.1109/JSSC.2008.2005456
[^15]: L.B. Leene and T.G. Constandinou, ''A 0.016 mm	sqrd12 b $\Delta \Sigma$  SAR with 14 fJ/conv. for ultra low power biosensor arrays,''  IEEE Trans. Circuits Syst. I, vol.64, no.10, pp. 2655--2665, Oct  2017. [Online]: http://dx.doi.org/10.1109/TCSI.2017.2703580
[^5]: W.Jiang etal., ''A ±50 mV linear-input-range VCO-based  neural-recording front-end with digital nonlinearity correction,''  IEEE J. Solid-State Circuits, vol.52, no.1, pp. 173--184, Jan  2017. [Online]: http://dx.doi.org/10.1109/JSSC.2016.2624989
[^4]: S.Li, A.Mukherjee, and N.Sun, ''A 174.3 dB FoM VCO-based CT  $\Delta \Sigma$ modulator with a fully-digital phase extended quantizer and  tri-level resistor DAC in 130 nm CMOS,'' IEEE J. Solid-State  Circuits, vol.52, no.7, pp. 1940--1952, July 2017. [Online]:  http://dx.doi.org/10.1109/JSSC.2017.2693244
[^6]: W.Yu, J.Kim, K.Kim, and S.Cho, ''A time-domain high-order MASH  $\Delta\Sigma$ adc using voltage-controlled gated-ring oscillator,''  IEEE Trans. Circuits Syst. I, vol.60, no.4, pp. 856--866, April  2013. [Online]: http://dx.doi.org/10.1109/TCSI.2012.2209298
