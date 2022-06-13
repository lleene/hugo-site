---
title: "An adaptive 16/64 kHz, 9-bit SAR ADC with peak-aligned sampling for neural spike recording"
date: 2014-06-01T15:26:46+01:00
draft: false
toc: true
math: true
type: posts
tags:
  - publication
  - instrumentation
  - CMOS
  - biomedical
  - sampling
---

Lirong Zheng, Lieuwe B. Leene, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

This paper presents a novel method and circuit for feature-driven data acquisition in single neuron recording. By dynamically adjusting the phase of the sampling clock in a Successive Approximation Register (SAR) Analogue to Digital Converter (ADC), the samples can be maximally aligned to the spike extrema (peaks). This is achieved by using spike detection to switch from a 'coarse' to 'fine' sampling clock, and triggering a peak-search algorithm to determine the offset between the peak occurrence and the coarse clock. Subsequent samples are then aligned to the peak by shifting the coarse clock by the measured offset. This adaptive sampling scheme thus allows for improved temporal precision on features of interest (i.e. peaks) whilst maintaining a coarse effective sampling rate, also minimising power consumption. The proposed method reduces the output data bandwidth by approximately 70% in comparison to a fixed-sampling rate data converter that would achieve similar precision in peak alignment. The circuit implementation achieves 9-bit resolution with a 93 fJ/conversion-step energy efficiency in a standard 0.35\\( \mu\\)m CMOS technology.

# 2 Introduction

In the quest towards understanding the human brain, neuroscientists are now using 'new' research tools to record single neuron activity in-vivo. Neural probes consisting of micro-fabricated multi-electrode arrays (MEAs) together with supporting recording electronics are providing the opportunity to observe the extracellular activity of an increasing number of neurons in real-time [^1]. To this end, the Neural Engineering and BioCAS communities have made significant progress in the past decade, developing countless integrated, multi-channel neural recording interfaces, Eg. \cite{harrison2007low, bonfanti2010multi, gao2012hermese}. These amplify, filter and digitise the Extracellular Action Potentials (EAPs) with hardware specifications carefully selected so as to maintain signal integrity for post-processing or offline analysis [^5].

Spike sorting allows the decomposition of extracellular recordings into single unit EAP activities. This process typically involves spike detection, alignment, feature extraction and clustering. Although neural interfaces maintain the signal bandwidth in front-end conditioning and comply to Nyquist criteria in digitisation, the temporal precision of spike features can still be compromised in quantisation. Specifically, spike peaks can be 'missed' if incident between sampling cycles, and can then be prone to sampling error causing the peak magnitude be undersampled. The precise detection of spike peaks is critical in ensuring good alignment for spike sorting [^6]. In methods such as template matching it has been shown that spike sorting accuracy degrades significantly with poor alignment [^5]. However, if good alignment can be maintained, then decreasing the template size (i.e. using a reduced sampling rate to provide fewer samples for a fixed spike window) has a negligible impact on spike sorting accuracy. In practice, good alignment can be achieved either by: (1) increasing the sampling rate, thus increasing the temporal resolution, or (2) reducing the sampling rate and interpolating (i.e. upsampling) to 'reconstruct' the peak. Both these methods however are undesirable, as they increase complexity and thus hardware resource (power and area) requirements.

This paper presents a novel data converter design that aligns its samples to the spike peak by adapting its sampling rate, thus combining the good alignment accuracy of a high sampling rate, with the reduced data bandwidth (and power consumption) of a low sampling rate. The core is based on a SAR charge redistribution ADC, which is the topology used in all integrated neural interfaces due to low area and power requirements for low to medium resolution converters. Although adaptive SAR ADCs have previously been reported for neural recording applications \cite{o2011adaptive, huang20121}, these adapt the resolution rather than sampling rate and therefore would not provide benefit to spike alignment as presented herein.

The paper is organised as follows: Section 3 introduces the concept and system architecture; Section 4 details the circuit implementation; Section 10 describes the simulated results and target specifications; and Section 11 concludes the paper.

{{< figure src="/images/iscas2014/concept.svg" title="Figure 1: Proposed concept of fine (high sampling rate) peak alignment with coarse (low sampling rate) data output. Shown is: (a) fixed uniform sampling; and (b) proposed adaptive sampling method." width="500" >}}

# 3 Concept and System Architecture

The basic idea is to use fine sampling at 64 kHz to locate the spike peak, and then sample the rest of the spike using coarse sampling at 16 kHz. It is essential however, that the coarse sampling is peak-aligned (by adjusting sampling clock phase. The adaptive sampling rate is controlled using threshold-based spike detection. This concept is illustrated in Fig. 1. The system architecture is shown in Fig. 2. This consists of two main sub-systems: the core SAR ADC, and the digital alignment controller;  responsible for the spike detection, peak search and detection, and timing/sampling alignment.

{{< figure src="/images/iscas2014/architecture.svg" title="Figure 2: System architecture of the proposed peak-aligned ADC with adaptive sampling rate." width="500" >}}

# 4 Circuit Implementation

The circuit has been implemented as a mixed-signal design in a commercially available 0.35\\( \mu\\)m 2P4M CMOS technology provided by AMS.

## 5 Digital Alignment Control

The adaptive sampling algorithm has been implemented in Verilog using a digital design flow. A standard cell based circuit implementation has been realised using Cadence RTL compiler for synthesis and Encounter for place & route.

The controller, which operates at the 64 kHz clock frequency, consists of 3 main blocks to first detect the spike, then search for and detect the peak and finally to provide the aligned samples to the output register.

## 6 Spike Detection

This is achieved using a double threshold detection method as previously illustrated in Fig. 1. This provides the system sensitivity to both positive and negative peaks. The thresholds are externally calibrated after recording and analysing a training dataset.

## 7 Peak Search & Detection

The state diagram for the peak search and detection is shown in Fig. 3. Here the concern lies with the noise corrupted neural spike that will present fluctuations around the peak maximum. To avoid detecting these artifacts as multiple peaks, a 4 sample window is used that  succeeds the peak sample. Analyzing these samples will indicate whether the signal is still increasing or if the peak maximum has been detected.

{{< figure src="/images/iscas2014/state2.svg" title="Figure 3: State diagram of the Peak-Search and Detection Algorithm." width="500" >}}

## 8 Timing Control

Once the a peak location in confirmed, the data steam is then re-aligned by updating the valid data phase off-set of the down sampled stream and the logic returns to a to the low frequency data monitoring state. In coherence with the spike detection algorithm, data points are continuously throughput at the 16 kS/s rate. Only upon the re-alignment event does the sampling phase at of the data shift. This implies that when the ADC is driven to record at 64kS/s the extraneous data used for aligning will need to be removed from the output steam by means of latching the digital data buffer at valid data times.

## 9 Analog To Digital Converter

{{< figure src="/images/iscas2014/sar_adc.svg" title="Figure 4: 9-bit Differential SAR ADC." width="500" >}}

{{< figure src="/images/iscas2014/clk.png" title="Figure 5: Time Sequencing for a 9-bit Successive Approximation." width="500" >}}

Fig. 4 illustrated the SAR ADC structure. The topology presented here employs a fully differential binary weighted capacitor array that allows for a highly linear 9-bit output that is driven by standard FSM logic. Moreover the top plate sampling technique will minimize the number of buffered voltage sources required for operation. The fully differential configuration is key for mixed signal systems as a significant amount of noise is rejected from the voltage supplies particularly the common mode of the differential input. The typical timing sequence of 10 cycles for the data converter is illustrated in Fig. 5. The basic binary weighter array is highly insensitive towards mismatch and process variation relative to split cap and C2C structures as parasitics load less significant charge with respect to the net capacitance. This justifies the use of minimum feature size $5 \mu m \times 5 \mu m$ poly-poly unit capacitors that have a capacitive value of 23.22fF.

The successive approximation is initiated by sampling the differential input on the top plate of the two capacitor banks and tying the bottom plates the the respective positive and negative reference supplies \\(GND\\) & \\(V_{ref}\\). This is followed by disconnecting the input from the top plate to allow charge redistribution due to changing the polarity of most significant bit (MSB). Each successive evaluation of the comparator will determine in logical value of the quantization bits in decreasing magnitude. The resulting voltage at the input of the comparator due to digital feedback on the bottom plates may be evaluated by use of charge balance equations.

A positive evaluation of the comparator after sampling with the MSB set high will imply the differential input is positive and hence the MSB changes polarity and the second to most significant bit is now 1. The following will be true for both differential and single ended signals;

\\(\\) V_{x} = V_{in} - \frac{V_{ref}}{4} \\(\\)

A negative evaluation of the comparator implies the differential input is positive and hence both the MSB and the second to most significant bit are now 1. Similarly the following will be true for both differential and single ended signals;

\\(\\) V_{x} = V_{in} + \frac{V_{ref}}{4} \\(\\)

Where \\(V_{x}\\) is the resulting voltage at which the input of the comparator settles. It is important to note that due to sampling with the MSB as high this value will is bounded between $GND & Vref$ which is important to prevent forward biasing any diode to substrate. This can be confirmed by considering the input either as slightly higher than \\(V_{ref}/2\\) or as GND.

{{< figure src="/images/iscas2014/comp.svg" title="Figure 6: Schematic Illustration of Comparator." width="500" >}}

The edge triggered comparator structure used in this design is illustrated in Fig. 6. This dynamic latch structure allows good trade offs with respect to speed and the off-set as speed is limited by the gate to drain capacitive component on the input transistors (M1 & M2). These transistors are required to be large in order to minimize off-set components while the latching transistor can be minimum feature size to maximize evaluation speed. The kick back noise of the comparator is alleviated as the feed through capacitance of the input pair is not coupled to the differential output and the differential structure of the DAC cancels the common mode switching components of the comparator. The output is buffered by a latch that will absorb the glitches on the evaluation transitions when both outputs float around the middle of the rail.

The sampling switches are driven by a boot strap circuit [^9] that will drive the gate voltage of the transistor to \\(V_{dd}+V_{s}\\) for a constant over drive voltage of \\(V_{dd}-V_{th}\\). This allow a full dynamic range on the input signal while preventing signal dependent charge injection to be sampled on the top plate. The switch network for the capacitor array employs stacked transmission gates [^10] on the top plates that minimize leakage components which is important for low frequency operation and single complementary transmission gates on the bottom plates that connect the supplies for rapid charge settling.

# 10 Simulation Results

Preliminary validation of the proposed implementation has been done through schematic level simulations in the Cadence IC 6.1.5 Design Environment using industry provided PSP models.

{{< figure src="/images/iscas2014/dnlinl.png" title="Figure 7: Simulated DNL & INL results." width="500" >}}

The ADC INL & DNL performance in Fig. 7 illustrates the 8.9 effective number of bits (ENOB) accuracy of the converter where the INL is limiting figure of merit. This result was produced using a slow input ramp on the ADC input that is sampled 2048 times across the full 3.3V scale and is aligned with the critical sampling points. The excelent DNL figure is a consequence of not using a split capacitor in the capacitor array.

The performance of this system is summarized in Table 1. The average power dissipation of the data converter from the 3.3V supply is $3  \mu W$ when processing typical neural activity that contain 200 spikes per second. This results in a respectable 93.3 fJ per conversion Figure of Merit (FOM) for the $0.35  \mu m$ CMOS technology given the control overhead for timing both the ADC and data buffer. Where the FOM is given by;

\\(\\) \frac{power}{F_{sample} \cdot 2^{ENOB}}\\(\\)

{{< figure src="/images/iscas2014/result2.svg" title="Figure 8: Simulation Results (top) Analog (bottom) Digital output." width="500" >}}

The simulated transient results in Fig. 8 demonstrate the dynamic sampling of a neural signal that has been measured in-vivo at both 16kHz as well as 64kHz. It can be observed that both positive and negative peaks are sampled with fine temporal resolution and their respective peak amplitude & position are also recorded accurately. Note that if a second peak is detected outside of the 4 sample window this peak will also be registered as a maxima ans will realign the data according to the last peak event. Although in this case these positions are very close to one another, a larger window buffer may be required for better tolerance towards spikes that occur consecutively.

Table 1: Data converter Performance Summary}\label{summary
|Reference | [^11] | [^12] | This work |
|----|----|----|----|
|Year				| 2007 	| 2011 	| 2013 |
|Tech. [nm]  		| 90 		| 130 	| 350 |
|Power [(\mu)W] 	| 700	| 1580 	| 3.06 |
|Supply [V] 		| 1	 	| 1.2 	| 3.3 |
|Rate [S/s]  		| 50M	| 50M	| 16k (64k) |
|INL [LSB] 			| \textless 0.6	| - 		| +0.55/-0.59 |
|DNL [LSB] 			| \textless 0.6 	| - 		| +0.25/-0.25 |
|FOM 	[fJ/bit]		| 4.5 	| 55 		| 93.3 |
|Data Reduction   	| - 		| - 		| 70% |

# 11 Conclusion

In this paper, we have presented the design of a novel, resource-efficient, 9-bit SAR ADC with adaptive (16/64 kHz) rate for peak-aligned sampling. This strategy has been adopted to improve alignment precision to enable high performance spike sorting. Furthermore, by combining high precision peak-alignment with a reduced (effective) sampling rate in this way, good efficiency is achieved in both power consumption and data bandwidth utilisation. The design reported achieves a FOM of 93.3 fJ/conversion-step in a standard 0.35\\( \mu\\)m CMOS technology which is comparable to the state-of-the-art. Future work will focus on also achieving adaptive spike detection in addition to further optimisation of the peak search and detection algorithm.

# 12 Acknowledgment

This work was in part funded by EPSRC grants EP/I000569/1 and EP/K015060/1. The authors would like to thank Song Luan for useful discussion and technical support.

# References:

[^1]: I.H. Stevenson and K.P. Kording, ''How advances in neural recording affect  data analysis,'' Nature neuroscience, vol.14, no.2, pp. 139--142,  2011.
[^12]: S.-J. Cho, Y.Hong, T.Yoo, and Kwang-Hyun-Baek, ''A 10-bit, 50 ms/s, 55  fj/conversion-step sar adc with split capacitor array,'' in IEEE  ASICON, 2011, 2011, pp. 472--475.
[^11]: J.Craninckx and G.Vander Plas, ''A 65fj/conversion-step 0-to-50ms/s  0-to-0.7mw 9b charge-sharing sar adc in 90nm digital cmos,'' in IEEE  ISSCC, 2007., 2007, pp. 246--600.
[^9]: A.Abo and P.Gray, ''A 1.5-v, 10-bit, 14.3-ms/s cmos pipeline  analog-to-digital converter,'' IEEE JSSC, vol.34, no.5, pp.  599--606, 1999.
[^10]: D.Zhang, A.Bhide, and A.Alvandpour, ''A 53-nw 9.12-enob 1-ks/s sar adc in  $0.13 \mu m$ cmos for medical implant devices,'' in Proc. ESSCIRC,  2011, 2011, pp. 467--470.
[^7]: S.O'Driscoll, K.V. Shenoy, and T.H. Meng, ''Adaptive resolution adc array  for an implantable neural sensor,'' Biomedical Circuits and Systems,  IEEE Transactions on, vol.5, no.2, pp. 120--130, 2011.
[^6]: M.S. Lewicki, ''A review of methods for spike sorting: the detection and  classification of neural action potentials,'' Network: Computation in  Neural Systems, vol.9, no.4, pp. 53--R7, 1998.
[^8]: G.-Y. Huang, S.-J. Chang, C.-C. Liu, and Y.-Z. Lin, ''A 1-$\mu$w 10-bit  200-ks/s sar adc with a bypass window for biomedical applications,''  Solid-State Circuits, IEEE Journal of, vol.47, no.11, pp.  2783--2795, 2012.
[^2]: R.R. Harrison, P.T. Watkins, R.J. Kier, R.O. Lovejoy, D.J. Black,  B.Greger, and F.Solzbacher, ''A low-power integrated circuit for a wireless  100-electrode neural recording system,'' Solid-State Circuits, IEEE  Journal of, vol.42, no.1, pp. 123--133, 2007.
[^4]: H.Gao, R.M. Walker, P.Nuyujukian, K.A. Makinwa, K.V. Shenoy, B.Murmann,  and T.H. Meng, ''Hermese: A 96-channel full data rate direct neural  interface in 0.13< formula formulatype=,'' IEEE JSSC, vol.47,  no.4, pp. 1043--1055, 2012.
[^3]: A.Bonfanti, M.Ceravolo, G.Zambra, R.Gusmeroli, T.Borghi, A.Spinelli, and  A.Lacaita, ''A multi-channel low-power ic for neural spike recording with  data compression and narrowband 400-mhz mc-fsk wireless transmission,''  Proc. IEEE ESSCIRC, pp. 330--333, 2010.
[^5]: D.Y. Barsakcioglu, A.Eftekhar, and T.G. Constandinou, ''Design optimisation  of front-end neural interfaces for spike sorting systems,'' Proc. IEEE  ISCAS, pp. 2501--2504, 2013.
