---
title: "A 0.45 V continuous time-domain filter using asynchronous oscillator structures"
date: 2016-12-11T15:26:46+01:00
draft: false
toc: true
type: posts
math: true
tags:
  - publication
  - instrumentation
  - CMOS
  - time-domain
  - asynchronous
---

Lieuwe B. Leene, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

This paper presents a novel oscillator based filter structure for processing time-domain signals with linear dynamics that extensively uses digital logic by construction. Such a mixed signal topology is a key component for allowing efficient processing of asynchronous time encoded signals that does not necessitate external clocking. A miniaturized primitive is introduced as analogue time-domain memory that can be modelled, synthesized, and incorporated in closed loop mixed signal accelerators to realize more complex linear or non-linear computational systems. This is contextualized by demonstrating a compact low power filter operating at 0.45 V in 65 nm CMOS. Simulation results are presented showing an excess of 50 dB dynamic range with a FOM of 7 fJ/pole which promises an order of magnitude improvement on state-of-the-art filters in nanometre CMOS.

# 2 Introduction

The challenges for advancing digital devices and energy constrained computation no longer exhibit the coherent virtues dictated by Moore's Law[^1]. Instead current research is driven to find new solutions inspired by the natural world for solving problems that are dissonant with today's computational paradigm. This has led to the re-emergence of processing in the analogue domain as accelerator to the digital framework [^2]. Motivated by the fact that when tailored to a specific computational problem analogue efficiency can be vastly superior to its digital equivalent [^3][^4]. However there remain many challenges that prevent a clear advantage for such architectures in practice. Current state-of-the-art demands fully integrated SOCs in nanometre CMOS for a cost effective solution. This substantially degrades analogue performance in addition to the difficulty in miniaturizing analogue elements. More importantly analogue tends to drastically lose fidelity for near threshold supply voltages which is an essential aspect to ultra low power digital systems [^5]. To address such challenges oscillator based topologies have been proposed in association with a new computational paradigm [^6][^7]. There are two critical advantages that such an approach can leverage. The first is that the signals pertaining to these systems are digital in nature where the information is encoded with respect to the timing between logical events equivalent to clock edges. This implies that a single binary bit stream can represent multiple bits of information artificially increasing the density of CMOS interconnect. Moreover such signals allow them selves to be manipulated by standard logic gates and asynchronous digital controllers for very rich yet highly efficient signal control[^8]. The second aspect is that voltage controlled oscillators suffer very little performance degradation from aggressive technology scaling or poor transistor characteristics. In fact the perpetual improvement f<sub>T<sub> increases the maximum temporal resolution achievable using time-domain quantizers for unparalleled dynamic range.

{{< figure src="/images/icecs2016/td_system.svg" title="Figure 1: Oscillator based computing to realize linear and non-linear dynamics that utilize a phase domain state as memory." width="500" >}}

In an effort to explore the potential of such a modality this work considers the use of oscillator structures for processing neural activity in extension to a previously developed oscillator based instrumentation system in [^9]. As implantable brain machine interfaces present one of the most demanding applications for realizing power efficient structures that acquire and classify neural activity to treat neurophysiological disorders. The ring oscillator concept shown in Fig. 1. This oscillator plays the role of analogue memory by retaining a state in the phase domain. A transconductive element adjusts the phase subject to the digital control signals. The digital logic dictates the overall response of the structure by using single or multiple phases of the oscillator. This presents negative feedback that stabilizes the operation of the system by rejecting frequency off-sets and noisy aggressors external to the circuit. As will be demonstrated this closed loop dynamic has true analogue aliasing properties due to the nature of VCO based integration. This implies that any logical approximations that induce errors or distortion at high frequency can be rejected. This paper is organized as follows. The basic aspects of the filter architecture is introduced in Sec. 3. This is followed by the circuit level implementation that is detailed in Sec. 4. Sec. 5 presents preliminary simulation results which are concluded upon in Sec. 7.

# 3 Ring Oscillator based Filter

{{< figure src="/images/icecs2016/TD_L1.svg" width="500" >}}

{{< figure src="/images/icecs2016/TD_L1.svg" title="Figure 2: Proposed Single pole ROF structure where V<sub>R<sub> represents the only analogue node in the system. " width="500" >}}

A first order realization of this Ring Oscillator based Filter (ROF) is presented in Fig. 2. This simpler structure will allow the discussion to give insight the elementary operation. Here the digital signals D and Q are pulse width modulated (PWM) encoded time domain signals and are typically not modulated using the same carrier frequency. In essence a digital adder injects current into the oscillator such that the phase recedes or advances with respect another local oscillator by comparing the two pulse width components of D & Q. By using a differential structure the phase can be encoded as self referenced timing events that do not require global frequency synchronization to decode phase information. It is also important to note this structure differs characteristically from classic literature examples [^10] but remain very useful for analysis. This discrepancy arises from sub-threshold and current starved operation of the oscillator which implies that the conduction phases of the NMOS and PMOS transistors for each inverter are non-overlapping. In a general sense however the output voltage V<sub>out<sub> of the structure is often modelled as:

$$  V_{out} (t) = A(t) \cdot f\left[   \omega_0   t + \phi(t)   \right] $$

$$  \phi (t) = \int_{-\infty}^{\infty} h_{\phi}(t,\tau)   i(\tau) \: d\tau = \int_{-\infty}^{t} \Gamma(\omega_0 , \tau)   i(\tau) \: d\tau $$

In Eq. 1 A and \pphi represent the amplitude and phase state variables of the system as a function of time. \\(f\\) describes the limit cycle of the oscillation that captures the non-linearities of V<sub>out<sub> as a function of phase. Our primary interest lies with Eq. 2 which captures the dependency of phase with respect to the impulse response h<sub>\pphi<sub> and the cyclo stationary impulse sensitivity function (ISF) \gGamma. \gGamma is evaluated with respect to a specific small signal source. This dependency is what gives rise to the inherent integral behaviour of oscillators where parasitics diminish the integration constant but will not effect the ideal loop gain of the circuit. The transconductance Gm is introduced to translate the digital output to currents injected into the oscillator represented by I<sub>\dDelta<sub>. The resulting behaviour can be summarized in the s-domain by assuming \gGamma <sub>Gm<sub> is approximately independent of the phase[^11]:

$$  H_{\phi}(s)=\frac{1}{s} \frac{Gm}{2\pi   q_{max}}  \text{where}  q_{max} = N   V_R   C_{T}  $$

$$  V_R = V_{th} + \eta U_T   \ln \left( \frac{2 I_B}{2\eta   U_T^2  \mu  C_{ox}}   \frac{L}{W}  \right) $$

In Eq. 3 N, V<sub>R<sub>, and C<sub>T<sub> represent the number of inverter stages, voltage across the oscillator, and total capacitance seen as load to each gate in the oscillator. Note q<sub>max<sub> physically represents the total charge that is dissipated each period which implies a frequency of oscillation in terms of f<sub>osc<sub>=I<sub>B<sub>/q<sub>max<sub>. For simplicity the carrier mobility \mmu and V<sub>th<sub> for both PMOS and NMOS are taken as equivalent such that their conductivity is equal. In practice W must be adjusted to compensate this difference but will typically lead to improved supply noise rejection. Fig. 3 shows the phase dependency of \gGamma with respect to I<sub>B<sub> and constituent NMOS & PMOS devices of all gates together for a 5 stage ring oscillator. Although H<sub>\pphi<sub>  due to I<sub>B<sub> exhibits some dependency with respect to phase it is well estimated by Eq. 3. The phase information is extracted using an XOR gate which has a gain of 1/\ppi.

{{< figure src="/images/icecs2016/ISF.svg" title="Figure 3: Impulse sensitivity function for a 5-stage ring oscillator with respect to the bias current and NMOS/PMOS contributions from all stages together. " width="500" >}}

Although the first order structure has very low complexity the drawback is that the bandwidth is directly related to the the frequency of oscillation when H<sub>\pphi<sub> is put into feedback. This coupling is undesirable for two reasons. The first is from a noise perspective which is that for a fixed frequency decreasing I<sub>\dDelta<sub> increases the input-referred noise power (e²<sub>n<sub>) of this circuit approximately as (U<sub>T<sub>\\(\cdot\\)I<sub>B<sub>/I<sub>\dDelta<sub>)² which may become very pronounced. This forces the structure to dissipate excessive amounts of power to maintain adequate dynamic range. The second aspect is that the capability to control the oscillator frequency independent of loop bandwidth is useful to adjusting digital power dissipation and its interaction with other system blocks.

{{< figure src="/images/icecs2016/TD_L2.svg" title="Figure 4: Proposed two-pole ROF structure with the digital output Q represented by K PWM phases for reduced analogue distortion." width="500" >}}

For this reason the second order structure is introduced in Fig. 4. This has equivalent characteristics to that of a miller compensated amplifier where the switched current loads into a capacitor across a high gain stage which is realized by the first order structure. As a result noise/bandwidth and oscillator characteristics are decoupled by being represented through two different capacitors C<sub>L<sub> and C<sub>T<sub>. The additional consideration required here is that the digital feedback Q over C<sub>L<sub> can cause large signal swings on the gate of M<sub>B<sub> degrading transconductive linearity. Generally if M<sub>B<sub> is also in sub threshold operation its input range is limited to 2U<sub>T<sub> before excessive distortion is introduced. However capacitively coupling M phases of Q in parallel the quantization levels are reduced to V<sub>DD<sub>/M. Each phase is simply represented by taking more taps from the ring oscillator in parallel. Moreover if M is chosen proportional to V<sub>DD<sub>/2U<sub>T<sub> this structure actually reduces in complexity and improves efficiency as the supply voltage decreases. Note that for high frequency operation the switched current DAC exhibit poor switching dynamics due to the reduced supply voltage. In such a case it is sufficient to replace this block with parallel resistors equivalent to active RC integrators. As such it may be expected that this configuration implies the 3dB frequency equivalent to f<sub>3dB<sub>=I<sub>\dDelta<sub>/C<sub>L<sub> where C<sub>L<sub> is approximated as U<sub>T<sub> kT/e²<sub>n<sub> to match the required noise levels. In extension the oscillator spurs can be set to match this noise floor by considering the filter response and quantizer level dependency such that f<sub>osc<sub>\textgreater f<sub>3dB<sub> SNR/N for a first order system.

# 4 Circuit Implementation

The presented implementation realizes a 0.45 V second order ROF using commercially available TSMC \cmostech LP MS RF technology (1P9M\_6X1Z1U\_RDL). Fig. 5 shows transistor level implementation of the transconductor and oscillator structure that retains the phase state of the system. Here a bias current is simply switched differentially into the capacitive load while M\tss{1-2} provide common mode feedback. The transistors M\tss{3-4} realize a current mirror that biases the ring oscillators proportionally to I<sub>B<sub>. The control switches S<sub>A<sub>/S<sub>C<sub>/S<sub>B<sub> correspond to +1/0/-1 transconductive gains that realize a 1.5 bit current DAC. The oscillators are floating in the middle the supplies due to M<sub>5<sub> which has its body connected to source. This improves the switching behaviour of the proceeding XOR gate by providing good high/low voltage levels while also reducing the noise coupling from ground/substrate if the oscillator is allowed to use isolated P/N-wells. The capacitor C<sub>L<sub> is split into 11 MIM fringe capacitors for a total of 100 fF load on each terminal.

{{< figure src="/images/icecs2016/TD_sch1.svg" width="500" >}}
{{< figure src="/images/icecs2016/TD_sch2.svg" title="Figure 5: The proposed transistor level implementation of the second order ROF" width="500" >}}

The digital logic used to realize unity gain feedback is presented in Fig. 6. Three out of the 11 phases are used in the feedback logic for demonstration. Typically this number of phases is directly related to the frequencies of D & Q or their intermodulation products that will introduce spurs outside of the filter bandwidth. Increasing the number of phases used reduces distortion components while increasing the effective carrier frequencies. This can and should be reconfigurable in addition to tuning I<sub>B<sub> to accommodate the typical process variance for transistor characteristics. While other types of phase detectors beside the XOR gate can be used it is important to realize its impact on distortion due to the finite bandwidth of digital gates. The XOR realization grantees that for near zero input Q will exhibit the smallest bandwidth requirement due to its 50 % duty cycle which gradually increases as the phase difference approaches 0 or \ppi.

{{< figure src="/images/icecs2016/TD_logic.svg" title="Figure 6:  Boolean operator used that allows a unity gain configuration of the ROF." width="500" >}}

# 5 Simulation Results

In practice the primary difficulty with time domain structures is their associated simulation effort because the bandwidth of operation is many orders larger than the signals of interest. For this reason the analytic model is also presented to perform behavioural simulations and guide the design effort. The results presented here are based on transient noise simulations using industry provided PSP models for completeness. Fig. 7 shows these simulation results where a 1 kHz PWM encoded input signal is driving the system at 95 % of the full input range. V<sub>R<sub> shows the oscillator providing capacitive feedback on the miller integration node while the phase difference of the two ring oscillators tracks the pulse width of the input. Fig. 9 presents the frequency content when three of the phases are summed together and Fig. 8 shows the oscillator phase difference as a function of time. The 56 dB THD shown is critically related to the current DAC characteristics near the cut-off frequency as it not adequately shaped by the integration loop which is challenging to enhance with limited voltage overhead. Table 1 compares the performance presented here using a figure of merit defined where SINAD<sub>MAX<sub> is the maximum signal to noise and distortion ratio as: FOM = Power/(N<sub>poles<sub> BW SINAD<sub>MAX<sub>).

{{< figure src="/images/icecs2016/visual.svg" title="Figure 7: Digital input (D) & output (Q) components together with the integration node V<sub>R<sub>  and oscillator outputs internal to the system. " width="500" >}}

{{< figure src="/images/icecs2016/Delta.svg" title="Figure 8: Phase difference of the oscillator structure measured as time delay." width="500" >}}

{{< figure src="/images/icecs2016/Spectrum.svg" title="Figure 9: Spectral power densities of the multi-phase PWM signal Q" width="500" >}}

Table 1: Performance summary and comparison with state of the art
|		Specification       | This Work | [^6] | [^12] | [^13] |
|----|----|----|----|----|
|		modality 		 | Time 			| Time 		| Volt. 	| Volt.   	|
|		Order 			 | 1 				|  4    	| 3     	| 3 		|
|		Technology       | 65nm   			| 90nm  	| 0.5\mmu   | 0.5\mmu 	|
|		Supply [V]       | 0.45    			| 0.55 		| 3.3  		| 1.8 		|
|		Supply [A]       | 35n  			|  5.3m 	| 1.4m 		| 2m		|
|		Bandwidth [Hz]   | 6k  				|  7M  		| 1.5M 		| 500k 		|
|		SINAD [dB]       | 52 				|  61  		| 60  		| 65 		|
|		FoM [fJ]         | 7.4 		|  93   	| 1026		| 1350 		|
|		Area [mm²]	 | 0.001			|  0.29    	| 2.2  		| 0.68 		|

# 6 Acknowledgement

This work was supported by EPSRC grants EP/K015060/1 and EP/M020975/1.

# 7 Conclusion

The model and implementation of a oscillator based filter has been demonstrated to complement that of FIR structures [^14] for asynchronous time domain structures. High linearity is demonstrated at full input dynamic range while operating with a 0.45 V supply voltage. The extensive use of digital logic in its construction allows highly synthesizable oscillator based computing for future ultra low power systems in nanometre CMOS. Preliminary simulation result indicates a FOM of 7.4 fJ/pole for the 6 kHz bandwidth which is a substantial improvement over previous time-domain implementations. While it remains to be seen if the efficiency can be maintained in more complex systems the proposed topology shows much promise for ultra low power systems. Moreover we expect that both the first & second order primitives proposed here will find many other applications like \\(\Delta\Sigma\\) ADCs due to its simplicity and flexibility towards process parameters for low voltage operation.

# Refernces:

[^1]: I.L. Markov, ''Limits on fundamental limits to computation,'' Nature,  vol. 512, pp. 147--154, August 2014.
[^2]: N.Guo etal., ''Energy-efficient hybrid analog/digital approximate  computation in continuous time,'' IEEE J. Solid-State Circuits,  vol.51, no.7, pp. 1514--1524, July 2016.
[^3]: M.Verhelst and A.Bahai, ''Where analog meets digital: Analog-to-information  conversion and beyond,'' IEEE Solid-State Circuits Mag., vol.7,  no.3, pp. 67--80, September 2015.
[^4]: R.Sarpeshkar, ''Analog versus digital: Extrapolating from electronics to  neurobiology,'' Neural Computation, vol.10, no.7, pp. 1601--1638,  Oct 1998.
[^5]: M.Alioto, ''Understanding dc behavior of subthreshold cmos logic through  closed-form analysis,'' IEEE Trans. Circuits Syst. I, vol.57,  no.7, pp. 1597--1607, July 2010.
[^6]: B.Drost, M.Talegaonkar, and P.K. Hanumolu, ''Analog filter design using ring  oscillator integrators,'' IEEE J. Solid-State Circuits, vol.47,  no.12, pp. 3120--3129, December 2012.
[^7]: W.Y. Tsai etal., ''Enabling new computation paradigms with hyperfet -  an emerging device,'' IEEE Trans. Multi-Scale Comput. Syst., vol.2,  no.1, pp. 30--48, Jan 2016.
[^8]: T.S. Lande etal., ''Running cross-correlation using bitstream  processing,'' Electronics Letters, vol.43, no.22, Oct 2007.
[^9]: M.Elia, L.B. Leene, and T.G. Constandinou, ''Continuous-time micropower  interface for neural recording applications,'' in IEEE Proc. ISCAS,  May 2016.
[^10]: A.Hajimiri and T.Lee, ''A general theory of phase noise in electrical  oscillators,'' IEEE J. Solid-State Circuits, vol.33, no.2, pp.  179--194, February 1998.
[^11]: A.Hajimiri, S.Limotyrakis, and T.Lee, ''Phase noise in multi-gigahertz cmos  ring oscillators,'' in IEEE Proc. CICC, May 1998, pp. 49--52.
[^12]: C.Garcia-Alberdi etal., ''Tunable class ab cmos gm-c filter based on  quasi-floating gate techniques,'' IEEE Trans. Circuits Syst. I,  vol.60, no.5, pp. 1300--1309, May 2013.
[^13]: J.Galan etal., ''A very linear low-pass filter with automatic  frequency tuning,'' IEEE Trans. VLSI Syst., vol.21, no.1, pp.  182--187, Jan 2013.
[^14]: M.Kurchuk etal., ''Event-driven ghz-range continuous-time digital  signal processor with activity-dependent power dissipation,'' IEEE J.  Solid-State Circuits, vol.47, no.9, pp. 2164--2173, September 2012.
