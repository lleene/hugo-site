---
title: "A 2.7 μW/MIPS, 0.88 GOPS/mm² distributed processor for implantable brain machine interfaces"
date: 2016-10-17T15:26:46+01:00
draft: false
toc: true
type: posts
math: true
tags:
  - publication
  - processor
  - CMOS
  - biomedical
---


Lieuwe B. Leene, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

This paper presents a scalable architecture in 0.18 um CMOS for implantable brain machine interfaces (BMI) that enables micro controller flexibility for data analysis at the sensor interface. By introducing more generic computational capabilities the system is capable of high level adaptive function to potentially improve the long term efficacy of invasive implants. This topology features a compact ultra low power distributed processor that supports 64-channel neural recording system on chip (SOC) with a computational efficiency of 2.7 \\( \mu\\)W/MIPS with a total chip area of 6.2 mm². This configuration executes 1024 instructions on each core at 20 MHz to consolidate full spectrum high precision recordings from 4 analogue channels for filtering, spike detection, and feature extraction in the digital domain.

# 2 Introduction

A key challenge for state-of-the-art neuroscience is real-time data analysis at a massive scale for the diagnosis, treatment and recovery of incapacitating neurological conditions[^1]. While this field has advanced substantially in the realization of signal acquisition and methods for decoding activity. Current systems show a disconnect between implantable devices and the development of algorithms. The initiatives for next generation BMIs focus on scaling recording capabilities and do not consider a strategy for providing highly efficient processing which is imperative implantable SOCs. Moreover it is rare to see methods actively utilize the reconfigurability of modern sensor systems while maximizing the integrity of decoding spike train activity. Numerous aspects with regard to the signal integrity cannot be anticipated and thus assuming a specific method or signal modality will lead to conservative design because an excessively noisy environment is a potentiality. This reveals that chronic instrumentation have yet to be take advantage of more generic real-time processing to improve the efficacy of these invasive devices. Implantable systems predominantly struggle in finding compact and power efficient architectures for signal decomposition. Moving towards fully packaged millimetre scale devices that can support wireless spike train analysis of hundreds of neurons is a highly contested target for many research groups[^2][^3]. As a result high level reconfigurability is yet to be adopted in the current state-of-the-art.

The approach to specialized DSP in the literature reflects two problems pertaining to neural recording systems. The first is signal extraction from recordings that consists of spike detection to extract compressed spike train data. The other is associated with accelerating adaptive filters that map these spike trains to estimate cognitive dynamics or invoked limb movement. Typical examples for acquiring neural activity are fully synthesized cores [^4] [^4]\cite\{2\} that have been successful in realizing implantable solutions. In contrast high level decoding is predominantly performed by FPGAs as integration makes less sense at the system level [^6]. However highly reconfigurable instrumentation have been suggested to leverage both adaptive noise shaping or artefact removal [^7] [^8].

In line with such work this paper presents a distributed processor architecture. Sec. 3 motivates the direction taken here and models the principle constraints for processing at the sensor interface. The proposed system is introduced in Sec. 4 and contextualized by a software development driven platform. The execution unit implementation is detailed in Sec. 5 and accompanied with performance results in Sec. 6.

# 3  On-Node Processing

In order anticipate how future processing methods can be accomodated in SOCs it is essential to capture high level trends with respect to processing capacity of neural implants. Here digital resource requirements are normalized in terms of state variables for evaluating technology dependency. The number of state variables in a dynamic process is a good indicator for complexity whether is a digital classifier or an analogue filter. Here the focus is exclusively on processing such that the signal of interest is idealized with respect amplitude and representation. Consider \\(L\\) as a normalized feature size that allows the evaluation of parameters for a particular technology and extrapolate them based on constant field scaling factors. This remain adequate considering BMIs are fabricated using wide range of 65 nm to 1 \mmu m CMOS technologies.
$$  R_{D} = \underbrace{ \alpha    f_s   C_{g}   V_{dd}^2   L^2   \log_2(SNR) }_{power} \cdot \underbrace{ \alpha \log_2(SNR) A_{g} L^2}_{Area} $$
Eq. 1 represents the power area product for a digital state variable. \\(C_{g}\\), \\(A_{g}\\), \\(\alpha\\) parametrise typical gate capacitance, area, and overhead for each register respectively [^9]. Similarly \\(f_s\\), \\(V_{DD}\\) reflect the sampling frequency and supply voltage.  Generally the scaling of \\(R_D\\) constituents are well known and guide maximizing system efficiency in an abstract sense [^10]. For the sake of this discussion we assert that analogue instrumentation is limited to a large extent to having an area power product \\(R_A\\) larger than $10^{-15}  Wm^2$ when considering an SNR of 60 dB for a 1.2V system. The derivation comes from the fact that neural signal levels require a specific current dissipation associated with the thermal noise levels and filtering & sampling imply a certain capacitor size according to the supply voltage. The later two terms trade off power with area that can be improved by optimization of the instrumentation topology but will be bounded by signal dynamic range and minimum capacitor sizes.

{{< figure src="/images/biocas2016/Operations.svg" title="Figure 1: Analytic number of digital operations available with respect to different technologies (red) with references to the normalized performance of image processors (blue)." width="500" >}}

With this understanding Fig. 1 illustrates the expected number of digital state variables that aggregate to an equivalent power area product to that of the instrumentation circuit. This shows standard logic in 0.18 um CMOS allows 100 state variables or equivalently 100 operations per sample taken. As reference specialized image processors that similarly rely heavily on data intensive operations are normalized in Fig. 1 to illustrate how technology scaling exhibits the predicted characteristics. As a result it is expected that even for ultra low power BMIs digital processing capacity will be an abundant resource in future systems.

# 4 Neuron-Processor Interface

The high level objective for this system is illustrated in Fig. 2. The application of a generic IoT platform is used to support an unconstrained software stack for networking, data analysis, or system interrogation that best described by high-level languages. This simplifies the development with non-hardware specific software abstractions and accommodates the ease incorporating other modules. The proposed Neuron-Processor Inteface (NPI) device may directly be integrated with the sensor as ASIC and receive configuration commands from this platform to adjust its operation. In extension it follows that peripherals for regulating power and distributing clocks must be integrated on chip. This conforms the interface towards simply providing power and bi-directional data in terms of a SPI protocol.

{{< figure src="/images/biocas2016/Sys_iP.svg" title="Figure 2: Proposed development platform for highly reconfigurable neural recording systems." width="500" >}}

The proposed architecture introduces a large number of on-chip DRAM macros to support the retention of 1024x32-bit instructions. This represents program that is pipelined to each execution unit to instruct filtering coefficients or feature extraction in a manner that can be extended to an arbitrary the number of processing units. Local to each unit is another 1 kbit macro that enables memory intensive methods such as template matching to take place. Four analogue instrumentation channels with a 12 bit ADC is multiplexed to the 8 b processing unit with 68 dB SNDR maximal precision. This is an extension to prior work in [^15] which details the analogue recording implementation.

{{< figure src="/images/biocas2016/NPI_TLT.svg" title="Figure 3: Implemented Neuron-Processor Interface (NPI) system architecture for realizing high performance reconfigurable processing." width="500" >}}

The system is illustrated in Fig. 3, there are multiple layers from system peripheral to the internal units where average data rates progressively increase. We adopt an in-data processing methodology such that the signal is maximally reduced to its principle components at the sensor interface with high-performance digital methods. This mitigates any redundant energy dissipation for data telecommunication. The primary mechanism of operation is the program memory that continuously feeds the stored instructions into the array of processors that operate locally on the recorded data. The execution of these instructions are handled with what is essentially a instruction decoder, memory module and an arithmetic operator. Inherently this implementation will sacrifice the availability of more intricate functionality found in DSPs since the data is not funnelled into one processing unit that can be very elaborate in complexity. The distributed structure is rationalized by the fact that typical methods such as clustering operate at a much lower speed due to the sporadic spiking activity which makes statistical convergence slow. Furthermore these adaptations need to be performed on the order of minutes by which such functions may also be implemented through the redundancy of elementary operations. It is important to mention that multiplexing loses its effectiveness in memory intensive applications such as neural decoding. This is because it does not mitigate the power & area scaling associated with memory allocation and in fact becomes less efficient.

## 5 Execution Unit

It is clear that although all recording channels should execute the same algorithm they will typically not share the same state of operation. This state dependency is exemplified with respect to intermittent processing during bursting neural activity and idling during quiet periods. This is an inherent limitation to sharing the program memory as the dynamic execution of the code where each core has its own program counter or a top level scheduler is not feasible for an arbitrary number of channels. The quasi-out-of-order execution makes it challenging for us to adopt scalable tile structures found in image processing [^11].

Instead branch control or conditional execution is mediated by skipping a section of the incoming instructions if a condition is not met. In this context individual cores may need to execute any section code and branching will only be limited by the dissipation related to the registers pipe-lining the instructions across the chip. As a result any resources associated with cycling through the program has a diminishing contribution to system requirements as the number of channels is increased. This implies that as more sensors are integrated the complexity in algorithm can also increase proportionally which will not be characteristic of conventional implementations that do not pipeline high-level control signals.

{{< figure src="/images/biocas2016/Sys_uC.svg" title="Figure 4: Functional connectivity of the embedded execution unit and sub-blocks" width="500" >}}

The individual components of the execution unit are shown in Fig. 4 and details the main data buses used for exchanging data. The majority operations revolve around manipulating data in the registers R1-R16 as A operand in association with any other data sources that can be used as B operand. In terms of instructions there are always two components where the first is simply the operation executed by the ALU in addition to the two memory sources. The second component optionally extends this simple functionality by writing these intermediate values to multiple other locations or arbitrary branching operations that will take the unit out of sleep.

# 6 Results & Discussion

{{< figure src="/images/biocas2016/Lay_sH.png" title="Figure 5:  Fabricated NPI SOC using a 6-metal $0.18   \mu m$ CMOS process showing the system block annotation and top metal routing. " width="500" >}}

This system has been fabricated using a commercially available 6 Metal \cmostech technology (AMS/IBM C18A6/7SF) for validation. The chip micrograph is shown in Fig. 5 measuring 6.2mm² including test circuits and pad ring. While the architecture is capable of achieving very dense configurations at the system level we emphasize that the sensor interface plays an crucial role for noise isolation and chip area overhead.

{{< figure src="/images/biocas2016/TPhw.svg" title="Figure 6: Realization of the development platform used for characterization system functionality." width="500" >}}

The testing platform is photographed in Fig. 6 which interfaces the NPI system with a raspberry pi module. This set-up supports a embedded Linux operating system with low level device control to meed a diverse set of needs. By monitoring the internal data-bus of one core the specialized processing structure has been exhaustively validated at the design point for operating frequencies of 5 MHz to 20 MHz with varying sampling rates on the ADC. Currently the synthesis of instructions remain tailored in associated to the hardware specific compiler because the low level control is crucial for active ADC and amplifier control.

{{< figure src="/images/biocas2016/uC_PS.svg" title="Figure 7:  Measured power dissipation with respect to specific operations for the same operand A=113 & B=114 in randomized order." width="500" >}}

The results in Fig. 7 shows the dependency of power dissipation with respect to different operators for the same operand A and B. It should be expected that the is a strong operand dependency with respect to power consumption but these results follow post layout simulations closely. When the unit is in a sleep or branching state the power dissipation is mainly associated with the instruction pipeline. As this 32-bit pipeline transverses the entire execution unit it represents a considerable baseline power contribution. While typical power consumption for full activity lies around 45\\( \mu\\)A at 20 MHz. The reduced complexity local to each channel allows this configuration to achieve \\(2.7 pJ/Cycle\\) or $2.7 \mu W/MIPS$. The specifications given in Table 1 summarize the main features associated with this system on chip for processing neural data at the sensor interface.

Table 1: Comparison of performance specifications for the NPI system.
|		Specification | This Work | 2011 [^11] | 2011 [^4] |
|----|----|----|----|
|		Scaling |  Fine | Fine | Coarse |
|		Tech. [nm] | 180 | 65 | 65 |
|		Supply [V] | 1.2 |  1.2 | 0.27|
|		Units	| 64 |  2048 | 16|
|		Freq. [MHz]	| 20 | 300 | 0.48 |
|		Sys. Power [mA]	| 1.42  | 300 | 0.28 |
|		Sys. Memory [kb]	| 32  | - | 50 |
|		Tile Memory [kb]	| 1 | 1 | - |
|		Processor Area [mm(^2)] | 1.37 | 5.10 | 2.09 |
|		P-Merit [GOPS/mW] | 1.52 |  0.31 | - |
|		A-Merit [GOPS/mm(^2)] | 0.88 | 36.1 | -|

# 7 Acknowledgement

This work was supported by EPSRC grants EP/K015060/1 and EP/M020975/1.

# 8 Conclusion

A scalable processing architecture is proposed in effort to realize compact and efficient neural recording arrays. The topology reflects the nature of processing neural data in the context of extracting signal components and we expect the application of this architecture to be relevant to many high channel count neural SOCs. This discussion details both low-level and system level considerations that look towards better software integration. The proposed system power consumption is on the order of \\(1.5 mW\\) with a power density \\(26 mW/cm^2\\). However this figure is subject to the physical & software reconfiguration that allows extensive optimization for different neural recording applications using the same fabricated device. This work aims to realize long term solution for neural recording implants directed at validating neural decoding methods with in-vivo settings. Importantly standardization off-chip interfacing protocols with self-sustained operation should grantee the ease of integrating existing wireless solutions in extension to this system.

# Refernces:

[^1]: I.H. Stevenson and K.P. Kording, ''How advances in neural recording affect  data analysis,'' Nature neuroscience, vol.14, no.2, pp. 139--142,  February 2011.
[^2]: A.Khalifa etal., ''A compact, low-power, fully analog implantable  microstimulator,'' in IEEE Proc. ISCAS, May 2016, pp. 2435--2438.
[^3]: J.S. Ho etal., ''Midfield wireless powering for implantable systems,''  Proc. IEEE, vol. 101, no.6, pp. 1369--1378, June 2013.
[^4]: V.Karkare etal., ''A 75- $\mu$w, 16-channel neural spike-sorting  processor with unsupervised clustering,'' IEEE J. Solid-State  Circuits, vol.48, no.9, pp. 2230--2238, September 2013.
[^5]: A.M. Sodagar etal., ''A fully integrated mixed-signal neural processor  for implantable multichannel cortical recording,'' IEEE Trans.  Biomed. Eng., vol.54, no.6, pp. 1075--1088, June 2007.
[^6]: Y.Xin etal., ''An fpga based scalable architecture of a stochastic  state point process filter (ssppf) to track the nonlinear dynamics underlying  neural spiking,'' Microelectronics Journal, vol.45, no.6, pp. 690 --  701, June 2014.
[^7]: C.Qian etal., ''A low-power configurable neural recording system for  epileptic seizure detection,'' IEEE Trans. Biomed. Circuits Syst.,  vol.7, no.4, pp. 499--512, August 2013.
[^8]: Y.Xin etal., ''An application specific instruction set processor  (asip) for adaptive filters in neural prosthetics,'' IEEE/ACM Trans.  Comput. Biol. Bioinformatics, vol.12, no.5, pp. 1034--1047, September  2015.
[^9]: T.N. Theis and P.M. Solomon, ''In quest of the "next switch" prospects for  greatly reduced power dissipation in a successor to the silicon field-effect  transistor,'' Proc. IEEE, vol.98, no.12, pp. 2005--2014, December  2010.
[^10]: M.Verhelst and A.Bahai, ''Where analog meets digital: Analog-to-information  conversion and beyond,'' IEEE Solid-State Circuits Mag., vol.7,  no.3, pp. 67--80, September 2015.
[^11]: T.Kurafuji etal., ''A scalable massively parallel processor for  real-time image processing,'' IEEE J. Solid-State Circuits, vol.46,  no.10, pp. 2363--2373, October 2011.
[^12]: H.Noda etal., ''The design and implementation of the massively  parallel processor based on the matrix architecture,'' IEEE J.  Solid-State Circuits, vol.42, no.1, pp. 183--192, Jan 2007.
[^13]: J.Y. Kim etal., ''A 201.4 gops 496 mw real-time multi-object  recognition processor with bio-inspired neural perception engine,''  IEEE J. Solid-State Circuits, vol.45, no.1, pp. 32--45, Jan 2010.
[^14]: C.C. Cheng etal., ''ivisual: An intelligent visual sensor soc with  2790 fps cmos image sensor and 205 gops/w vision processor,'' IEEE J.  Solid-State Circuits, vol.44, no.1, pp. 127--135, Jan 2009.
[^15]: L.B. Leene etal., ''A compact recording array for neural interfaces,''  in IEEE Proc. BIOCAS, October 2013, pp. 97--100.
