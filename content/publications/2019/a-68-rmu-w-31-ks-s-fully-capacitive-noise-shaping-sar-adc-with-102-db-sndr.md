---
title: "A 68 μW 31 kS/s fully-capacitive noise-shaping SAR ADC with 102 dB SNDR"
date: 2019-05-26T15:26:46+01:00
draft: false
toc: true
math: true
type: posts
tags:
  - publication
  - CMOS
  - data-converter
  - instrumentation
  - circuit
---

Lieuwe B. Leene, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

This paper presents a 17 bit analogue-to-digital converter that incorporates mismatch and quantisation noise-shaping techniques into an energy-saving 10 bit successive approximation quantiser to increase the dynamic range by another 42 dB. We propose a novel fully-capacitive topology which allows for high-speed asynchronous conversion together with a background calibration scheme to reduce the oversampling requirement by 10\\(\times\\) compared to prior-art. A 0.18μ m CMOS technology is used to demonstrate preliminary simulation results together with analytic measures that optimise parameter and topology selection. The proposed system is able to achieve a FoM<sub>S<sub> of 183 dB for a maximum signal bandwidth of 15.6 kHz while dissipating 68 μ W from a 1.8 V supply. A peak SNDR of 102 dB is demonstrated for this rate with a 0.201 mm² \:area requirement.

# 2 Introduction

Analogue-to-digital converter (ADC) efficiency remains to be the highlight for many current developments in both industry and academia. It used to be the case that oversampling converters (ΔΣ ADCs) and successive-approximation register converters (SAR ADCs) found separate application domains where this factor peaks. State-of-the-art ADCs however have mixed these two digitisation techniques to improve performance beyond a 170 dB Schreier Figure-of-Merit (FoM<sub>S<sub>)[^5][^4][^3][^1][^2]. This trend is in-part driven by the growing bio-metric and bio-medical electronics market that necessitates low-power high dynamic-range signal acquisition as many phenomena of interest exhibit signal dynamics with several orders of magnitude in variation. For example a peripheral neuro-modulation device with digitally assisted artifact rejection[^6] requires over \\(>\\)100 dB of dynamic range to detect micro-volt level sensory neuron activity in the presence of large mili-volt level interference from stimulation or motor-unit activity which is the application of interest that motivated this work.

The emerging ADC topologies for bio-sensors use multi-stage noise shaping or pipe-lined operation where multiple quantisers are integrated together and the quantisation error of the first quantiser is either resolved by another quantiser after amplification or may be used directly with an alternate feedback mechanism to similarly resolve additional bits. The noise-shaping SAR (NS-SAR) [^2][^7] however adopts a different approach by sampling and converting the input multiple times while simultaneously employing multiple feedback mechanisms that up-modulate any conversion errors out of the signal bandwidth. In this way the signal can be resolved with much finer precision once the output is decimated and the out-of-band frequency components are filtered out.

{{< figure src="/images/iscas2019/sar_sys.svg" title="Figure 1: Block diagram of the proposed high-resolution data converter showing the SAR digital controller applying feedback through 3 separate capacitor arrays and is augmented by the switched-capacitor loop filter H(z\tps{-1})." width="500" >}}

Here we present a novel fully-capacitive NS-SAR topology using active higher-order noise shaping that achieves state-of-the-art efficiency for high resolution signal acquisition. The proposed configuration is shown in Fig. 1. This figure summarises which signals are processed by each block in a closed-loop fashion to resolve the sampled analogue input signal V<sub>IN<sub>. The main data-conversion mechanism is based on the conventional SAR controller that uses the comparator decisions K to successively set the MSB and LSB bits[^8]. However to augment this operation two separate noise-shaping mechanisms are added; one for quantisation noise, H(z\tps{-1}), and another for mismatch noise by means of data-weighted averaging (DWA) together with mismatch-error shaping techniques (MES).

The NS-SAR approach is advantageous because the first several bits can be resolved rapidly using SAR and the remaining bits are resolved using ΔΣ modulation over several samples with reduced oversampling-ratio (OSR) to yield a significant overall improvement in conversion efficiency. Reusing the sampling mechanism of the SAR allows the quantisation residue left on V<sub>DAC<sub> to be directly integrated by the loop filter H(z\tps{-1}) that off-sets future conversions and shapes the quantisation noise as 1/(1+H(z\tps{-1})). The main drawback here in comparison to high-resolution \rDS\: modulators is that, while the conversion is faster, the mismatch in the high-resolution DAC must be carefully mitigated. This is where the DWA[^9] and MES[^10] are introduced to eliminate mismatch errors. DWA manipulates the selection of elements used within the MSB capacitive DAC such that the capacitor mismatch is not only decorrelated from the input but is also shaped with a (1-z\tps{-1}) characteristic. The MES module in the LSB section directly off-sets the sampled input using past conversion results to realise a FIR feedback structure such as (1-z\tps{-1}) or (1-2z\tps{-1}+z\tps{-2}) high-pass characteristics to minimise signal-band noise components.

The rest of this paper is organised as follows; Sec. 3 will relate the main design parameters to conversion precision in relation to primary noise sources. Once these are established the circuit implementation is presented in Sec. 4 together with simulation results in Sec. 5 and Sec. 7 will then conclude this work.

# 3 NS-SAR Design

Comparing with other data-converters, the NS-SAR topology is quite complex with a large number of design parameters that need to be optimised for efficient operation. Below, several of these parameters are discussed in relation to the ADC precision explaining the proposed configuration. Following the single-ended configuration shown in Fig. 1, we will estimate the expected sampling noise power (SNP), quantisation noise power (QNP), and mismatch noise power (MNP) for the signal bandwidth of fs/(2 OSR) where fs is the sampling speed. This formulation is purposely presented in brief since it based on established theory from [^11] but it does well to illustrate several trade-off considerations quantitatively when configuring this topology for a particular precision requirement.

$$  SNP \approx \frac{kT}{C_T} \cdot \frac{2.4}{OSR} $$

The expression in Eq. 1 should be a familiar representation for evaluating the input-referred sampling noise associated with a switched-capacitor integrator. In particular, this corresponds to the input being sampled with a total capacitive value of C<sub>T<sub> using kT as the Boltzman temperature factor. The second term simply arises from averaging the input over OSR cycles together with a correction factor of 2.4 due to the integrator topology in H(z\tps{-1})[^12]. Fig. 2 shows the estimated resolution for several capacitor values assuming we use an input sinusoid with maximum signal power (SP) given a 1.8 V ADC reference voltage as V<sub>DD<sub>. Inevitably, achieving high resolution implies a large sampling capacitance or a large oversampling ratio. Typically the former is preferred because increasing the capacitive load also decreases the mismatch power from the capacitive DACs.

$$  QNP \approx \underbrace{\left( V^2_{DD} e^{-3\tau} + \frac{V^2_{DD}}{2^{2N}} \right)}_{\text{SAR settling + quantisation }\epsilon} \cdot \frac{\pi^{2M}}{12   (1+2M) OSR^{1+2M}} $$

The expression in Eq. 2 parametrises the overall SAR resolution as N, the loop fillter order as M, and the number of time constants we allow the capacitive DAC to settle as τ \:in order to estimate QNP. This construction shows that settling and quantisation errors are shaped by the loop filter reducing the noise power by the term outside the brackets. Both in Fig. 3 and in the formulation we observe a strong dependency with regard to M as long as we provide sufficient settling time during SAR conversion. This result suggests that the noise-shaping feed-back must avoid driving the capacitive DAC with active amplifiers during successive-approximation to avoid slowing down the conversion speed or equivalently increasing the power requirement of each amplifier. We can also confirm here that the order of the loop filter does not need to be very high if the QNP needs to match the SNP.

$$  MNP \approx \underbrace{\left( \frac{\pi^2 2^{-2D}}{3 \cdot 2^K   OSR^3} + \frac{\pi^{2E} 2^{-2K}}{(1+2E) OSR^{1+2E}} \right)}_{\text{DWA-MSB + MES-LSB DAC}} \frac{\sigma^2   V^2_{DD}}{3} $$

The MNP is evaluated in Eq. 3 with respect to the MES noise shaping order E, the number of bits D used to calibrate each capacitor in the MSB DAC in an idealised way. K represents the MSB DAC resolution in bits. Using a capacitor standard deviation \\(\sigma=0.5%\\) and K=4, the MNP of several configurations is shown in Fig. 4. The observation here is that for small OSR values the mismatch noise is typically dominated by the MSB DAC as the mismatch is not sufficiently shaped. It is relatively expensive to increase the number of elements in the MSB DAC since the scaling is linear and increasing the OSR diminishes the advantage of performing SAR. Instead we propose to calibrate the 15 capacitors in the MSB section as D will reduce the MNP more efficiently. The mismatch from the LSB section contains many more elements and is more effectively shaped using a second-order MES technique.

The above trends are used to optimise the FOM<sub>S<sub> in a similar fashion to [^3] by correlating hardware requirements with power and accuracy estimators for several configurations. Given an initial 18 bit target precision, we propose the following configuration: CT=50 pF, M=2,τ=5, K=5, D=4, E=2 with the OSR set to 16 to ease the decimation effort.

{{< figure src="/images/iscas2019/osr_snp.svg" title="Figure 2: ADC precision as a function of oversampling ratio with respect to SNP while varying sampling capacitance C<sub>T<sub>." width="500" >}}

{{< figure src="/images/iscas2019/osr_qnp.svg" title="Figure 3: ADC precision as a function of oversampling ratio with respect to QNP while varying settling times \\(\tau\\) and noise-shaping order M." width="500" >}}

{{< figure src="/images/iscas2019/osr_mnp.svg" title="Figure 4: ADC precision as a function of oversampling ratio with respect to MNP while varying calibration D and mismatch-shaping order E." width="500" >}}

# 4 Circuit Implementation

The analogue part of the ADC implementation is shown in Fig. 5. Note that the implemented ADC uses an equivalent fully-differential configuration to gain extra input-dynamic range as well as digital noise suppression. This realisation is entirely based on manipulating the capacitive DAC and enables low-power operation for varying sampling rates. A second distinguishing feature of the proposed topology is that the comparator only requires one input terminal opposed to two seen in prior-art [^2][^7] which leads to better linearity and noise performance. In addition the input is bottom plate sampled such that sensitivity to parasitic capacitance and comparator non-linearity is considerably reduced. This figure also shows three capacitor arrays where the DAC<sub>M<sub> section corresponds to the DWA modulated MSBs and the DAC\tss{L1/L2} section represents the MES modulated LSBs being fed back from the SAR controller. Implementing the second-order MES noise-shaping uses the ping-pong configuration from [^13].

{{< figure src="/images/iscas2019/sar_cdac.svg" title="Figure 5: Implementation of the capacitor network used to perform signal conversion using the bottom sampled capacitor arrays DAC<sub>M<sub> for the DWA bits and DAC<sub>L1<sub> & DAC<sub>L2<sub> for the MES bits. The loop filter is also shown where A<sub>1<sub> amplifies the quantisation residue that is then integrated by A<sub>2<sub> & A<sub>3<sub> for noise-shaping." width="500" >}}

Three switched-capacitor amplifiers are used to realise a second-order cascaded-feed-forward-integrator (CFFI) loop filter topology where the first stage provides auto-zeroing as well as signal amplification by \\(C_T/C_1\approx30\\). This design uses an asynchronous SAR conversion process [^14] which is why there are only 3 phases in the switched capacitor circuit; the sampling phase (SMP), the successive approximation phase (SAR), and the quantisation filtering phase (QNF). The SAR only takes 100 ns and the FSM immediately initiates the QNF phase reducing the input clock to twice the sampling rate. The three phases operate as follows:

\begin{enumerate}
	\item[**SMP**] First A<sub>1<sub> actively samples its offset on the top plate while bottom plate samples V<sub>IN<sub> on DAC<sub>M<sub> together with the MES code on DAC\tss{L1/L2}. A\tss{2/3} are simultaneously integrating quantisation errors and sampling the result V\tss{X2/X3} with respect to V<sub>DAC<sub> on C<sub>6<sub> and C<sub>7<sub>.
	\item[**SAR**] V<sub>DAC<sub> then converges to virtual ground by switching the input to DAC\tss{M/L1/L2} while quantisation errors from prior conversions are removed by grounding the bottom plate of C\tss{6/7}. This also disconnects A\tss{1/2/3} from V<sub>DAC<sub>.
	\item[**QNF**] Finally DAC\tss{M/L1/L2} is held and the resulting quantisation residue left on V<sub>DAC<sub> is amplified by A{1} on V<sub>X1<sub>. C\tss{2/4} samples the voltages V\tss{X1/X2} which are used to integrate during the following SMP phase.
\end{enumerate}

This configuration scales well for varying loop filter structures as 80% of the power is dissipated by A<sub>1<sub> and the total sampling noise is dominated by C<sub>T<sub>. The comparator uses a conventional strong-arm topology that is carefully designed to minimise off-set since this off-set will be seen at the output of A<sub>3<sub> after amplification which can diminish the output-swing. Conversely the noise and distortion characteristics of the analogue filtering chain is proportionally reduced when the signal is fed back onto the capacitor array during sampling as the attenuation ratio \\(C_{6-7}/C_T\\) inverts the amplification ratio with good matching.

The MSB DAC calibration mechanism is uses a digital shuffling technique to identify mismatch by switching out different sets of capacitors that will only incur voltage fluctuation on V<sub>DAC<sub> in the presence of mismatch[^15]. These errors are then amplified by A<sub>1<sub> after the SAR & QNF process and digitally tunes each MSB capacitor using a capacitive sub-DAC. The sign of each shuffling result is accumulated to adjust the the 15 calibration codes thereby eliminating the mismatch in the MSB DAC. This process can be performed in the background without requirements on the input signal because DWA randomises the capacitor selection mechanism during shuffling.

Table 1: Performance summary and comparison with state of the art
|		Spec.       	| This Work | [^16] | [^15] | [^4] | [^5] | [^3] | [^7] | [^2] |
|----|----|----|----|----|----|----|----|----|
|		Year									| 2018						|  2018				| 2018 				| 2018 				| 2018 				| 2017 				| 2016 				|	2012 |
|		Tech.[nm] 			| 180 						|  180				| 180					| 28	 				| 40	 				| 180	 				| 55  				|	65	|
|		Supply[V]      	| 1.8    					|  1.8				| 1.8/5				| 1.1/1.2			| 2.5/1.1	 		| 1.2 				| 1.2  				|	1.2	|
|		Power[W]      	| 68μ  				|  7.93μ		| 12.9m				| 4.2m 				| 140μ			| 5.16μ		| 15.7μ		|	806μ	|
|		Topology 		 					| NS-SAR 					| \rDS-SAR		| SAR 				| CT-\rDS			| \rDS-SAR		| \rDS-SAR		| NS-SAR			|	NS-SAR	|
|		DAC Res.[b] 		| 10 							|  9 					| 20 					| 4		 				| 7		 				| 8		 				| 12					|	8	|
|		NS-Order 			 				| 2(^\dagger)			|  1					| 0 					| 2(^\dagger)	| 3		 				| 2		 				| 1(^\dagger)	|	1(^\dagger)	|
|		OSR 			 						| 16 							|  256    		| 1 					| 16	 				| 12	 				| 24	 				| 256    			|	4	|
|		BW[Hz] 					| 15.6k  					|  1k  				| 500k				| 10M	 				| 40k	 				| 100k 				| 4k					|	11M	|
|		SNDR[dB]      	| 102		 					|  85					| 102					| 94	 				| 84					| 67	 				| 96.1 				|	62	|
|		Area[mm²] 	| 0.201						|  0.68				| 4 					| 0.1	 				| 0.07 				| 0.02 				| 0.07				|	0.03	|
|		FoM<sub>S<sub>[dB]  | 183(^\star) 		|  166				| 176					| 168	 				| 169	 				| 170	 				| 180					|	164	|

\\(^\star\\) Estimated based on post-layout simulation results where FoM<sub>S<sub> = SNDR + 10log<sub>10<sub>(BW/P). \\(^\dagger\\) FIR & digital noise-coupling poles excluded.

# 5 Simulation Results

The proposed NS-SAR has been designed and validated using a commercially available 180 nm TSMC technology (1P6M HV BCD GEN II). All sub-circuits have been integrated with reconfigurable ΔΣ, DWA, MES, and calibration modes to fully characterise post-silicon performance that will confirm the evaluation in Sec. 3. This circuit uses an analogue and digital supply at 1.8 V, a 1 μ A current reference to bias A\tss{1-3}, and a 0.9 V common-mode reference for V<sub>CM<sub>-based capacitor switching. Preliminary post-layout simulation results are shown in Fig. 6. This demonstrates the ADC can resolve 17 bits of precision without distortion while using an external clock of 1 MHz where one cycle is used to sample the input and one cycle is used for conversion plus quantisation noise shaping and another cycle is optionally used for background calibration. The last phase can be skipped if the MSB capacitors are already tuned to speed-up signal conversion to 31.25 kS/s since temperature and voltage variations over time during normal operation will typically not corrupt the calibrated capacitor characteristics.

{{< figure src="/images/iscas2019/sar_sim_thd.svg" title="Figure 6: Post-layout simulation result showing the noise-shaped output spectrum from a -3 dBFS  input sinusoid at 6.5 kHz." width="500" >}}

{{< figure src="/images/iscas2019/sar_floor_plan.svg" title="Figure 7: ADC micro-photograph showing labelled blocks in relation to Fig 1 where the MES and DWA circuitry is included in the main digital core. Decoupling capacitors are placed over active circuitry or underneath active mim-caps." width="500" >}}

The layout for this ADC is shown in Fig. 7. A large majority of silicon area is dedicated towards the MSB capacitive array as the sampling noise must be suppressed. The switched capacitor integrator can be relatively small because the internal loop-filter gain reduces its sampling noise. The digital core takes up a considerable amount of area and power budget primarily as a result of using a 180 nm CMOS technology where more advanced technologies may lead to further improvements if the 1.8 V rating can be maintained. Each MSB capacitor is trimmed using a 8 bit sub-DAC that tunes about 5% of the 1.7 pF unit capacitance which accommodates well over 3σ of the expected capacitor mismatch as well as wafer level variations that may not be captured by the typical mismatch model. The performance measures for the proposed ADC are shown in Table 1. Again we highlight the fact that while all these works have highly optimised power budgets, this topology is able to achieve over 100 dB SNDR with a 10\\(\times\\) lower oversampling ratio than prior art for this level precision. While this does imply a marginally increased area requirement, the peak efficiency can be achieved over a greater span of sampling frequencies. Note that this particular TSMC process kit does not allow post-layout Monte-Carlo so the calibration will be validated using post-silicon results.

# 6 Acknowledgement

This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC) grants EP/M020975/1 & EP/R024642/1.

# 7 Conclusion

This works presents a 17 bit Noise Shaping SAR ADC with reduced oversampling ratio and a purely capacitive implementation which enables in state-of-the-art conversion efficiency over a large range of sampling frequencies. In comparison with conventional over-sampling ADCs simulation results suggest this NS-SAR is able to achieve 102 dB SNDR with substantially lower noise-shaping requirements with comparable or reduced circuit complexity while achieving better power efficiency. We also demonstrated a high-level parameter selection methodology that is used to optimise the FoM<sub>S<sub> and identify the factors limiting ADC precision.

# Refernces:

[^11]: S.Pavan, R.Schreier, and G.C. Temes, Understanding Delta-Sigma Data  Converters.\hskip 1em plus 0.5em minus 0.4emelax IEEE, 2017. [Online]:  http://dx.doi.org/10.1002/9781119258308
[^12]: R.Schreier, J.Silva, J.Steensgaard, and G.C. Temes, ''Design-oriented  estimation of thermal noise in switched-capacitor circuits,'' IEEE  Trans. Circuits Syst. I, vol.52, no.11, pp. 2358--2368, Nov 2005.  [Online]: http://dx.doi.org/10.1109/TCSI.2005.853909
[^10]: M.Aboudina and B.Razavi, ''A new DAC mismatch shaping technique for  sigma–delta modulators,'' IEEE Trans. Circuits Syst. II,  vol.57, no.12, pp. 966--970, Dec 2010. [Online]:  http://dx.doi.org/10.1109/TCSII.2010.2083172
[^13]: J.Liu, G.Wen, and N.Sun, ''Second-order DAC MES for SAR ADCs,''  IET Elec. Letters, vol.53, no.24, pp. 1570--1572, 2017. [Online]:  http://dx.doi.org/10.1049/el.2017.3138
[^9]: B.H. Leung and S.Sutarja, ''Multibit sigma - delta A/D converter  incorporating a novel class of dynamic element matching techniques,''  IEEE Trans. Circuits Syst. II, vol.39, no.1, pp. 35--51, Jan  1992. [Online]: http://dx.doi.org/10.1109/82.204108
[^8]: B.P. Ginsburg and A.P. Chandrakasan, ''500 MS/s 5 bit ADC in 65 nm  CMOS with split capacitor array DAC,'' IEEE J. Solid-State  Circuits, vol.42, no.4, pp. 739--747, April 2007. [Online]:  http://dx.doi.org/10.1109/JSSC.2007.892169
[^5]: A.AlMarashli, J.Anders, J.Becker, and M.Ortmanns, ''A nyquist rate SAR  ADC employing incremental sigma delta DAC achieving peak SFDR=107 dB  at 80 kS/s,'' IEEE J. Solid-State Circuits, vol.53, no.5, pp.  1493--1507, May 2018. [Online]:  http://dx.doi.org/10.1109/JSSC.2017.2776299
[^4]: I.Jang etal., ''A 4.2 mW 10 MHz BW 74.4 dB SNDR  continuous-time delta-sigma modulator with SAR-assisted digital-domain  noise coupling,'' IEEE J. Solid-State Circuits, vol.53, no.4, pp.  1139--1148, April 2018. [Online]:  http://dx.doi.org/10.1109/JSSC.2017.2778284
[^3]: L.B. Leene and T.G. Constandinou, ''A 0.016 mm	sqrd 12 b $\Delta\Sigma$  SAR with 14 fJ/conv. for ultra low power biosensor arrays,''  IEEE Trans. Circuits Syst. I, vol.64, no.10, pp. 2655--2665, Oct  2017. [Online]: http://dx.doi.org/10.1109/TCSI.2017.2703580
[^1]: Y.Chae, K.Souri, and K.A.A. Makinwa, ''A 6.3mu W 20 bit incremental  zoom-ADC with 6 ppm INL and 1 mu V offset,'' IEEE J.  Solid-State Circuits, vol.48, no.12, pp. 3019--3027, Dec 2013. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2278737
[^16]: S.Choi etal., ''An 84.6 dB-SNDR and 98.2 dB-SFDR  residue-integrated SAR ADC for low-power sensor applications,''  IEEE J. Solid-State Circuits, vol.53, no.2, pp. 404--417, Feb  2018. [Online]: http://dx.doi.org/10.1109/JSSC.2017.2774287
[^2]: Y.Shu, L.Kuo, and T.Lo, ''An oversampling SAR ADC with DAC mismatch  error shaping achieving 105 dB SFDR and 101 dB SNDR over 1 kHz  BW in 55 nm CMOS,'' IEEE J. Solid-State Circuits, vol.51,  no.12, pp. 2928--2940, Dec 2016. [Online]:  http://dx.doi.org/10.1109/JSSC.2016.2592623
[^7]: J.A. Fredenburg and M.P. Flynn, ''A 90 MS/s 11 MHz bandwidth 62 dB  SNDR noise-shaping SAR ADC,'' IEEE J. Solid-State Circuits,  vol.47, no.12, pp. 2898--2904, Dec 2012. [Online]:  http://dx.doi.org/10.1109/JSSC.2012.2217874
[^6]: A.E. Mendrela etal., ''A bidirectional neural interface circuit with  active stimulation artifact cancellation and cross-channel common-mode noise  suppression,'' IEEE J. Solid-State Circuits, vol.51, no.4, pp.  955--965, April 2016. [Online]:  http://dx.doi.org/10.1109/JSSC.2015.2506651
[^15]: H.Li etal., ''A signal-independent background-calibrating 20 b  1 MS/S SAR ADC with 0.3ppm INL,'' in IEEE Proc. ISSCC, Feb 2018,  pp. 242--244. [Online]: http://dx.doi.org/10.1109/ISSCC.2018.8310274
[^14]: R.Sekimoto etal., ''A 0.5 V 5.2 fJ/conversion-step full  asynchronous SAR ADC with leakage power reduction down to 650 pW by  boosted self-power gating in 40 nm CMOS,'' IEEE J. Solid-State  Circuits, vol.48, no.11, pp. 2628--2636, Nov 2013. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2274851
