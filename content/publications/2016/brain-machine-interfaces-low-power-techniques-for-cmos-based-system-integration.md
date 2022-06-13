---
title: "Brain machine interfaces: low power techniques for CMOS based system integration"
date: 2016-08-08T15:26:46+01:00
draft: false
toc: true
math: true
type: posts
tags:
  - chapter
  - thesis
  - CMOS
  - biomedical
---

Lieuwe B. Leene, Yan Liu, Timothy G. Constandinou

Department of Electrical and Electronic Engineering, Imperial College London, SW7 2BT, UK

Centre for Bio-Inspired Technology, Institute of Biomedical Engineering, Imperial College London, SW7 2AZ, UK

# 1 Abstract

The emergence of miniaturized electronic sensors for recording neural activity is opening up new opportunities for better health care and understanding brain function. The precise instrumentation for sensing these signals has been developed extensively, but no implantable system available today is capable of providing a high density recording structures that can be scaled to accommodate the large number of electrodes and processing neuro-prosthetics need for functional limb replacement. The design of these systems is complicated by micro-volt levels of signal that contain convoluted mixtures of information. This demands highly accurate signal quantization and exhaustive processing that is constrained by the scarce power availability. The resulting difficulty in realizing viable solutions for chronic implants necessitates cutting-edge fabrication technologies and state-of-the-art circuit optimization techniques.

This thesis presents the understanding behind optimizing these instrumentation systems in order to maximize the simultaneous sensing capabilities of brain machine interfaces that can be implanted wirelessly into living systems. These analytics enabled this work to outperform state of the art in terms of delivering high precision at 56 dB SINAD with a sub 0.01mm\\(^2\\) silicon footprint and a 800 nW power budget by employing novel time-domain circuit techniques. This advancement will enable BMIs to be integrated & minimutrized using nanometre CMOS with extensive digital processing capabilities that are capable of decoding neural signals without supervision such that therapy in a fully implanted fashion. Moreover by introducing distributed processing architecture this work is the first to allows scalable fully reconfigurable functionality at the instrumentation interface for complex algorithmic operations while maintaining a power efficiency of 2.7\\(\mu\\)W per MIPS.

I would like to express my sincere gratitude for the opportunities and guidance that Dr. Timothy Constandinou has given me. It has been a wonderful experience to peruse my passion for electronics and do research guided by his generous supervision. He has made working with the next generation neural interfaces group has been a genuine privilege. I also extend my thanks to my colleges at the centre for bio inspired technology for providing an amazing environment in B422. It is inspiring to see so much talent come together and find ways to work and have fun together. I especially want to thank Tor Sverre Lande for his the inspiration and insightful discussions. Finally I would like to thank my friends and family for their support and encouragement.

# 2 Introduction

The ability to tap into the electrical activity of the central nervous system holds the promise of personalised health-care with unparalleled capabilities such as restoration of vision or paralysis [^2]. The development of implantable electronics that enable these capabilities are a key component to any future of bio-electronic medicines termed as electroceuticals that exhibit superior spatial and temporal precision than the chemical counterpart. This follows a vision for electronics that can be distributed throughout the body to treat a plethora of neurological conditions and psychological disorders by attaching to nerve endings to decode and modulate neural signalling[^3]. These devices provide a means to model neurological activity and find a basis for diagnosing of brain related diseases. However the human brain alone distributes the activity of \\(8\times10^{10}\\) neurons over a \\(1200 cm^3\\) volume with intricate structures where current recording systems can only observe a minute fraction of isolated activity with centimetre scale devices. Making these systems practical and useful requires more effective ways to distribute the recording of activity. This requires techniques for miniaturization towards minimally invasive implantable recording devices.

"""
Today’s best brain-computer interface systems are like two supercomputers trying to talk to each other using an old 300-baud modem
        2016 - Phillip Alvelda [^4]
"""

One exemplary effort directed at achieving better sensors for decoding neural activity is currently a $60 million project under a Neural Engineering System Design (NESD) program that is lead by the Defence Advanced Research Project Agency (DARPA). This is one of eight aspects under the brain initiative that is lead by research in the US which signifies the explicit importance of developing better interfaces to enable new technologies. From a data processing perspective the principle issue with current systems is the limited information rates that can be extracted from chronic neural recording devices.  

# 3 Motivation

Brain machine interfaces have long been seen imagined as a solution to incapacitating neurological injuries like paralysis, spinal cord lesion, stroke, and brain trauma. However such a solution has eluded science for a number of decades. The functional interaction between electronics and neural tissue dates back to 1870 when Gustav Fritsch and Eduard Hitzig first questioned the muscular contractions due to electrical stimulation of the motor cortex [^5]. This extensive development took many years in part because modulating neural signalling electronically in well controlled manner requires exquisite precision and correctly decoding the brain activity is a challenging processing problem that requires a intricate understanding in underlying brain function. The first success for interfacing electronics with neural circuitry is that of the cochlear implant which was approved by the American Food and Drug Administration (FDA) in 1985 [^6]. In 2015 these implants help 13 thousand individuals over come their hearing disability in the UK alone [^7].

Today we face an unprecedented and increasing number of patients with neurological disorders which we have yet to find rehabilitating treatment for. In fact 350 thousand people in the UK lost their self-reliance due to a disabling neurological condition [^8]. Many of these cases are the result of unsuccessful rehabilitation after stoke, spinal cord/brain injury or our inability to treat progressive neurodegenerative conditions such as amyotrophic lateral sclerosis. While these disorders still challenge our scientific understanding, the application of machine assisted intervention for neural repair and rehabilitation has demonstrated promising results with invasive implants [^9] and non-invasive robotics [^10]. Such experimental results encourage us to continue these efforts but it is also evident that this domain requires substantial improvements towards clinical solutions equivalent to that of deep-brain stimulators, pacemakers or the cochlear implants. In retrospect the guiding imperatives currently perused by leading research for better bioelectronic medicines in humans hope are aimed at meeting a number of neuroscience achievements by 2020 [^3]. These efforts can be classified with five essential components;

{{< figure src="introduction/Mapping_A.pdf}" width="500" >}}

{{< figure src="introduction/Mapping_B.pdf}" title="Figure 1: " width="500" >}}

** Structural & functional mapping ** Revealing the signalling interconnect for organ-centric nerve wiring and functional signalling patterns provides a baseline for the diagnosis and understanding of nervous system. Similar to that in Figure 1 where the learning process of a rat brain is investigated with regard to functional patterns. This objective includes establishing correlations between organ function and neural activity. In order to catalogue these details we require tools for high-resolution imaging of fibre anatomy and taxonomy at micrometer resolution. The scale of exploring inter- and intra-species variation in neuroanatomy necessitates the collaboration through documenting a library or repository of tracers for visualization and standardized data collection. Moreover we need to find methods for precise identification and referencing nerve structures in a clinical environment.

{{< figure src="introduction/Organ_A.pdf}" width="500" >}}

{{< figure src="introduction/Organ_B.pdf}" title="Figure 2: " width="500" >}}

** Sensing organ functions ** Finding better means to support the close-loop functionality of bioelectronic factors in the body and organ behaviour is essential. Due to natural development and biological adaptation we require detailed understanding of physiological dynamics and thereby inferring organ function from marker variation. Here we need microscopic sensors that monitor and survey a variety of markers that allow us to characterize the changes in physiological markers in relation to organ and neural activity. Introducing low risk and highly reliable sensors is crucial for performing well defined and chronic data collection on patient variance. Here Figure 2 exemplifies such a sensor interfaced with the lower spinal cord to study the efficacy of neuro-reconstruction techniques to recover bladder control [^12].

{{< figure src="introduction/electrode_A.pdf}" width="500" >}}

{{< figure src="introduction/electrode_B.pdf}" title="Figure 3: " width="500" >}}


** Electrodes for visceral nerves ** Improving electrode-based interfaces for reliable recording and modulation is a proven enabler for many clinical applications. Miniaturization of cuff-electrodes is necessary for interfacing small nerves that are \textless100\\( \mu\\)m in diameter adjacent to organs that provide greater specificity for treatment. As shown in Figure 3 these are complex structures that require delicate application in a clinical setting. Furthermore high-density arrays that exhibit shape-adaptable contacts could allow us to further maximize signal-to-noise and reliability. These platforms will need algorithms in order to track time evolving activity across multiple fascicles.

** Signal imaging and actuation ** Exploring other biophysical techniques that allow us to decode and actuate neural activity with less invasive means may result in more effective means for clinical applications with lower risk factors than cortical implants. This includes expanding on the current optogenetic methods to distribute excitatory or inhibitory activity in highly specific neuronal populations. Scaling electromagnetic and ultrasonic imaging to more practical form factors may also enable improved sensing modalities. Using nano-particles to enable remote interrogation by aforementioned sensing modalities also requires evaluating in-vivo reliability.

{{< figure src="introduction/Viceral_A.pdf}" width="500" >}}

{{< figure src="introduction/Viceral_B.pdf}" title="Figure 4: " width="500" >}}

** Visceral control modules ** Enabling implantable sensors like that in Figure 4 requires integrating the interface with power management, wireless connectivity, and processing capabilities in highly miniaturized configurations. In particular these platforms need to provide modular support that enables recording, stimulation and blocking experiments for proof of concept. Developing the support for characterizing organ specific neural activity on-chip facilitates closed loop control without intervention. Moreover the capacity for signal processing and pattern recognition will improve bandwidth management for sensors with larger channels counts.

# 4 Research Objectives

Contemporary objectives for sensor design used in neuroscience applications can be approached from a number of perspectives. One could focus on wireless connectivity of body sensor networks, the chronic behaviour of miniaturized electrode interfaces, Analysis methods for distributed neural activity, or exploring organ specific functional indicators. All of which reflect how the research imperatives can be addressed in the domain of electronics. This work will specifically focus on the miniaturization and optimization of integrated electronic instrumentation. This work will form a basis for maximizing the capacity of implantable systems in a general sense irrespective of their functional purpose. In particular we raise the question: how does one enable a wireless implant to record from thousands of channels without being constrained by the bandwidth of telecommunication? Moreover how do we grantee that the integrated chip uses the absolute minimum amount of power and silicon area such that the system becomes viable for implantation? Can we find better ways to miniaturize these devices with existing technologies and what are the current limitations?

Here we attempt to approach the design of brain machine interfaces specifically with the objective of integrating thousands of channels on a single CMOS chip. This perspective implies not only that we need to find ways to miniaturize the electronic circuits used for sensing but also find processing architectures that perform highly efficient signal analysis irrespective of channel count. This reflects our consideration towards a fixed communication bandwidth that results from the limited power budget. The implication is that the neural recordings need to be compressed by representing only high level features of collective activity. As the number of channels increases our processing capacity must proportionally increase to accommodate the increased compression rate.

** More explicitly, this work aims to develop a fully integrated instrumentation system for brain machine interfaces that is functionally far more capable and much more power efficient than conventional systems though analytic optimization methods and circuit level techniques.**  

# 5 Thesis Outline

The elementary components to these systems are discussed in Chapter 6. We review how neural activity is sensed electronically and the physiological components that affect these measurements. In addition we address how modern technologies are advancing the capabilities of neural recording systems to give insight to future prospects for BMIs. In particular we will discuss the associated impact CMOS integration has on sensor characteristics based on trends in on going efforts. Finally we overview brain machine interfaces that are currently presented in the literature by reviewing the current considerations in designing these sensors.

The principle discussion presented in Chapter 16 is based on the analysis of instrumentation circuit design and the optimization there of that enables us to achieve state of the art sensing efficiency. The methodology discussed informs us how resource efficiency is dependent on both topology and CMOS process parameters. In particular by introducing the underlying resource relations for amplifiers and data converters we can present a perspective on their system level implications. This discussion addresses the impact of circuit topologies to leverage the fundamental relationship between resource requirements and the performance specifications. In association we propose several topologies in each domain that can excel at maximizing performance with the minimum area and power requirements specifically for these low frequency signals. Finally these results are extrapolated to introduce the dependency on voltage scaling and higher order filter configurations. This reveals observable relations and limits with regard where our expectations lie given the direction of miniaturizing instrumentation structures.

Section 30 continues this notion of resource optimization by abstractly quantifying the extent we can perform processing on chip under the assumption that the design should dedicate as much resources on analogue instrumentation as on signal processing. This leads to the impression that depending on the construction of the algorithm there is an increasing amount of capacity for distributed digital processing as these systems employ more modern CMOS fabrication processes. Here we introduce an efficient implementation of two spike classification algorithms in association with a detection operator to quantify the resource requirements for methods commonly used in the literature. With this context we introduce a scalable microcontroller topology the enables distributed processing across an arbitrary number of channels and executes reprogrammable algorithms with exceptional efficiency when large channel counts integrated on chip.

Section 43 uses the observations from the foregoing discussions to identify two components that allow integrated sensors to substantially improve performance. The first is using time domain topologies to realize a instrumentation topology based on digital logic gates that do not diminish performance due to transistor imperfections. By employing sub-threshold oscillator structures in amplification circuits the topology can achieves near ideal noise efficiency similar to conventional sensing but with improved characteristics. This structure exhibits significantly increased input impedance and reduced power dissipation than a more conventional realization would. The second component is that we propose performing adaptive classification of spike signals in the analogue domain in order to avoid digital processing data at the Nyquist frequency. This takes advantage of reduced feature bandwidth in neural recordings. Finally the different approaches to neural classification with minimal hardware requirements is evaluated in the analogue and digital domain. The proposed mixed signal method shows that we may opt to use an analogue integrator for every cluster extracted without needing analogue to digital conversion.

Section 53 summarizes this work by considering how the proposed architectures can be improved upon to approach better system integration. Reflecting on the current capabilities of the proposed system we conclude that much effort is still needed for realizing chips that are capable of directly decoding neural activity. While proposed platform already exhibits the necessary flexibility to accommodate a number of scientific inquiries there are two directions that are clearly exemplified with regard continuing research objectives. This outline can summarized in terms of the following technical details listed below.

**Section 6**
 - Fundamental aspects for sensing of neural activity electronically and the trends in current BMI technologies.
 - Review of the fully integrated BMI systems presented in recent literature.

**Section 16**
 - Chopped amplifier structure for the miniaturization of power efficient instrumentation and the design considerations there of.
 - Power efficient oversampling ADC topology for compact signal quantization with minimal area requirements.
 - System level resource models that addresses the configuration/optimization of amplifiers, data converters and digital processing.

**Section 30**
 - Rationale for in-channel processing and the design of template-matching and PCA based methods for that context.
 - Scalable processing architecture based on software-defined instrumentation and the implementation there of.
 - Linux-based ASIC interfacing platform that enables real-time data visualization and high level instrumentation protocols.

**Section 43**
 - Introduction for using sub-threshold ring oscillators as resilient time-domain memory that allows analogue processing with ultra-low supply voltages.
 - VCO based instrumentation topology for nano-metre CMOS capacitively coupled amplifiers and filter structures.
 - Develop a basis for performing adaptive neural spike detection & classification in the analogue domain.

# 6 Background

In order to detail how we might be able improve the current approach of using electronic sensors to record neural activity. This chapter will review the primitive components to sensing brain signals and associate them with research developments that are promoted though the miniaturization in microelectronics. The discussion will give insight to trends like Moore's law that allow us to envisage what to expect from BMIs several years beyond current state-of-the-art and reveal challenges that still need to be overcome. This chapter is organized by introducing the basics of sensing of neural activity in Section 7 followed by a discussion on technology impact in Section 8. Finally we summarize what current systems look like today with respect to their capacity for decoding brain function in Section9.

# 7 Electrical Sensing of Neural Activity

The basis for interacting with neural activity electronically is derived from charged carrier exchange that couples electronic devices to the intracellular or extracellular potentials found in neural tissue and its fluids. Neurons found in the human brain signal information throughout the body by releasing various types of neurotransmitters at synaptic connections. Because the release of these chemical species is mediated by triggers from the localized membrane potential. A neuron's chemical activity can be inferred sensing voltage fluctuations at the cell membrane. Individual neurons will exhibit a variety of dynamics across the their cell membrane, the most prominent of which is the spiking response due to an excitatory threshold crossing in it membrane potential. These dynamics also include membrane oscillations and sub-threshold responses which can be detected but are substantially less energetic. However all of these phenomena derive from the interaction of gated ion-channels in these excitable membranes that enable the transmission of neural activity across the body of the neuron [^15]. The specificity of this behaviour arise from specific neural characteristics that play a vital role in brain structure. For instance pyramidal neurons found in the hippocampus with slow-firing characteristics gain high place specificity with increased plasticity while fast-firing neurons have low selectivity but hypothetically promote neural network stability [^16]. Plasticity refers to how easily a neuron changes it synaptic weights to increase sensitivity to trigger a response from the incident action potential of specific neuron. Evaluating factors relating to response latency, tuning and extracellular waveforms of individual neurons allows us to study their role in the network passively or in response to external stimulus.

{{< figure src="literature/record_neuron.pdf" title="Figure 5:  Instrumentation for probing neural electro-physiology intra cellularly (above) and extracellularly (below)." width="500" >}}

The small signals generated by migration of ionic species is historically studied using the patch clamp method where an amplifier directly senses intracellular potential by means of a pipette sealed to the cell's membrane[^17]. This is illustrated in Figure 5. In addition we could perform extra cellular recording where an electrode is placed in close proximity to the cell. A critical difference separating these two measurements is that extracellular recording is significantly effected by the electrostatics of surrounding tissue. In particular intermediate neurons, genial cells, or astrocytes due to tissue scarring will attenuate the signal making it more difficult to detect activity. The defining advantage on the other hand is that embedding a shank with multiple electrodes will record the activity of numerous neurons without needing a clamping or sealing procedure. This allows close inspection of localized neural circuits and their interaction instead of the intricacies of single cell mechanisms. Either method however will allow the use of ion or protein sensitive electrode membranes for precise analysis of cellular fluid constituents.

{{< figure src="literature/coupling_phys.pdf}" width="500" >}}

{{< figure src="literature/coupling_elec.pdf}" title="Figure 6:  Representation of measuring neural activity with extracellular recording due to ion displacement. " width="500" >}}

Figure 6 illustrates the physiological and circuit equivalent understanding of how conduction dynamics at the membrane are coupled to an extracellular electrode. This coupling defined as \\(V_{MEM}/V_{OUT}\\) is related to what signals appear on the voltage output of the amplifier from which we want to infer how ionic species are being modulated at the cell membrane. That is we want to detect the time dependent or reactive variations in ionic membrane conduction \\(g_{Na-}\\) and \\(g_{K+}\\) which will be loaded by various components before appearing at the input of the amplifier. This is particularly important when considering electrode composition in order to couple to the input of the amplifier. One such consideration would be avoiding faradaic charge injection from the electrode that may result in the disassociation of molecules that form harmful by-products [^18]. The physiological representation of spiking activity gives the idea that upon membrane stimulus the activation of sodium channels displaces charge inwards. This induces a localized recess in charge near the electrode before the potassium channels activate to initiate the repolarization of the cell. The effect of any intermediate tissue can be modelled by lossy coupling represented by the impedance \\(R_{e}\\), \\(R_{cell}\\), and \\(C_{cell}\\). Similarly the electrode response can be modelled using Randeles circuit by extracting the equivalent parameters \\(R_{ct}\\) and \\(Z_{CPE}\\) [^19].

In this respect we observe that the response observed at the amplifier is both dependent with respect to frequency and stay loading from biological or electronic elements in the signal path. Particularly the high frequency content or spiking activity is inhibited from coupling effectively through the tissue due to shunt resistance and stray capacitive loading. This also highlights that because the impedance of the electrode is proportional to its surface area when we reduce its size we must make sure to proportionally reduce the parasitic loading from the instrumentation in terms of \\(C_{par}\\) and \\(R_{par}\\).

{{< figure src="literature/cp_m1.pdf}" width="500" >}}
{{< figure src="literature/cp_m3.pdf}" width="500" >}}
{{< figure src="literature/cp_m2.pdf}" title="Figure 7: " width="500" >}}

These relations are well understood and summarized in Figure 7 following a review on multi-electrode array technologies in [^20]. The nature of this analysis similarly extends towards larger scale recordings like electrocorticography and electroencephalography where we increasingly subject the signals to a larger tissue barrier which limits propagation of electrostatic dipole effects. It also clarifies why low-frequencies tend to be more a prominent basis for analysis in the case of less invasive methods because they are less effected by the attenuation effects. In contrast consider the advantage related to high spacial resolution at higher frequency bands as the measurement of single unit activity is isolated from distant sources by means of this attenuation. This will infer that recordings associated with analysing action potential activity are more invasive but will lead to better confidence in observing specific functional and temporally precise diagnosis of brain structures.

# 8 A Technology Perspective

The prolific impact developments in the microelectronics industry is compelling enough that its prediction, Moore's law, has come to represent an established achievement for integrated electronics [^21]. The perpetual reduction in cost and sustained performance enhancement has become a strong driving force that many technologies exhibit similar growth characteristics in exponential progress simply by association with CMOS integrated circuits. While it could be considered a self-fulfilling prophesy, the expectation of progress has had a profound impact on science and engineering where research can be directed at objectives five to ten years ahead of contemporary technology to address emerging challenges. As a result leading research is not only associated with advancing our current understanding but also finding new ways to augment the methods used to validate these studies.

{{< figure src="literature/trend-TPY.pdf}" width="500" >}}

{{< figure src="literature/trend-NPY.pdf}" title="Figure 8:  Exponential growth in research driven technologies." width="500" >}}

In 2015 Moore's Law celebrated its 50\\(^{th}\\) year and in Figure 8 we look back at its uncanny accuracy. While not evident, CMOS as a technology has had to address numerous hurdles like gate leakage, thermal limits of packaging, and the break down of mesoscopic carrier transport. The exponential growth in computational capacity per Watt in particular has played a mayor role in enabling mobile devices that are seeing new opportunities in point of care medical systems. Cost reduction is most certainly not the only factor that is driving the translation of CMOS to enhance a technology like patch clamp electrophysiology. The application of miniaturized electronics to a field like neuroscience introduces a considerable amount of added-value as 'Moore than Moore' scaling benefits beside digital processing power. These include increased sensor sensitivity, material diversification, sensor in package integration, or specific manipulation of quantum effects. The characteristic growth in the number of simultaneously recorded neurons in Figure 8 is a exemplary indicator how Moore's law is accelerating development in neuroscience. Upon the introduction of using microfabrication techniques to create electrode arrays on glass in 1972 [^24] there has been a rapid growth in the number of simultaneously recorded neurons used in experiments. This growth accelerated again in the late 1990s when silicon based micro-fabrication techniques for micro-machined probes that established unprecedented capabilities. This trend can be interpreted to reflect that current systems are still unable to over come the complexity of how information in encoded within neural activity such that these application seek to acquire more recordings and measures. Nevertheless a substantial progress has been made over the past decade where only recently we have started to see successful real-time prosthetic control with a few degrees of freedom [^25].

{{< figure src="literature/RND-for.pdf" title="Figure 9: Primary factors influencing development of neural interfaces." width="500" >}}

Figure 9 outlines the external drivers for innovation and more effective neural interface systems. As shown there is a engineering domain that primarily revolves around technology translation and pushing the capabilities of current integrated systems. The research driven factors from a bio-medical standpoint come from developing better models of the human body and finding new ways to interact with electronics or interpret signals. A large part of bio-medical research effort for interfaces is in order to explore basic science where we take the brain initiative[^26] or the human brain project[^27] as example. The nature of this research allows us to envision more effective ways to perform chronic treatment of neurological disorders and improving diagnostics by interfacing electronics with the human nervous system in the form of electroceuticals[^28] or optogenetics[^29]. While there remain many questions in regard to what the most effective means is to interact with the nervous system there are very clear short term goals associated with limb replacement and real time prosthetic control [^30]. Although our focus here is with regard to the fundamental challenges associated with electronic sensors and instrumentation of neurons it is important to acknowledge their role in facilitating of high level objectives associated with these efforts. The impact technology has on sensors systems in particular can be derived from three factors; CMOS-Scaling, specialized processing architectures, and More-Moore System integration. The most obvious is that of the CMOS-Scaling which primarily correlates digital performance with the decrease in technology feature size. Because power dissipation is directly related to the switching losses used for clocking operations in digital systems. Reducing the physical size of devices implies a reduction in transistor capacitance \\(C_{gate}\\). This well known relation for power dissipation; $Power = N_{tran}   C_{gate}   V^2_{DD}   f_{c}/2$ tells us for given supply voltage \\(V_{DD}\\) and clock frequency \\(f_{c}\\), the complexity of our digital system will infer how many transistors \\(N_{tran}\\) are used or equivalently how much capacitance is switched. In fact we can accurately anticipate to what extent different CMOS parameters will change under different scaling laws as technology progresses to finer transistor sizes[^31].

Table 1:
|		**Description** | **Parameter**         | **Constant Field** | **Maximum Speed**			   | **Multi Core**			   | **Adiabatic Scaling** |
|----|----|----|----|----|----|
|		Gate Length          | (L_{gate})                 | (1/\alpha)     			| (1/\alpha)                           | (1/\alpha)                        | 1                 |
|		Wire Geometry        | (W,L_{wire})               | (1/\alpha)     			| (1/\alpha)                           | (1/\alpha)                        | (\alpha^2)        	|
|		Supply Voltage       | (V_{DD})                   | (1/\alpha)     			| 1                                    | 1                                 | 1                 |
|		Gate Capacitance     | (C_{gate})                 | (1/\alpha)     			| (\alpha)                             | (1/\alpha)                        | 1                 |
|		Clock frequency      | (f_{c})                    | (\alpha)       			| (\alpha)                             | 1                                 | (1/\alpha)        |
|		Transistors per Core | (N_{tran}/core)            | (\alpha^2)     			| (\alpha)                             | 1                                 | 1                 |
|		Core Density         | (N_{core}/A)               | 1              			| 1                                    | (1/\alpha)                        | (\alpha)         |
|		Power Density        | (Power/A)                  | 1              			| (\alpha)                             | 1                                 | 1                 |
|		Digital Throughput   | $f_c   N_{tran} N_{core}$ | (\alpha^3)     			| (\alpha)                             | (\alpha)                          | (\alpha)|


The nature of the scaling laws in Table 1 reflect the different limitations for processing capacity in terms of \\(\alpha\\) using different scaling modalities. Constant field scaling has been the predominant drive for improved performance that extends from the 1970s. Until the late 1990s where the threshold in particular was preventing \\(V_{DD}\\) to be scaled proportionally due to off-leakage in the deep sub-micron domain. This implied a combination of constant field and maximum frequency scaling was employed to increase processing throughput. While average power densities of integrated chips increased it became more evident other solutions were needed. This led to the commercialization of multi-core scaling in the mid 2000s that physically distributed the performance across a multitude of integrated circuits. This was known to be limited Amdahl's law[^32] where the bottleneck transforming software to become highly parallel in execution. Anticipating this inevitable bottle neck the current direction for performance enhancement is looking for other scaling modalities that exploit the availability very large number of specialized transistors structures. Adiabatic operation for charge recovery has in fact been studied as a power reduction technique for over a decade [^33]. This is currently being proposed in association with the processor in memory solution to address some of the data intensive problems [^34].

$$  U_{Adiabetic} = \frac{ C   V^2_{DD} }{ 2 } \cdot \frac{\tau_{RC}}{ t_s } $$

It is interesting to note the fundamental concept behind this motivation as detailed in [^31] in attempt to explore new mechanisms that reduce energy dissipation in switching systems. We can derive Equation 1 when we consider the power dissipation of a digital switching circuit \\(U_{Adiabetic}\\) when instead of a fixed supply voltage we have a fixed supply current. We observe that if the charging phase \\(t_s\\) is much larger than the circuit's time constant \\(\tau_{RC}\\) the dissipated energy is reduced and charge is recycled with other logic blocks. Moreover if this is configured with a resonant inductor \\(L\\) for energy recovery we fundamentally expect significant improvements over conventional CMOS in power dissipation based on fundamental principles in nano-meter CMOS [^35]. This has conceptually already been applied to neural stimulation circuits [^36] as wireless sensors are typically powered by a resonant power source this technique's prevalence is expected to be more frequent.

While the fundamentals of devices and processing architectures continue to evolve, where do we find analogue sensors in this changing context? Because the disparate nature of analogue sensing is continuous in operation the improvement in switching characteristics of the transistors will not be reflected. Fortunately the concept of semiconductor based instrumentation is well abstracted to the extent that we can predict the performance of analogue sensors with equivalent accuracy as that of digital circuits. In particular it turns out that many process parameters do not significantly affect the power dissipation of analogue sensors which we aim to aggressively minimize [^37].

$$  Power \propto kT \cdot SNR \cdot BW \cdot \frac{1}{V_{DD}}   \frac{\Gamma}{gm/I_D} $$

Equation 2 embodies the main dependencies with respect to power dissipation for sensing signals electronically with a certain bandwidth \\(BW\\) and uses constants \\(kT\\) and \\(q\\) to represent the Boltzmann energy and the electron charge respectively. Here \\(gm/I_D\\) and \\(\Gamma\\) represent transistor efficiency in terms of its transconductance per ampere and noise excess factors respectively. With respect to the different technology scaling we can see two elements that will change as process parameters change. That is the voltage supply which scales somewhat inversely to that of digital dependency and the transconductance efficiency. This efficiency factor generally is equivalent the the transistor sub-threshold slope in the low-power domain which ideally approaches a theoretical value of \\(ln(10) kT/q\\) independent of technology. This factor is as important to analogue as it is to digital operation so we expect a constancy in good transconductance efficiency for most CMOS technologies. The supply scaling however directly deters all-analogue sensor systems from migrating to more advanced processes because it may imply increased power dissipation if we naively attempt to use the same topology.

{{< figure src="literature/gain2tech.png}" width="500" >}}
{{< figure src="literature/lin2tech.png}" title="Figure 10: " width="500" >}}


In addition to an increased power budget it is typical to see trends similar to those illustrated in Figure 10. This shows that using more advanced technologies may result in the minimum size transistor to behave less like an ideal transconductance element than its previous generation. This manifests itself by reducing amplifier gain or distorting filter linearity that prevent linear amplification of small signals. Ideally we want predictable relations between the small gate voltage variation and drain current of a device but this is becoming more difficult to achieve due to the dependency on the drain potential and short channel scattering effects. In addition these scaling laws will also imply variability in impurity doping concentrations have a proportionality to the scaling factor \\(\alpha\\). In fact we can estimate its effect on threshold voltage variance \\(\sigma_{Vth}\\) using the process parameters \\(t_{ox}\\), \\(N_{A}\\), \\(t_{ox}\\), and $L_{eff} W_{eff}$ which represent the transistor's gate oxide thickness, channel doping concentration, and effective channel area resprectively [^38].


$$  \sigma_{Vth} \approx 3.19 \times 10^{-8} \left( \frac{t_{ox}   N^{0.4}_{A}}{√{L_{eff} W_{eff}}}  \right) \propto \alpha^{0.4} - \alpha^{1.4} $$

Most terms in Equation 3 will correlate to some extent between similar analogue transistors due to the fact when that they are placed close to one another and will experience similar statistical distribution in their parameters. It is not possible to prevent the over all variance for degenerating as the sensitivity literally approaches discretization at quantum levels. This has lead to the prevalence of digital calibration and pre-distortion techniques to counteract these shortcomings and still take advantage of increased bandwidth of analogue circuits. In addition this trend also explains the recurrence of mixed signal systems in modern sensor systems where the availability of immediate signal processing can effortlessly be taken advantage of. Dealing with transistor imperfections for circuits is one of the biggest effort in current analogue circuit design theory[^39].

This brings us to the importance algorithms and machine learning for sensor systems in particular. It is becoming more common that modern systems have an abundance of data and processing capacity at its disposal. This has generally lead to 'smart' sensors that can extract an adaptive set of indicators or refine signal structure at the source instead of using supervision to fine tune any changing characteristics for each sensor exhaustively. For BMIs in particular the input data has unknown mixtures of information that we can only generally assume as relevant by probing the right sections of brain structure in the area of implantation. Dealing with this decoding problem can be quite demanding in the context of recording from large ensembles of neurons. If we inevitably want to achieve a mobile solution for brain controlled prosthetics it would be imperative to develop specialized hardware and processing topologies that can achieve efficient computation on a implantable platform [^40].

{{< figure src="literature/learning.pdf}" title="Figure 11:  Different classes of processing modalities with respect to topology where supervised processes are in white and adaptive processes are in grey." width="500" >}}


The classes of methods being applied to neural sensors are very rich where some focus on extracting various characteristics in recordings while others focus on reinforcement learning associated with subjects adapting to a prosthetic[^45]. Figure 11 depicts the typical structure for methods used in neural signal decoding with references and annotated automation. We note that at least in the literature there is a general trend to wards full automated feature mapping and representation discovery because a priori understanding on signal encoding is not needed at the cost of being less resource efficient. This is a highly diversifying field because there are many challenges that remain to be addressed effectively such as the effect if long term behavioural dynamics on cognitive state variables [^46]. Even assuming spike rate based cortical recordings are used it is difficult to assert to which decoding method these systems will converge to in the long term. More typically novel methods approach improving performance by contributing to the framework of signal analysis. Typically this is not done in conjunction with the hardware or computational requirements which has led to some disparity with respect to methods that are feasible for integration and those that are not. Fortunately we can also find many promising hardware realizations that do allow the acceleration or an increase efficiency for these decoding methods. Although the more progressive deep learning methods still struggle with finding compact configurations [^47] initial results appear promising with respect to power efficiency [^48] due to digital scaling. However this is a common trend among integrated classifiers where power dissipation is on the order of several microwatt but due to complexity such a system requires several mm\\(^2\\) of silicon area for operating on tens of channels [^49] [^129]\cite{folding_}.

{{< figure src="literature/lfpcor.pdf" title="Figure 12:  Extracted correlation in local field potentials for different frequency bands in the human superior temporal gyrus." width="500" >}}


While these methods represent a corner stone for BMIs, it can be argued that carefully accounting for the spacial distribution of neural activity within brain tissue plays a much more significant role towards information extraction than the intricacy of the decoding method. In fact over the past decade, while we have been able to record from many more neurons and use more advanced processing, the rate of information extracted from neural recording has only marginally doubled to 2 bits per second [^51]. In fact this paper argues that if adjustment of electrode positioning is allowed these rates can be fine tuned to achieve much better information rates experimentally. This is still a significant improvement over non-invasive recording that is generally limited to less than 0.5 bits per second. A main consideration is illustrated in Figure 12 where low frequency neural activity are spatially correlated due to the propagation of local field activity [^52]. Implantable devices need careful consideration towards electrode distribution to prevent high correlation in recorded data. These physiological parameters are highly varied in different sections of the brain and the motor cortex in particular exhibits high single unit correlations that impedes effective recording [^53]. As such electrode distribution across the cortex of the brain is revealing to be critical aspect to implantation and approaching a more spatially distributed system design.

With that in mind we can interpret the current trend for monolithic integration of active electronics and neural electrodes. Fundamentally we know that in order to enhance the basic tasks seen in BMI experiments, a significantly larger number of neurons may be needed for recording. This is both from a reliability point of view as neurons will 'drop out' as tissue ages and inferring more degrees of freedom requires even better signal integrity. Moreover we are not definite in our current understanding of information encoding in relation to the anatomy of the brain. However scaling the current paradigm for neural recording platform will not allow implantation of micro-wires with external recording for very high channel counts. Both in terms of surgical feasibility and chronic stability of the system. The use of silicon probes with integrated CMOS devices have demonstrated superior viability for chronic implants with high density electrodes, flexible structures, drug delivery [^54], and hermetically sealed micro-packaging [^55]. In extension these devices are significantly more scalable due to wireless capability and on-chip compression or data analysis which can be attributed to translating advancements in system integration. In particular the fine control over micro-fabrication structural or chemical composition is enabling chronic stability with less abrasive lesion when inserted into neural tissue.

{{< figure src="literature/probe1.pdf}" width="500" >}}
{{< figure src="literature/probe2.pdf}" title="Figure 13: " width="500" >}}


Figure 13 shows the structure of current active probe technology where circuits can be integrated underneath the distributed array of contacts that are exposed to the tissue [^56]. Such a shank is capable of monitoring activity from multiple cortical layers of the brain simultaneously corresponding to various structural and functional neurons that exhibit different dynamics at each layer. In fact it typical to see electrode structures use very dense configurations such that we can be selective with regard to which neurons are decoded though electrode proximity. Currently the head stage extruding from the shank is of considerable size due to the contacts to external circuitry and possibly analogue to digital converters. Ideally this can be minimized by redesigning the instrumentation and allowing for only a few contacts that connect to a inductive link. It is important to point out that freely moving cortical probes with a reduced footprint appears to be the most significant factor for preventing haemorrhaging and the formation of scar tissue that impedes chronic utility of such a device[^18]. We can attribute significant improvements in chronic electrode behaviour with functional probes that leverage chemical agents in combination with micro-meter size incisions to reduce tissue damage [^57]. To a certain extent it is beneficial to have active recording electronics to be on the same order of scale as electrode structures. Such that electrodes can form in relatively arbitrary configuration from a fabrication standpoint and our data processing capacity would scale proportional to the number of recording sites in the system.

{{< figure src="literature/chronic_neuron.pdf" title="Figure 14: " width="500" >}}


As illustrated in Figure 14 many of the earlier penetrating electrode structures can experience detrimental loss of recording capacity in chronic settings. The integrity of electrodes over the course of several years is scrutinized by a number of practicalities during and after implantation. Researchers have found effective methods to recover most of the recording activity by adjusting the electrode shank by a few micrometers or introducing neural growth factors after the primary inflammatory response from invasive surgery has passed [^58]. In fact this remains a major challenge for integrated modules because once these are implanted we lose substantial access to manipulate these devices. Many of these techniques must be mediated by accompanied micro-mechanical structures that coordinate with the electronic system. This aspect represents the leading edge of biomedical device integration where chronic solutions still struggle with attempting to achieve a multitude of capabilities beside simply recording activity.

While it is easy to identify the demand for miniaturized packaging with electronic, mechanical and chemical sub-systems that are hermetically sealed for long term stability. The fabrication methods play a major role in enabling wafer-level or scalable fabrication techniques that are a crucial requirement for cost-effective commercialization. Silicon MEMS allow well established techniques to be applied to fabricating medical devices [^59] but also exhibit drawbacks in long term bio-compatibility associated material composition and structural stiffness. Emerging techniques in 3D-printing [^60] or distributed mesh structures [^61] may address these challenges but have yet to be evaluated with respect to long-term stability to the same extent that we understand the failure modes in silicon MEMS structures.

# 9 Integrated Recording Systems



Here we shall discuss the novelties presented recent publications to review some of the typical system level design considerations. These works present state-of-the-art specifically in the context of fully integrated systems. This implies that the design considers a multitude of functionalities simultaneously to enable isolated operation for implantation.

## 10 Power Density Target for High Channel Count Recording



The trend towards increased recording capacity emphasises the importance for careful sensor design that maintains adequate thermal dissipation. Particularly when current systems extensively perform processing on chip. It remains to be the case that electrode configurations like the Utah array [^62] are distributed over a volume of cortex while sensing take place on a two dimensional array of instrumentation circuits. Clearly fabrication technologies could provide 3D integration of sensor circuits. However this may actually exhibit worse thermal capacity than 2D integration due to reduced surface area per recording unit. The key requirement is then that integrated devices should realize very high 2D density in order to probe the different layers & columns of cortical tissue.

{{< figure src="literature/sys_density.pdf}" title="Figure 15: System power density with respect to sensing area for state of the art recording systems." width="500" >}}
%

In order to reveal the challenge of managing thermal capacity experienced by state of the art recording systems we have surveyed a number of sensor systems published over the past 5 years. This is summarized in Figure 15 which illustrates how well high density recording is achieved with respect to the thermal budget of 80mW/cm²[^68]. In particular the system power density is considered with respect to the sensor density. The power density is evaluated in terms of the total system power dissipation and the fabricated silicon die size which typically dissipates its heat into the surrounding tissue. On the other hand the sensor size is taken with respect to the size of integrated electrode pitch or the size of the corresponding instrumentation circuits in order to emulate the achievable electrode pitch.

Probably the most interesting aspect of this depiction is the constraint imposed by the thermal noise limit. This results from the minimum current dissipation from each sensing circuit in order to achieve 5\mmu V<sub>rms<sub>  input referred noise given a 5 kHz bandwidth. A strict amount of power needs to be dissipated irrespective of the instrumentation size resulting in a power density inversely proportional to sensor area. The closer a system is to this limit the better the NEF it will exhibit. Unless the supply voltage, noise requirement, or bandwidth is readjusted the system power density cannot fall below this limit. As a consequence, managing the thermal budget is an imperative design consideration for future systems that target extreme miniaturization. This is usually required in order to minimize device impact on biological tissues. For such a scenario, reducing the acquisition bandwidth may become a predominant reason for using LFP recordings over spiking activity. This could be the only way to allow several thousand channels to be integrated onto a sub-millimetre size CMOS device without thermal concerns.

The flicker noise sources for active readout transistors also plays an important role that can impair such achievements. If we assume transistors are equal in size to that of the sensing area then it should be expected that below a certain size the flicker components inhibit signal detection. Conventional readout topologies can not achieve very high densities due to flicker noise if chopping or electrode multiplexing techniques are not utilized. However such structures guarantee DC blocking behaviour which is desirable for safety regulations. It is well known that chopper instrumentation can achieve substantially smaller configurations but degrades instrumentation input impedance [^69]. The system in [^70] shows how the use of chopping can achieve 50\mmu m electrode pitch for exceptional spacial resolution with 768 active recording channels. This particular configuration performs quantization at the sensor interface using a ramp ADC and a open loop amplifying structure to minimize the number of analogue components in the system. A similar structure is employed in [^66] with the addition of digital feedback in order to introduce high-pass filtering behaviour. This key modification allows robust in-vivo recording that is not impaired by electrode drift or large fluctuation in local field potentials that are typically not present en-vitro.

Another means to accommodate higher sensing densities is achieved by actively multiplexing the electrode array and only selecting the most informative electrode locations for the decoding task. This allows the work in [^67] to interface over 26 k electrodes while simultaneously recording from 1024 units for the en-vitro study of cell cultures. By embedding SRAM memory cells within the electrode switch matrix this system presents a highly versatile MEA platform that can perform extensive signal conditioning. The main challenge is that the system complexity results in a 76mm² die size which is difficult to translate towards an implantable solution. For this reason the work in [^71] focuses explicitly using a silicon probe as substrate to allow 52 simultaneous recording channels from 455 electrodes. This approach seems to be one of the most promising for future BMI systems as the electrodes can be fabricated together with the electronics using well established microfabrication [^72].

In addition to these high density recording systems a number of promising circuit techniques have been proposed that may allow considerable improvements in performance. For instance the application of bulk switching in [^73] is capable of reducing flicker noise without sacrificing the DC blocking characteristics. On the other hand [^74] suggests removing the capacitive coupling structure altogether by extensively utilizing digital feedback which could achieve very high recording densities if electrode multiplexing is also incorporated. Overall this trend towards higher recording densities is expected to remain a sustained effort where both fabrication and circuit techniques will play a key role for miniaturization.


Table 2: Performance specifications for integrated neural instrumentation systems found in the literature. \\({\dagger}\\) integrated power management, \\({\star}\\) integrated silicon probe, \\({\triangle}\\) commercialized system, \\({\diamond}\\) integrated stimulator, \\(\circ\\) integrated chemical readout.
|	Reference  |            |Intan [^75] |Yoon [^76] |Je [^77] |Gielen [^71] |Rabaey [^64] |Chan [^63] |
|----|----|----|----|----|----|----|----|
|	Year       |                     | 2012           | 2012          | 2013          | 2014          | 2015          | 2016          |
|	Technology | [nm]            | -              | 250           | 180           | 180           | 65            | 180           |
|	Supply     | [V]             | 3.3            | 0.9           | 0.45          | 1.8           | 1             | 1.8           |
|	Power      | [(\mu)W]        | 830            | 3.96          | 0.96          | 27.8          | 3.6           | 9.1           |
|	Channels   |                     | 64             | 16            | 100           | 455           | 64            | 200           |
|	Area       | [mm(^2)]        | 0.47           | 1.56          | 0.25          | 0.19          | 0.075         | 0.067         |
|	Bandwidth  | [Hz]            | 10k            | 11k           | 10k           | 6k            | 8k            | 10k           |
|	Highpass   | [Hz]            | 0.1-1k         | 0.1-1.2k      | 0.25          | 1-500         | 10-1k         | 0.1           |
|	Noise      | [$\mu V_{rms}$] | 2.4            | 4.8           | 3.8           | 3.2           | 7.5           | 4.07          |
|	Note       |                     | ({\triangle})   |   ({\star})    | ({\dagger})  | ({\star})   | ${\dagger   \diamond}$| ({\circ})  |

Here we highlight the digital electro physiology interface chips provided by Intan technologies as one of the few commercialized integrated instrumentation systems [^75]. These chips are the base line for numerous other advanced neural sensors. The mixed signal architecture it self can still be identified in newer systems. The on-chip configuration is relatively straightforward where there are 16-64 channels with differential inputs that are amplified and filtered by \\(3^{rd}\\) order low-pass filter. In addition to a combination of \\(1^{st}\\) order analogue and \\(1^{st}\\) order digital high-pass filter are used to reject low-frequency content. The digital back-end directly clocks the data converter as slave to sample the various channels. The key component to these systems is the robust simplicity and guided application that has accelerated the research for many groups.

{{< figure src="literature/R2_IC.pdf}" width="500" >}}
{{< figure src="literature/R2_SYS.pdf}" title="Figure 16: " width="500" >}}


The multi channel device in [^76] is some of the earlier work that focuses explicitly on the miniaturization of analogue recording. This work was later improved upon in [^77] where a dual sample and hold structure was proposed to mitigate the class-A power-bandwidth trade off associated with the buffer driving the ADC by using two separate capacitor arrays. This system can be seen in Figure 16. More importantly this system introduced on-chip power management to that would allow a telemetry module to power the implant. There is also an attempt here for using the dynamic range at different supply voltages more effectively to marginally reduce the system power budget. By using a charge pump to drive the supply on stages that have a large output swing the low voltage component have reduced power requirement.

{{< figure src="literature/R9_IC.pdf}" width="500" >}}
{{< figure src="literature/R9_SYS.pdf}" title="Figure 17: " width="500" >}}


The authors of [^71] introduce the conceptual hurdles and advantages of using a fully integrated active probe that is fabricated by post processing standard CMOS wafers. This system can be seen in Figure 17. Here the active electrodes are demonstrated to deal with the cross-coupling of high density electrode configuration and enabling a significant amount of multiplexing for electrode selection. Because we see the use of analogue voltage transmission across the chip the discussion addresses a number of limitations due to the limited drive capability of the active electrode structure. We may be quick to suggest alternative structures that does not suffer from such complications but it is difficult to avoid open-loop behaviour will not allow good linearity or matching drawbacks.

{{< figure src="literature/R11_IC.pdf}" width="500" >}}
{{< figure src="literature/R11_SYS.pdf}" title="Figure 18: " width="500" >}}


The work in [^65] exemplifies an alternative to closed loop amplifier structures by performing direct quantization. This system can be seen in Figure 18. Similar to oversampling data converters this approach resolves a number of issues like the limited linearity of analogue blocks or variance in their characteristics. However these complications can now be seen in the feedback structure where the digital to analogue conversion requires fine linearity calibration in the feedback and most of the digital processing has a considerable dynamic range. This approach does well to leverage deep sub-micron CMOS.

{{< figure src="literature/R7_IC.pdf}" width="500" >}}
{{< figure src="literature/R7_SYS.pdf}" title="Figure 19: " width="500" >}}


The system presented in [^64] by the same authors as  is exceptional because it demonstrated a fully integrated system on chip solution that can perform closed loop stimulation while processing neural activity. This system can be seen in Figure 19. Moreover the system integrates power regulation that adaptively scales the stimulator supply in order to maximize the efficiency of current stimulation. The embedded digital processing is capable of extracting spikes that are detected by a non-linear energy operator and evaluate long term firing rates as a form of data compression. Moreover the 65 nm CMOS technology allows this system to achieve a respectable power budget while performing extensive digital processing.

\TFigure{
	\centering
	\subfigure[Fabricated device in 180 nm CMOS.]{\includegraphics[height=7cm]{literature/R6_IC.pdf}}

	\subfigure[Integrated system architecture.]{\includegraphics[height=6cm]{literature/R6_SYS.pdf}}
	\caption[Neural recording system from the literature showing the fabricated and system level implementation.]{Proposed neural recording system from [^63] showing the fabricated and system level implementation.}
	\label{fig:LT_R6}
}

The acquisition platform in [^63] merges the capability to perform electrical and chemical sensing of biological cultures. This system can be seen in Figure \ref{fig:LT_R6}. The discussion on the different sensing modes motivates discreet-time biasing of the current feedback. This is followed by careful transistor sizing accordance to the detailed noise analysis that attempts to maximize the power efficiency. This work also reviews a number of other works with respect to their performance and draws our attention towards the difficulty of achieving good linearity and input impedance.

Generally we find that systems published in the recent literature are pressed to achieve good power efficiency in the analogue and digital domain because this component are well understood as a critical factor. The focus for innovation is typically the introduction integrating more axillary circuits that improve the viability for wireless implantation and wafer-level fabrication with electrodes. We do find that typically the compactness is not viewed as stringent because it is presumed to be largely technology dependent. Moreover integrated processing methods are strictly evaluated with respect to their algorithmic complexity and not the memory requirements which are equally scarce resources.

The fully integrated realization of neuromodulation ICs has been an outstanding endeavour for a number of research efforts that is rapidly becoming more successful. As demonstrated by Medtronic's pioneering work [^78] that is one of the few to realize neuromodulation devices with FDA approval. Similar closed loop systems extensively use LFP signals for seizure prevention have been particularly successful at realizing integrated solutions. For instance the system in [^79] uses extensive segregation of different LFP frequency bands from 0.5 to 30 Hz as features which allows a support vector machine in the digital baseband to to perform classification on EEG activity. While this is not quite as invasive a solution as the Medtronic device this work illustrates that the processing architecture plays a key role in on-chip resource requirements. Generally the level of invasiveness will reflect in the system's latency to detect events in neural activity while exhibiting more challenging instrumentation requirements for EEG systems when compared to ECoG or intracortical recordings. In fact the newer implementation in [^80] uses a non-linear basis SVM engine to improve its hardware efficiency resulting in an accuracy improvement from 84% to 95%.

To some extent the integrated form factor allows these SOCs to deliver substantially increased sensing & stimulation capabilities when compared to benchtop alternatives. In fact the overall experimental complexity is considerably less and environmental noise sources are less likely to perturb an integrated system. For instance the system in [^81] uses 64 recording and stimulation channels for cortically implanted electrode arrays to deliver electrical stimulation therapy based on closed loop control. This type of active neuromodulation can improve clinical efficacy in freely moving rats. Earlier results [^82] indicated that such an approach can reduce epileptic seizures by 90% in addition to improving chronic viability owning to a reduced implant size and wireless capability. This particular system uses phase synchrony in specific LFP frequency bands to trigger current mode stimulation with minimal feedback latency. A similar wireless system in [^83] also uses LFP energies to deliver stimulation but proposes to take advantage of log-based signal encoding in neural activity to improve energy efficiency. This is just one of many examples where the physiology of neural activity can be used to allow more effective processing methods. The target application here is using deep brain stimulation to treat essential tremor and Parkinson's disease using a programmable PI controller.

An isolated number of works have used neural spiking activity to realize closed loop stimulation control of neural activity on SOC platforms. This is possibly due to the large stimulation artefacts that can disturb the instrumentation front end but also because most target applications are directed at external motor control. The system in [^84] suggests adiabatic charge-recycling may potentially realize better efficiencies. However the recorded spike rates are not directly used to adjust the stimulation pattern without off-chip intervention. On that note the system in [^85] utilizes the spiking rates from classified neurons to infer bladder volume and thereby provide a well informed condition for stimulation. This should indicate that peripheral nerve control is more adequate for this class of devices simply due to the lack of information in local field fluctuations. Instead chemical measures or the associated nerve activity is used for closed loop control.

## 11  Emerging Technologies



It is becoming apparent that increasing the capacity current BMIs requires us to find more efficient means to perform signal extraction as well as finding more effective interfacing strategies. For this reason we will highlight a few of the promising technologies that will hopefully make substantially more effective systems in the future.

## 12 Advanced CMOS Technologies



A number of recent BMI publications show a growing interest for using advanced CMOS technologies in order to accommodate more digital processing capabilities on chip. This is particularly relevant for closed loop neuromodulation that needs more sophisticated diagnostics to perform therapeutic feedback. To some extent the high channel count recording systems also necessitate extensive processing for various types of signal compression. As a result there are a number of opportunities associated with using nano metre CMOS processes. For example the 0.25 V neural processor in [^86] is able to perform feature extraction on quantized recordings with exceptional power efficiency in part due to the 65 nm technology. Combining this with existing sensor interfaces that operate at very low supply voltages [^87] [^88] may result in an order of magnitude improvement in power dissipation when compared to previously proposed systems.

It is important to point out that there are other challenges that prevent conventional instrumentation structures to deliver precise sensing at these technology nodes. Particularly when attempting to achieve a compact configuration with good linearity at these reduced supply voltages[^89]. It should not be surprising that the use of oscillators have been particularly successful to leverage the digital design style [^90]. Our group recently demonstrated that oscillator based structures, while high digital in nature, can allow exceptional performance for filtering time domain signals [^91]. In fact the concept of encoding signals in the time domain has been proposed in a number of recent works [^92] [^93] [^94]. This is motivated by asynchronous processing capabilities for sparse neural activity that could drastically reduce power dissipation [^95]. However this is still an ongoing effort where the current realizations show exceptional dynamic range but have not yet been able to demonstrate the same noise efficiency conventional methods. This is partly because such benefits can only be realized when both instrumentation and signal processing is performed using the time domain signal modality. Some further argument can be made that the reduced parasitics and smaller geometries from this trend make chopper circuits substantially more viable. This is because the input capacitance can be reduced if the closed loop gain is maintained relatively large. Such a reduction should translate towards boosting the sensor's input impedance to hundreds of mega ohm. Again this works in favour of VCO topologies because they inherently exhibit excessive open-loop gain.

## 13 Chemical Sensing



In addition to the electrical activity that can be recorded from neural populations, chemical markers such as dopamine concentrations can play a key role in utilizing neurochemistry to refine the diagnostic fidelity of BMIs. The neurochemostat is a recent innovation that allows a means to perform closed-loop regulation of endogenous neurotransmitters [^96]. Because a number of neuropathologies relate explicitly to deficiencies in specific neurotransmitters this development can enable new therapeutic strategies that probe different pathways using rich neurochemistry. While chemical sensors face other challenges associated to the electrode composition & interface that can can degrade sensitivity in chronic settings [^97]. However there are a number of promising means to prevent such degradation such as anti-fouling coatings [^98]. Moreover a number of existing sensor platforms already allow simultaneous sensing of electrical and chemical activity with hundreds of different channels to study neurodegenerative diseases [^99].


## 14 Optical Sensing



The use of optics in implantable sensors is possibly one of the newer themes in brain machine interfaces as a result of the enabling success in optogenetics. Such sensors may provide essential clinical tools to precisely guide neurosurgery as well as new high resolution imaging tools for brain structures [^100]. That said there are also efforts to perform label-free imaging sensors that use the polarization of reflected light which does not require optogenetic transfection [^101]. While there is a great amount of functional flexibility, implantable optics face a demanding challenge in relation to developing compact devices. This is exemplified by the implantable prototype in [^102] which uses a coupled fibre to deliver optical stimulation from a battery powered system. This is primarily an outstanding challenge for recording activity from large volumes [^103] that has the potential to be integrated along side more conventional recording circuits [^70].

# 15 Summary



In hindsight to the trends in BMI innovation there is an definite expectation with regard to seeing more integrated probes with better processing capacity. Particularly because active probe integration solves many problems associated with electrode configuration and scalable data processing that is not limited by communication links. In some cases like closed loop stimulation it may even be necessary in order to avoid inconsistent signal latency which neural plasticity is highly sensitive to[^104]. Moreover there are not many clear answers towards optimizing area and power of analogue instrumentation. Particularly when dealing with noise limited systems. It is more typical to see strategies proposed for solving problems that are emergent from the implementation which is difficult to isolate from the fundamental aspects for signal amplification in a well defined manner. We also note that the number of neural recording system with integrated processing is very limited in terms of reconfigurability. In contrast to the work done with image processing ASICs that allow very efficient acceleration of various algorithms [^108][^107][^106][^105]. The reconciliation of software and algorithm developments is an important aspect which these specialized systems have yet to accommodate.


# 16 Neural Recording Front End Design



This chapter focuses on the multitude of questions associated with the mixed signal design for multi channel integrated neural recording systems. As a result, a significant section will be directed at developing an abstract understanding of how design parameters influence the various design challenges. This discussion will clarify the key limitations for these systems and propose how they can be mitigated or efficiently designed for. In the scope of integrating a large number of recording channels together, clearly understanding how each resource trades for another is crucial for optimizing a complex system. Optimization methods found in the literature typically assume a certain configuration which limits to what extent improvements can be made [^109]. However here we specifically identify abstractions that allow us to consider the impact of different topologies and filter structures simultaneously. This should enable a much boarder sense of optimization that will reflect in the improved performance characteristics demonstrated here.

We will focus on elaborately evaluating the dominant resource requirements with respect to noise, mismatch, quantization, and functional aspects for signal conditioning together that is mostly implementation independent. In addition we propose several circuit implementations based on this analysis that present highly efficient and compact instrumentation. The corresponding abstractions that we use attempt to realize clarity respect to underlying dependencies. This should allow better analytic models that make the limiting factors appear obvious and reveal means to circumvent specific constraints with alternative techniques. For example we may be interested to know when it is worthwhile to put certain functions in the digital domain in terms of the CMOS technology parameters. Approaching the ideal instrumentation structure in such a scenario remains highly desirable for constrained applications. Thus conforming to the technology parameters could reveal that conventional methods do not deliver the most effective solution.

The chapter is organized as follows; Section 17 describes the general problem statement related to the analogue front end which is followed by the associated amplifier design considerations in Section 19. The method for improving the analogue to digital conversion is outlined in Section \ref{ch:T1_converter}. These results are then collected in Section \ref{ch:T1_model} to evaluate the impact of system level parameters as a function of resource requirements.

\ifbrief

\else

# 17 Architecture for Neural instrumentation



The analogue dimension of neural recording system can be broken down into two objectives for signal conditioning that will maximize the performance of the proceeding digital signal processing. The first is related to getting adequate signal quantization by amplifying the signals to full input range of the data converter without corrupting the signal of interest. The second objective is performing some kind of filtering that removes noisy or irrelevant components in the recording and only captures the relevant signals of interest.

{{< figure src="technical_1/T1_SIG_Spectrum.pdf" title="Figure 20: Illustration of the spectral power density characteristic for a typical neural recording with the associated frequency bins. " width="500" >}}


As depicted in Figure 20, the input spectrum of a typical \text{in-vivo} electrode recording can be classified using a few frequency bands. The energy from extracellular spiking activity is primarily concentrated around \\(300 Hz\\) to \\(6 kHz\\) and is characteristically intermittent resulting in a distinct difference between the average and instantaneous spectral power [^110]. This characteristic is also present in the LFP band to a lesser extent. From an electrical standpoint the design constraints are derived from the tolerated noise levels in each frequency band to maintain a proper signal to noise ratio. As a consequence it important to specify the signal to noise ratio in terms of noise density opposed to integrated noise figures as digital processing accuracy is not limited by the later term. Here we should also note that the electrode spectral noise power $N^2_{electrode} = 4 kT R_{en} \Delta f$ depends on the resistive component of the electrode impedance. This is typically matched by that of the amplifier noise characteristic \\(N_{amp}\\) so that no excess power is wasted and is expressed in terms of the electrode resistance \\(R_{en}\\), Boltzmann energy \\(kT\\), and the frequencies of interest $\Delta f$.


## 18 Instrumentation Requirements



This kind of electrical sensing can be broken down in the a number of system blocks each of which perform an essential operation to this process. These are shown in Figure 21 and consist of an amplifier, a filter, a sampler, and a quantizer. Occasionally one circuit can combine multiple of these operations together depending on the construction. Table 3 presents the overall performance requirements that should be demonstrated when these components are integrated together. These are also the specifications that we will target as the design is being considered in the following discussion. The reasoning behind these specific requirements are mainly related to conventional signal acquisition given the bandwidth and noise requirements. Moreover these seem to be sufficient for most decoding/characterization methods hence similar figures can be found in most BMI publications.

{{< figure src="technical_1/ISYS.pdf" title="Figure 21: " width="500" >}}


Table 3: Summary of the target specifications for the analogue instrumentation system.
|	Parameter      | Symbol     		 | Specification    |
|----|----|----|
|    	Integrated Channels | | 64    	|
|	Supply Voltage | (V_{DD})| (<)1.8V |
|	Power Dissipation | (P_{SYS}) | (<)5 (\mu)W |
|    	Diff. Signal |  | 5 (\mu) - 5 mVpp 	|
|    	Common Signal |  | 50 mVpp 	|
|	CMRR/PSRR | | (>)80 dB			|
|	Input Referred Noise | (e^2_{in}) | (<)5 (\mu)Vrms |
|	Total Gain | (A_T) | (>)40 dB 	|
|	THD at max input | | (>)40 dB  |
|	3dB Bandwidth | (f_{3dB}) | 6 kHz  	|
|	High pass frequency | (f_{hp}) | (<)1 Hz |
|    	Sampling rate | (f_{smp}) | 25 kS/s 	|
|	Input Impedance | (R_{IN}) | (>)50$  M \Omega$ @( 1 )kHz |
|	ADC Resolution | (ENOB) | 12 bits |
|	Active Area | | 0.01 mm(^2) |


# 19 Amplifier Principles for Miniaturization




{{< figure src="technical_1/Harrison.pdf" title="Figure 22: " width="500" >}}


The principle design considerations for neural instrumentation have been well established particularly with regard to the Harrison topology [^111] that been widely adopted in many systems and shown in Figure 22. Objectively the optimization techniques have become both more specialized and specific for maximizing the average signal to noise ratio in the LFP or EAP bandwidth with the absolute minimum power budget. Interestingly due to the use of more advanced CMOS technologies there is a persistent trend towards sub-threshold operation. This is motivated by trading in the excess transistor bandwidth for improved current efficiency that measured in terms of the achieved transconductance per dissipated ampere of current. In fact this is purely a result of maximizing the individual transistor performance with respect to the speed efficiency product [^112]. This is expressed in Eq 4 using \\(f_T\\), \\(U_T\\), \\(v_sat\\), \\(\mu\\) as the transition frequency, thermal voltage, velocity saturation voltage, and carrier mobility respectively.

$$  \max\limits_{IC} \left\lbrace f_{T}   \frac{gm}{I_{DS}} \right\rbrace  = \frac{v_{sat}^2}{4\pi   \mu \eta   U_{T}^2} \: \frac{1}{IC_{max}} \approx \frac{22}{IC_{max}}   \left[ \frac{THz}{V} \right]  Where  IC_{max} = \left( \frac{L_{sat}}{L_{tech}} \right)^2 $$

Here \\(L_{sat}\\) is a technology independent BSIM6 parameter that reflects the impact of ballistic carrier transport during velocity saturation and normalizes the minimum feature length \\(L_{tech}\\) for a specific technology as an effective length. The implication of Equation 4 is that the transistors for optimized low frequency instrumentation amplifiers are exclusively in the sub-threshold regime because \\(f_T\\) is always in excess with respect to the signals of interest. The subthreshold operation results in each transistor's transconductance being defined as $gm = \frac{I_{DS}}{\eta   U_{T}}$ which only depends on drain current. Instead of noise optimization though the overdrive voltage, \\(V_{ov}\\), the topology can only reduce noise by removing non-amplifying transistors or biasing them with reduced drain current when compared to the input transistor(s). This reflects the need for a different design methodology as the input referred contribution is dominated by how the total amplifier current distributed to all the transistors. At least in the small signal sense the key requirement is that the amplifying transistors dissipate all the current while biasing/non-amplifying transistors dissipate relatively very little.

In principle due to the under-determined nature of transistor level design the optimization methodology is initially constrained by one of the most important objective characteristics. This could be low noise, wide bandwidth, good linearity, etc. Hence this discussion will digress by distinguishing the design considerations for noise or bandwidth limited amplifiers as separate cases. This should reveal some key relations with respect how power efficiency is achieved. For each case we evaluate the implications with respect to different resource requirements.

## 20 Noise limited Amplifiers



This discussion is guided by the leading challenge for instrumentation systems which is maximizing efficiency while maintaining good linearity. For this reason a noise efficiency factor (NEF) was first introduced in [^113] and is expressed in Equation 5.

$$  NEF^2 = e^2_{in} \frac{I_{tot}}{ U_T   4kT   \omega_{3db}} $$

This figure represents a normalized efficiency or in other words it evaluates how much extra current is dissipated by a particular circuit when compared to an ideal bipolar junction transistor for the same noise performance. Here \\(e^2_{in}\\), \\(I_{tot}\\) and \\(\omega_{3db}\\) represent the input referred noise power, the total current dissipation and the -3dB bandwidth in radians respectively. NEF reflects how well a particular topology achieves efficient amplification for a particular noise floor and thus it inherently trades off with a multitude of other parameters. Here we shall use it as design parameter that reflects the chosen transistor level topology. With this in mind, we propose the following reformulation from Equation 5:

$$  e^2_{in} = \frac{kT}{C} \frac{NEF^2}{\eta   A_{cl}} \frac{I_{in}}{I_{tot}}  \text{where}  C = \frac{gm}{\omega_{3db}   A_{cl}}  \text{and}  gm=\frac{I_{in}}{\eta   U_T} $$

This result leads to:

$$  gm = \omega_{3db} \frac{kT}{e^2_{in}} \frac{\zeta}{\eta}  Equivalently  I_{in} = \omega_{3db} \frac{q   U_T^2}{e^2_{in}}   \zeta   \text{where}   \zeta = NEF^2 \frac{I_{in}}{I_{tot}} $$

Note that this relation is exclusive to noise limited characteristics and implies nothing with regard to the output load or linearity conditions. Moreover there is a fundamental requirement for transconductance with respect to noise and an implementation related factor \\(\zeta\\). This factor represents the noise efficiency of the topology and the slope factor \\(\eta\\) that tells us about the transistor performance as a fundamental process parameter. Numerous techniques for improving NEF can be found in the literature. As a generalization these can be put into two categories. The first reducing the transconductance of non-signal amplifying transistors using degeneration such that their input referred noise is minimized [^114]. The second approach is AC coupling the amplifier's input signal to biasing transistors such that the total transconductance is increased and the current efficiency is improved. Interestingly because this factor relates to current efficiency the NEF can be smaller than 1 or exceed the efficiency of a BJT using a stacked mixer structure that reuses the same biasing current for multiple amplifiers [^115]. This hints at the fact that NEF should be normalized to the voltage supply but in some sense these structures trade off dynamic range for power efficiency. Theoretical NEF figures for some of the primitive low noise topologies are listed in Table 4 assuming biasing transistors have negligible contribution and taking \\(V_{th}\\) as the NMOS & PMOS threshold voltage.

Table 4: Theoretical figures for NEF for various amplifier topologies. \\(^\star\\) N is the number of stages sharing the structure.
|	Topology           		 | NEF                           	   | Minimum (Vdd)   			| Reference          	|
|----|----|----|----|
|	Single Transistor  		 | $\eta $                         	   | (V_{th})   				|     -              	|
|	Differential Pair  	 	 | $\eta   √{2}$                  | $V_{ds} + V_{th}$			| [^116]  		|
|	Complementary Pair 		 | $\eta $                             | $2   V_{th}+2   V_{ds}$	| [^117]  	|
|	Common Reference(^\star)    | $ \eta √{\frac{1+N}{N}}$     | $V_{ds} + V_{th}$			| [^118]     	|
|	Common Bias(^\star)         | $ \eta √{\frac{2}{N}}$       | $(1+N)   V_{ds} + V_{th}$	| [^115]     	|


These relations highlight the fact NEF primarily dependent on the chosen topology and less sensitive to the actual transistor design after optimization. Choosing a topology for the instrumentation amplifier with respect to its ideal NEF performance is significantly more effective than starting with a particular structure and introducing resistive degeneration on transistors that should not contribute noise.

Also notice that the expression for noise in Equation 6 only has one degree of freedom and that is the ratio between the closed loop gain and capacitive load of the amplifier. This implies the 3dB bandwidth of the amplifier is fixed but its unity gain frequency is arbitrary. In fact by satisfying the relation for Equation 7 it is automatically the case the the equivalent noise density requirement is also satisfied. This is significant because we could allow the first stage to provide wide band gain and rely on a second stage to perform filtering. The second stage will have a capacitor gain product that is \\(A_1^2\\) times smaller than if the fist stage had to perform filtering. This can has a large impact on analogue circuit area that is typically dominated by capacitors used for filtering and setting closed loop gain.

{{< figure src="technical_1/flickker.png" title="Figure 23: " width="500" >}}


So far we have only considered the implication thermal noise requirements on the design. We must also address the flicker noise sources because neural signals have a lot of low frequency content. Moreover because flicker noise sources concentrate the noise power at the lower frequencies, the total noise profile inside the LFP frequency band can be dominated by this type of noise. The nature of flicker noise from transistor physics can be due to a number of phenomena; mobility fluctuation $\Delta \mu$, carrier density fluctuation $\Delta N$, and changes in access resistances $\Delta R$. Each of these phenomena will exhibit a \\(1/f\\) frequency dependence when computing the input referred power spectrum. Typically for a given inversion coefficient IC only one of these phenomena will dominate the overall noise characteristic of a transistor. This is illustrated in Figure 23 which shows that $\Delta N$ is typically the leading cause for flicker noise generated additively to the drain current. IC is a factor that indicates to what extent a transistor is operating in the subthreshold region by using the definition IC=I<sub>D<sub>/($2\mu   C_{ox}   W/L   U^2_T$). This uses The more general parameters \\(q\\), \\(W\\), \\(L\\), \\(C_{ox}\\) that represent electron charge, transistor width, transistor length, and gate oxide sheet capacitance respectively. The region of interest for biomedical circuits is typically when \\(IC<1\\) which exhibits good current efficiency and subthreshold operation. The phenomenological model corresponding to carrier density fluctuation $\Delta N$ component is expressed in Equation 8 after being referred to the transistor gate as an equivalent voltage noise density [^119].

$$  e^2_{fl}   \Delta f = \frac{q^2   kT   \lambda   N_T}{W L   C^2_{ox}   f} \cdot K_{G}  \text{where}  K_{G} \approx (1 + \frac{\alpha   \mu}{2})^2  \text{for}  IC < 1 $$

Here \\(\alpha\\) and \\(\lambda\\) represent the coulomb scattering coefficient and tunnelling attenuation distance respectively. Notice that this expression has relatively weak biasing dependency in weak inversion contrast to the strong inversion region as shown in Figure 23. This trend follows very closely to the \\((gm/I_D)^2\\) characteristic which implies a fixed SNR for varying IC. The parameter \\(N_T\\) reflects the density of trapped charges at the oxide interface inside the transistor's conducting channel. Whether this parameter is consistent across various technology nodes is naturally put into question [^120] but similarly there is evidence supporting that indeed this factor is process independent [^121]. Now we should keep in mind that increasing the input transistor size will accommodate lower flicker noise but also result in increased noise. This is because of the signal loss when coupling \\(C_{in}\\) to \\(C_{fb}\\) that is loaded by the parasitic input capacitance of the amplifier \\(C_{g}\\) (see Figure 22). Keeping the ratio \\(C_{g}/C_{fb}\\) fixed as a \\(\delta\\), we can express the required input capacitance in Equation 9 in terms of general amplifier requirements using \\(A_{cl}\\), \\(K_F\\), \\(f_{cor}\\) as the closed loop gain, flicker charge density, corner frequency respectively.

$$  C_{in} = \delta A_{cl}   C_{g} = \frac{3}{4}  \delta   A_{cl}   C_{ox}   W L = \frac{3}{4} \frac{K_F   A_{cl}  \delta  }{C_{ox}   e^2_{in}   f_{cor}}  \text{where}  K_F = q^2   kT \lambda   N_T   K_G $$

This expression indicates that attempting to achieve all desirable characteristics; small \\(e^2_{in}\\), small \\(f_{cor}\\), large \\(A_{cl}\\) simultaneously in a single amplifier structure comes at the cost of a very large input capacitance that scales proportionally to all factors. This representation suggests the Harrison topology has limited flexibility for improving input capacitance as the only solution appears to be minimising \\(\frac{KF}{C_{ox}}\\) through CMOS process selection. Moreover \\(\delta\\) cannot be made arability small as it will more typically be bounded by the minimum feedback capacitor \\(C_{fb}\\). This need to be large enough to set the high pass pole location at sufficiently small frequency to prevent the resistor \\(R_{fb}\\) from introducing noise inside the signal band which has a integrated power of \\(\frac{kT}{C_{fb}}\\) [^111]. Not to mention that the resulting size of the input transistors can be very large for this particular topology.

## 21 Chopper Stabilized Amplifiers



Alternatively we can apply chopping techniques to deal with these noise requirements which is used extensively in bio-signal instrumentation systems [^69]. By up modulating the signal to a higher frequency before amplification, the flicker noise is added to the usual near-DC band which no longer coincides with out input signal. The output is then demodulated to recover the input. The difference is that the flicker components now lie at the chopper frequency \\(f_{chp}\\) which is typically out of band and can be rejected easily. This eliminates the requirements from Eq 9 on the input capacitance and shifts the focus to rejecting up modulated aggressors at higher frequencies. We suggest using keeping the sampling and chopper frequency coherent because it allows low order FIR filter reject all up modulated harmonics. For instance by chopping at the half the Nyquist frequency (\\(f_s/2\\)) or odd multiples of it (i.e. \\([2n+1] f_s/2\\) $|$ $n \in \mathbb{Z}$) will fold chopper harmonics onto \\(f_s/2\\). The resulting filter are quite relaxed because of the large fractional bandwidth in the transition band that separates our signal bandwidth \\(f_{3dB}\\) from \\(f_{chop}\\). In this particular case we employ a sampling frequency of \\(25 kS/s\\) and use a chopping frequency at \\(37.5 kHz\\) to achieve this functionality [^122]. Conveniently any common mode signals from the sensor or analogue supplies are also rejected using this configuration because they will appear at the chopper frequency.

In addition to basic chopping functionality, the performance can be further improved by providing closed loop feedback to actively cancel aggressors on top of filtering the resulting up modulated aggressors. This can be achieved in multiple ways and in some cases could improve linearity. One possible technique is using a DC-servo loop and another is performing ripple rejection both of which remove different components [^123]. Here we will consider the implementation of three such techniques that improve chopping performance that specifically have negligible power and area requirements. The considerations made here will be similar to that of [^124] [^125] but with explicit focus on area reduction.

{{< figure src="technical_1/T1_CAMP.pdf}" width="500" >}}
{{< figure src="technical_1/T1_CAMP_T.pdf}" title="Figure 24: Proposed compact chopper stabilized neural amplifier topology. " width="500" >}}


Figure 24 shows the proposed configuration that promises a significant reduction in input capacitance and the required silicon area. This configuration has two gain stages where the first stage A1 is a wideband low noise stage and the second provides A2 low pass filtering as motivated by Section 20. This enables the rejection of flicker noise from the first stage completely and effectively shifts the corner frequency of the second stage by gain of first stage squared. Moreover this the configuration does not require auxiliary integrators provide feedback on the capacitive feedback network around A1 that would lead to increased complexity.

The pseudo resistor across A1 in this configuration provides closed loop rejection of low frequency noise below the high pass pole with the time constant $\tau_{HP} = C_{F1} R_{HP}$. The noise components in the band from \\(f_{HP}\\) to \\(f_{CHP}\\) will be a mixture of flicker and thermal noise that are up-modulated by the chopper proceeding A1. This is because A1's corner frequency will lie inside of this band after sizing the input transistors such that \\(C_G\\) is about 5% of \\(C_{IN}\\) which usually leads to a target area of about 100 $\mu m^2$.

It is important that the gains of A1 and A2 are carefully selected because this configuration only provides a first order role off in terms of analogue filtering. It could be that \\(f_{CHP}\\) is not sufficiently outside of the \\(6kHz\\) filter bandwidth resulting in some aggressors to appear on the output of A2. For this reason we require an aggressive high pass pole location to minimize this total up modulated power. More specifically we can say that the total noise contribution below the \\(f_{HP}\\) is mainly from \\(R_{HP}\\) which has a noise power of $\frac{kT}{A1^2   C_{F1}}$ when referred to the input of A1. The main concern here is that we have to sacrifice a small amount of dynamic range on A2 to prevent distortion. Although this power is quite limited, we need make sure the FIR filter can reject up-modulated noise components effectively.

In addition we take advantage of the reduced output referred sampling noise a the input of the second stage that scales by \\(f_{3dB}/f_{CHP}\\). This is because most of the sampling noise will lie outside of the filter bandwidth. The size of \\(C_{I2}\\) can be reduced to alleviate the slewing errors due to the band limited behaviour of A1. In addition the parasitics at the output of A1 will pre-charge before \\(C_{I2}\\) is connected reducing the settling error due to the active nodes switching at the input and output.

A common concern for chopper stabilized circuits is the resistive element of each chopper which in this case is seen at the input of the amplifier. This resistance is due to the switching capacitor \\(C_{I1}\\) that is continuously dissipating dynamic current. This can partially be compensated for by performing positive feedback from the output to assist in cancelling the dynamic current through \\(C_{PF}\\) [^123]. However this will rely on the matching of the capacitor ratios $\frac{C_{I1}}{C_{F1}} \frac{C_{I2}}{C_{F2}}$ to be equal to \\(\frac{C_{I1}}{C_{PF}}\\). This can be quite challenging if small configurations are desired that do not need exhaustive calibration. The use of a high precision ADC makes this somewhat easier because the total gain A1\\(\cdot\\)A2 does not need to be as large implies smaller ratios and better matching. Evaluating this resistance in terms of the switching capacitance will result in the expression in Equation 10.

$$  R_{in} = \frac{1}{2 f_{CHP} \cdot (C_{I1} + C_{par} -  \frac{C_{I1}}{C_{F1}} \frac{C_{I2}}{C_{F2}}   C_{PF})} $$

This dependency should indicate that if the dynamic switching current cannot be well matched due to parasitics or variability the next objective would be to reduce the total switching capacitance. From our discussion however it appears that reducing the input capacitance is limited by the psuedo resistive noise that induces aggressors at the chopper frequency. This constraint can be mitigated using a distributed amplifier structure that splits A1 into two identical sections. This should be configured such that the second stage has its high pass pole and corner frequency proportionally larger than the first stage but scaled the gain of the prior stage. However such a topology is more constrained by parasitics that worsen the settling errors in $0.18 \mu m$ CMOS. In addition the poor control of psuedo resistive characteristics does not allow this to be convincing solution [^126]. The feasibility may be more favourable in more advanced technology nodes. Considering a value of \\(1 pF\\) for \\(C_{I1}\\) we expect slightly over \\(20 M\Omega\\) without positive feedback and approximately \\(200 M\Omega\\) with \\(10%\\) matching. This may be acceptable in either cases depending which type of electrode is used but generally any thing above \\(100 M\Omega\\) is satisfactory for most scenarios.


## 22 Bandwidth Limited Amplifiers



Biomedical instrumentation has the advantage that the slowly varying signals prevent most implementations from facing problems due to limited bandwidth. The exception however lies with the stage that drives the input capacitance of the ADC and the settling time during sampling can be quite challenging[^127]. Particularly when multiple channels are multiplexed to the same data converter. In some sense there is an similarity when we look at NEF and bandwidth efficiency because they are strongly dependent on maximizing transconductance efficiency.

$$  FOM   \left[ \frac{MHz \: pF}{mA} \right] = \frac{f_{UGF} \cdot C_{L}}{I_{tot}}  \text{for diff. pair}  FOM = \frac{10^{3}}{4 \pi   \eta U_{T}} $$

{{< figure src="technical_1/MCAmp.pdf" title="Figure 25: " width="500" >}}


Strictly stated in Equation 11, a bandwidth constrained circuit should minimize the total current consumption \\(I_{tot}\\) for a given unity gain bandwidth \\(f_{UGF}\\) and capacitive load \\(C_L\\). It is typical to find dedicated structures out side of the signal processing chain that drive the ADC input capacitance and focus specifically on maximizing the FOM by employing current recycling, adaptive biasing, and positive feedback techniques. The challenge here is efficiently introducing these techniques while also preserving the capability for full output swing, stability and particularly low distortion. The later is likely the most challenging and demands high loop gain that is generally not found in adaptive single pole structures if full output swing is also required. With that said, two stage Miller compensated topologies can provide an excellent solution to this problem because high gain in the second stage will suppress a number nonlinearities excited by the input stage. Further more the capacitive coupling of the output to the input of the second stage implies the settling speed is limited by bandwidth of the second stage. This allows the configuration to simultaneously  provide filtering and settling while sharing many of the biasing and feedback elements. Using the model shown in Figure 25. We can show that sampling induced kick back from the ADC at \\(V_{out}\\) has negligible in pact on internal integration node as it is inversely proportional to the product $A_{cl}\cdot \frac{gm2}{gm1}$ where \\(gm1\\) and \\(gm2\\) are the transconductance of the first and second stage. This is derived from evaluating a step response due to discharging the output load \\(C_{L}\\) which has the Laplace domain response as Equation 12.

$$  H_{step}(s) = \frac{s^2}{s^2 + (\omega_2 - \frac{\omega_1   C_{M}}{A_{cl}   C_{L}} ) s + \frac{\omega_{1} \omega_{2}}{A_{cl}}}  \text{where}  \omega_{1} = \frac{gm_1}{C_{M}} \: \: , \: \: \omega_{2} = \frac{gm_2}{C_{L}} $$

{{< figure src="technical_1/T1_T2AMP.pdf" title="Figure 26: " width="500" >}}


Figure 26 shows the proposed circuit implementation of the two-stage amplifier used inside the second instrumentation stage in Figure 24. This structure has the advantage of providing very high loop gain across the Miller capacitor and allows full output swing due to the positive feed back structures in the current mirrors. The PMOS mirror provides high gain by cancelling the \\(1/gm\\) transresistance of from the diode connected pair leaving the high impedance node and the NMOS mirror provides positive feedback to speed up the transient behaviour on the PMOS side. When this structure provides closed loop gain larger than 20 dB it is sufficient to rely on the NMOS current mirror for stability. In fact this is equivalent to a feed-forward stabilization technique that by passes high frequency signal lag induced by the pole at the PMOS side. However when good phase margin is required at the unity gain frequency stability becomes more stringent. In this case we suggest introducing an additional capacitor across \\(V_n\\) & \\(V_p\\) to realize a zero that cancels the pole in the PMOS branch [^128]. The zero will in fact boost the effective \\(\omega_{2}\\) from $N   M   \frac{gm_{M5}}{C_{L}}$ to $\frac{N   M + M }{2-N}   \frac{gm_{M5}}{C_{L}}$. The factor M in this structure has a rather interesting implication with respect to NEF. If M is large enough this topology will have a NEF equivalent to the complementary structure. However in effect the biasing current of the intermediate branch is reduced when M is large which can move the parasitic poles in side the amplifier bandwidth. The apparent trade off between stability and NEF is unique to this structure but it is not challenging to have M=8 for low power applications.

$$  FOM = \frac{10^3}{4\pi   \eta U_{T}} \cdot \frac{2   C_L }{ C_M   (1+M/K+1/K)} $$

The components that improve bandwidth efficiency are detailed in Equation 13. Referring this back to Equation 6 however implies the noise is dominated by the capacitor that introduces the dominant pole of the system. The observation made here is that unlike the single stage topologies, the two stage configuration can trade off input referred noise for a better speed FOM by adjusting the \\(\frac{C_M}{C_L}\\) ratio. The high level methodology applied here is replacing the \\(C_L\\) with a smaller capacitor that requires less power with the hope that stability can still be maintained by boosting transconductance power with positive feedback and current recycling.

## 23 Circuit Implementation



{{< figure src="technical_1/T1_T1AMP.pdf}" width="500" >}}
{{< figure src="technical_1/AMP_Feedback.pdf}" title="Figure 27: Schematic showing circuit implementation of the proposed compact neural amplifier. " width="500" >}}


Figure 27 shows the transistor level implementation of the topology used in Figure 24. The first gain stage is a highly compact complementary structure that exhibits exceptional noise performance. The second stage transistor implementation is the high gain two-stage topology discussed in Section 22. The variable gain configuration is facilitated by the digital controlled low leakage switches that connect a selected set of capacitors in feedback. This particular configuration provides more generic instrumentation of the 1 Hz to 6 kHz bandwidth. It is well known that the analogue filters introduce frequency dependent group delay near the pole locations which has been shown to degrade processing capabilities of spike sorting techniques [^129]. By placing the high pass pole well inside of the LFP band the spike wave-forms exhibit less distortion due to analogue filtering and is instead filtered using linear phase filters in the digital domain that do not suffer from such drawbacks.

The reset mechanism on instrumentation amplifiers using pseudo-resistive elements is essential. Either during stimulation, start-up, or amplifier saturation the charge across the feedback capacitor must be neutralized before correct operation can begin. This mechanism allows the rejection of various distortion components that would other wise corrupt the latent signal integrity or digital signal processing. However there is an inherent problem with these reset switches due to the parasitic charge injection induced on the intermediate semi-floating nodes. Moreover if these elements are cascaded to increase resistance or dynamic range these sensitive floating nodes are also increased thereby building up more residue charge. A significant amount of charge can introduce a permanent reset artefact after reset as this charge redistributes internally inside the resistor. The proposed solution to this problem is by minimizing the floating nodes and guarding the floating N-Well from injected noise. This should allow  a very large pseudo resistance for a sub-Hz high pass cut off frequency while maintaining exceptional reset characteristics. We minimize the resulting charge residue by absorbing the leaky diode currents and residues into the guarding amplifier. Now there will be some instantaneous off-set as the reset signal injects charge directly onto the feedback capacitor but this can be quite small when using small switches. The drawback here is that there may exist a very slow drift on the order of \\(V/sec\\) from the guarding amplifiers due to $V_{os}   R_{diode}$. But simple digital assistance will suffice in eliminating this concern by periodically resetting the structure and cancelling the residue off-set. This re-introduces the high pass pole at a well defined location depending on the periodicity of the reset signal and reconstructing signal in the digital domain [^130].

{{< figure src="technical_1/AMP_Label.pdf}" width="500" >}}
{{< figure src="technical_1/AMP_Chip.pdf}" title="Figure 28: Physical implementation of amplifier using a 6-metal $0.18   \mu m$ CMOS process measuring $75 \times 82   \mu m^2$ in size. " width="500" >}}


The floor plan for this implementation is annotated in Figure 28. The typical focus for analogue layout is achieving good matching for the input transistors and capacitors to minimise off-set or undesirable signal coupling. In this case the chopper introduces a lot switching that is difficult isolate from the signal so instead we focused on minimising parasitics of the clocked nets. The common mode feedback on the second stage uses a switched capacitor and wide band amplifier to ensure accurate common mode settling without deteriorating linearity. This is important because the ADC can be quite sensitive to the sampled common mode resulting in a reduced precision if there is an unexpected offset on the sampled output. Simulated performance of the implemented topology is shown in Figure 29. This compact configuration can achieve an input referred noise of $5.6 \mu V_{rms}$ over the specified bandwidth with a noise corner frequency of 20 Hz. The performance is detailed with a clear reduction in size can be observed when compared to other chopper systems in Table 5. The total gain is \\(421 V/V\\) for this particular configuration which can be adjusted using the digital calibration bits integrated into the structure allowing different gain and power settings. The maximum available gain setting is shown in Figure 30.

{{< figure src="technical_1/Noise_PLO.pdf}" width="500" >}}
{{< figure src="technical_1/Amp_Thd.pdf}" title="Figure 29:  Post layout simulated results of the proposed instrumentation circuit. " width="500" >}}



{{< figure src="technical_1/sim_gain.pdf" title="Figure 30:  Post layout simulated results using periodic steady state analysis to evaluate the closed loop gain of the instrumentation circuit. " width="500" >}}


Table 5: Summary of performance specifications of the proposed instrumentation topology and other bio-signal chopper stabilized amplifiers found in the literature.
|	Parameter      |  Units       |   This Work     | Markovic [^125] | Makinwa [^123] |
|----|----|----|----|----|
|	technology 		|		[nm]		|	180 | 40 | 65 |
|	Supply Voltage   |      [V]     			| (1.2)    | (1.2)    | (1)   |
|	Total Current    |    [(\mu)A]			| (1.05) | (1.67) | (2.1)|
|	Bandwidth        |       [Hz]      		| (<1)-(6 k) | (1-5k) | (0.5-1k)  |
|	Filter Order \ Roll-off | [dB/Dec]  | (20) | (20) | (20) |
|	Noise Floor   |  [$nV / √{Hz}$]     	| (55)  | (101) | (60)|
|	Noise Corner   |     [Hz]             	| $20   Hz$   | (100) | (<1)|
|	Dynamic Range |	[dB] 	  	| (58)   | (69) | (64) |
|	Area         |    [(\mu)m(^2)]       	| $6.2\cdot 10^3 $ | $7.2\cdot 10^4$| $2\cdot 10^5$ |
|	Area-Power-Product | [(\mu)W (\mu)m(^2)] | (7.3 10^3) | (141 10^3) | (420 10^3) |
|	NEF | | (1.08) | (2.5) | (1.66) |


Overall the proposed implementation performs well for supply voltages larger than \\(1.1 V\\) where the limiting factor is due to the current biased complimentary input stage. This configuration necessitates a voltage overhead requirement of \\(2V_{TH}+2V_{ov}\\). However both of the gain stages are class-A which at exhibit relatively well behaved current transients on the supplies. Class-AB alternatives do not share this feature and are more prone to disturb neighbouring recording circuits. Minimizing the dynamic current dissipation should lead to better LDO performance and lower supply induced sensor noise when many channels are integrated together. This also motivates another aspect for using a wide-band amplifier configuration for the first amplification stage because it usually implies that the common mode will also have wide band regulation. This leads to better common mode rejection in the signal band due to additional loop gain.

# 24 Analogue Signal Conversion


\label{ch:T1_converter}

Analogue to digital conversion remains to a crucial component instrumentation, particularly for full signal characterization. Even when considering the demanding constraints for integrated neural sensors, the prevalence of full spectrum signal characterization is ubiquitous in the literature. This is motivated by the efficiency and reliability of various digital processing methods that require very efficient signal conversion to discreet samples instead of processing recordings in the analogue domain. Typically the most valued performance criteria for such a system is the ADC power consumption. A Successive Approximation Register (SAR) ADC is commonly used for quantizing biomedical signals because it only dissipates switching energy that can be very small for slow sampling rates. The SAR topology is depicted in 31 and can be found extensively in BMI recording publications.

{{< figure src="technical_1/Split_Cap_Schmtc.pdf" title="Figure 31:  Schematic of a conventional N bit SAR ADC with the split capacitor at position M." width="500" >}}


## 25 Capacitive array miniaturization



This discussion pays special attention to acquiring neural recordings that include LFPs while minimizing the required silicon area per sensor. This is motivated by wanting to integrate many sensors on chip for large arrays and secondly reducing any capacitive switching noise that can be quite difficult to reject in fully integrated systems. Recording LFPs and EAPs simultaneously will require increased ADC resolution so that the instrumentation dynamic range exceeds 60dB. Equivalently this means 10 to 14 bit precision is needed depending on the nonlinearity tolerances of the proceeding processing methods. This can be quite difficult it terms of the SAR specifications because the capacitor mismatch and sampling noise can prevent aggressive sizing on the unit capacitor. For a given ADC precision N, the SAR capacitor array will require $M \cdot 2^{N/M}+M$ unit capacitors \\(C_{unit}\\) where M is the number of equally split sections. By splitting the array into sections it should be obvious that the total capacitor requirement \\(C_{Total}\\) can be reduced to some extent. The quantization errors resulting from capacitor mismatch on the other hand is also closely related to these parameters. For given standard deviation \\(\sigma\\) and confidence interval CI we can use Equation 14 to make a simple estimate for the expected quantization error \\(E_Q\\) [^131].

$$  E_Q = V_{ref} \frac{\sum \Delta Ci}{2^N C_{unit} - \Delta C_{Total}} = V_{ref} \cdot \alpha(N) \frac{√{2^N}-1}{√{2}-1} $$

The above expression assumes no split configuration is used where \\(\alpha\\) represents a scaling factor that is dependent on the number control bits for each sub-DAC, $\alpha(x)= \frac{CI \sigma}{2^x - CI \sigma √{2^x}}$. \\(V_{ref}\\) is the reference voltage by which the sampled input is normalized to arrive at the binary encoded result. Now extending this formulation to include the dependency of M and bounding $E_Q < LSB/2$ in accordance with the required ADC precision leads to the expression in Equation 15.

$$  \frac{1}{2^{N+1}} \geq \alpha(N/M) \sum_{k=0}^{M} \left[ \sum_{i=0}^{M} √{2^{i}} \right] \cdot \left( \frac{\alpha(N/M)}{2^{N/M}} \right)^k $$

There several higher order terms with respect \\(\sigma CI\\) not shown here because they have vanishing contribution as N is increased and require a numerical solution to the problem. Otherwise for M=2 and arbitrary placing the split capacitor K position in the array we can similarly reconstruct the equality from 14 in Equation 16.

$$  \frac{1}{2^{N+1}} \geq \frac{CI\sigma(√{2^{N-k}}-1)}{(2^{N-K} - CI \sigma 2^{\frac{N-K}{2}} )(√{2}-1)} + \frac{(√{2^{K}}-1) CI \sigma} {(√{2}-1) 2^K (2^K -CI \sigma 2^{\frac{K}{2}})} $$

The standard deviation \\(\sigma\\) is closely related to the exact requirements for the whole capacitive DAC in terms of the total area and unit capacitor size. The dependency of \\(E_Q\\) is mainly subject to the variance due to the MSB capacitors and for each less significant bit (from MSB to LSB) the expected variance increases by \\(√{2}\\) while its capacitive coupling decreases by 2. This is because $\sigma \propto 1/√{A_C}$ where \\(A_C\\) is the area of the capacitor. Clearly there is a process related figure of merit here that relates to the quality of capacitors since small capacitors with excellent matching will result in the best characteristics ADCs such that we minimize the % deviation per \\(\mu m^2\\).

{{< figure src="technical_1/Split_CAP.pdf" title="Figure 32: Numerical solution to Equation 16 relating the capacitive DAC area requirement with the DAC resolution (N) and the position of the split capacitor before capacitor K. " width="500" >}}


Figure 32 shows a numerical solution to the equality in Equation 16. This allows us to consider the effect of split capacitor positioning with respect to the optimal area allocation for the capacitor array. The visible plateau for small N represents the case when the design is bounded by the minimal unit capacitance. This is determined using the process documentation for the target 0.18 \\(\mu m\\) CMOS technology that gives its mismatch specifications and minimum sizing. Generally split capacitor configurations are more sensitive to parasitics they can lead to more pronounced nonlinearities. However in some cases that the unit capacitor size limits the array size such that splinting the array is an effective solution for improving power dissipation. We reiterate that this also indicates that the binary weighted configuration without splitting maximizes area efficiency if we are not limited by sampling noise or minimal capacitor sizing. In addition a fully differential DAC counter intuitively reduces the minimum size if the switching method first detects polarity before applying successive feedback [^132]. This is because the first quantization cycle does not depend on the capacitive division. This in turn means that the array can tolerate twice the mismatch error implying a 4 times smaller unit capacitance while only doubling the number of capacitors in the array.

## 26  Model based topology selection



From here there are multiple directions we can take in order to ensure efficient operation and simultaneously achieve a compact configuration. A common approach is to multiplex the SAR ADC to a large number of channels but this will also require the analogue stage driving the ADC to dissipate proportionally more power due to settling requirements on the sampling capacitance. From a high level perspective, distributing the quantization effort into a large array of ADCs with staggered operation should lead to much more systematic power dissipation due to their uncorrelated operation. Opposed to using a single high speed ADC that requires a much higher clock frequency with stronger tones in the generated supply noise. Another SAR based alternative using calibration for the capacitive array such that it can specifically be designed with the smallest possible unit capacitors. Then we could correct any nonlinearity or quantization errors that arise from capacitor mismatch if the array is characterized precisely enough. This does require either foreground or background calibration modules to extract the individual capacitor weights. Because we aim to perform a number of processing techniques in the digital domain for characterizing neural recording, it makes sense for us to consider effective means to perform calibration.

{{< figure src="technical_1/SDADC.pdf" title="Figure 33: Schematic of the proposed $\Sigma \Delta$ assisted SAR ADC topology for achieving a more compact configuration." width="500" >}}


The structure illustrated in 33 represents a hybrid topology based on SAR and sigma delta structures. The motivation is driven by the efficiency of SAR quantization for large signals and the compactness of high resolution quantization from sigma delta loops. The digital control will perform fully differential bottom plate sampling of the input which is then rapidly quantized to \\(2^N\\) levels using the typical binary search. After the SAR operation the resulting residue left on the capacitive array is quantized using a sigma delta control loop that feedback on the nodes \\(V\Sigma\Delta\pm\\).

There is a strict advantage over conventional sigma delta loops which is that the residue error that needs to be quantized is reduced to \\(\frac{V_{ref}}{2^{N}}\\) which can easily be designed to lie within the linear range of a differential pair. This negates having to use passive or active feedback to deal with transconductance nonlinearity and significantly improves the power efficiency by retaining a relatively simple control loop topology. Moreover as the feedback loop is typically responsible for small dynamic range of 30dB the requirements on clock jitter and decimation filtering is made more relaxed.

The more desirable advantage over a high resolution SAR is that the capacitive DAC may designed in a highly optimal configuration with as few bits as possible. This allows sizing that primarily focuses on suppressing parasitic effects with minimal sampling capacitance. As will be demonstrated this topology does not require an axillary calibration DAC or a pseudo random dithering source for performing mismatch correction. This is due to the capability that the internal sigma delta structure is in the same signal loop as the SAR operation and can trade-off bandwidth for increased noise rejection simply by adjusting the sampling frequency \\(f_s\\). Naturally because this topology inherently needs a pre-amp stage for SAR conversion we should not expect the FOM to do better than low resolution SARs.

Intuitively one can think that when combining the two topologies the individual sources for power dissipation now scale with \\(2^{\frac{N}{2}}\\). More specifically these sources come from the capacitive DAC and decimation filter. The components that do not have reduced scaling are related to the sampling noise and the thermal noise floor of the oversampling modulator. To demonstrate this quantitatively we will build an analytic model for the SAR and \\(\Delta\Sigma\\) SAR topologies to demonstrate some of the inherent characteristics. This will also reveal the techniques for optimizing of the proposed structure.

$$  FOM_{ADC} = \frac{P_{sys}}{2^{N} f_s} $$

Maximizing the performance indicator from Equation 17 will represent our objective function which reflects the efficiency by which each sample is converted into a digital code. Through the simplicity of this relation, any comparison primarily requires an accurate expectation for power budget in terms of the required resolution or precision requirements.

$$  P_{Ideal} = \underbrace{ E_{search} \cdot f_s C_{unit} V_{ref}^2 (2^{N-2}+2^2)}_{Capacitor Array} + \underbrace{2N (N+2) f_s E_{gate} }_{Register Logic} $$

Equation 18 Considers the primitive structure with an ideal comparator where \\(E_{search}\\) represents the average dissipation for binary search switching method and \\(E_{gate}\\) is the average gate dissipation per clock cycle. Both these parameters adjust to different core libraries or various switching methods that typically trade off efficiency for parasitic tolerance [^133]. This ideal structure is extended by the requirements of either a dynamic latch comparator or an analogue pre amplifier that allows negligible comparator requirements at the expense of consuming a static current. The classic pre-amplifier approach also tends to deal with mitigating kick back noise but in general the straightforward application of classic \\(kT/C\\) relations conveniently give;

$$  P_{amp} = 32   \pi   \ln(2) \cdot \underbrace{\frac{(U_T   N   2^N)^2}{V_{ref} \cdot \eta   q}}_{Noise} \cdot \underbrace{A_{ol}   f_s   NEF^2}_{Bandwidth} $$

Here \\(A_{ol}\\) represents the gain provided by the pre-amplifier. Notice the very typical inverse relationship with respect to \\(V_{ref}\\) which motivates the use of the more efficient dynamic comparator structure. However evaluating the equivalent input referred noise of a dynamic structure accurately requires the a piece wise evaluation for different phases of operation and the respective stochastic integrals [^134]. The contribution can be associated with two dominant sources, that of sampled noise;


$$  \sigma_{S} = \frac{4   kT}{3   C_x   F} + \frac{ kT}{3   C_x   F^2   H} + \frac{ kT}{12   C_x   F^2   H^2} $$

And noise contributed from transconductive elements;

$$  \sigma_{M} = \frac{kT}{C_x   F^2} + \frac{kT}{2   C_x   F^2   H}  + \frac{kT}{8   C_x   F^2   H^2} $$

$$  F = \frac{2 \rho V_{th}}{V_{ref} - V_{th} }  \text{and}  H = \frac{V_{ref}}{2  V_{ov}} \cdot {2 \rho }{1 + \rho} $$

As before, this must be bounded by the acceptable quantization noise, $ V_{ref} \cdot {2^{-N-2}} = √{\sigma_M + \sigma_S } $, which give the values for \\(C_x\\). Strictly there is a strong dependence on the input signal in order to evaluate the dissipated power but on average it is reasonable to approximate this to the capacitive switching energy of $P_{Latch} \approx f_{s}  C_x   V^2$.

Now consider the components of the \\(\Delta\Sigma\\) structure. Clearly it will follow closely to that of the pre-amplifier based relations with the exception that the primitive components from Equation 18. Instead this will scale with \\(N-K\\) where \\(K\\) is the number of bits resolved by the sigma delta loop. Here two additional components will be accounted for, the first is the integrator and the second is the digital FIR that decimates the modulated residue quantization. A second order feed forward integration topology is chosen for \\(H(s)\\) based on its efficacy of being applied to the configuration shown in Figure 33 and primarily minimizing the number of summing operators and coefficients prone to mismatch. For the sake of discussion we make the assertion that decimation noise rejection is bounded $K \leq (FIR)^{-1/2}$ in the case of a rectangular window for analytic clarity [^135]. Furthermore, note that as we increase the SAR quantization the first stage will proportionally see a reduction of the input signal that needs to be accounted for to achieve the correct integration constant.

$$  P_{int} = 32 \pi \cdot \underbrace{\frac{(U_T   2^{N}   NEF)^2 }{ q   V_{ref}}}_{Noise} \cdot \underbrace{FIR   f_s   (1+2^{N-K}) }_{Bandwidth} $$

And similarly the digital decimation filter will scale in the form of;

$$  P_{fir} = \underbrace{2^{K}}_{OSR}   \underbrace{( K + \log_{2}(K))}_{Quantization}   fs   E_{gate} $$

Collecting these terms for each topology will equate to expressions that typically have scalar dependencies on technology or implementation which we must make a set of reasonable assumptions for.  The literature will indicate numerous means by which each component can be reduced through specialized logic cells, adaptive comparator power allocation, or power saving switching methods. Our particular interest lies with the dependency on N that will imply the effectiveness of a certain topology for a given dynamic range requirement. In addition this familiarizes us with specific factors fundamental to power dissipation with respect to resolution.

{{< figure src="technical_1/P_TOP_N.pdf}" width="500" >}}
{{< figure src="technical_1/P_TOP_A.pdf}" title="Figure 34:  Summary of the FOM (\\(P_{sys}/2^{N} f_s\\)) for each topology with respect to different resolution requirements. " width="500" >}}


Figure 34 presents the expected merit for each topology as the target resolution is varied. Without consideration for area, there is a clear power advantage for the dynamic SAR structure mediated primarily by the fact that the comparator does not have settling associated tolerance. This is the main reason why the pre-amp topology requires a proportionally increased bandwidth/power as resolution is increased. What stands out is that the \\(\Delta\Sigma\\) structure has a power dependency $\propto   2^{3N}$ for achieving the required input referred noise in contrast to more conventional dependency of \\(2^{2N}\\). The mechanism behind this is due to the SAR quantization that reduces the signal input range which needs to be recovered to achieve the correct integration factors. Moreover the over sampling ratio increases simultaneously which has an overall multiplicative effect. Clearly the resolution of the SAR quantizer should only perform a few conversion that put the residue in the linear range of the loop filter and let the modulator perform most of the quantization effort. When all topologies are using the same unit capacitor, this result demonstrates that for \\(N < 5\\) & \\(N > 14\\) the \\(\Delta\Sigma\\) topology becomes strictly unfavourable in terms of power but performs comparably with respect to power efficiency for \\(N \approx 10\\). Taking the FOM area product by considering the capacitors in terms of \\(\Box\\) units the advantage of the \\(\Delta\Sigma\\) topology becomes more obvious. For the precision significant to neural recording, \\(8<N<12\\), the hybrid structure consistently grantees a more compact configuration by a factor of 10.

{{< figure src="technical_1/FOM_Space.pdf" title="Figure 35:  Figure of merit dependency of the proposed \\(\Delta\Sigma\\)SAR topology with respect to design parameters K1 & K2. " width="500" >}}


Considering the design space of the \\(\Delta\Sigma\\)SAR structure in more detail will expose a more optimal strategy for increasing FOM. Figure 35 exemplifies how the FOM behaves as either the SAR of sigma delta accuracy is increased. After the optimal basin at N = 9 & K=4 the best strategy for improving ADC resolution is by increasing SAR quantization at half the rate of the sigma delta increase in resolution. For reference a conventional $\Delta \Sigma$ modulator [^136] is designed with the same target specifications and using the same design method to configure the OPAMP integrators and resistive input network. Such a configuration achieves 167 dB FOM<sub>s<sub> irrespective of target resolution when we consider just the analogue power dissipation. In fact this figure is commonly achieved by state of the art [^137]. As shown in Figure 36 the \\(\Delta\Sigma\\)SAR configuration can theoretically achieve more than 4X better performance than conventional \\(\Delta\Sigma\\) modulators for resolutions above 12 bits even when operating at lower supply voltages. This is because of the improved noise efficiency. Please refer to Section 58 for additional details regarding derivations and topology comparisons that are omitted here for clarity.

{{< figure src="technical_1/AMD.pdf" title="Figure 36:  Estimation on the expected figure of merit for a target resolution and varying SAR precision. The red star and blue circle indicate the target and measured performance respectively. " width="500" >}}


## 27 Circuit Implementation



Extending the conventional SAR structure to perform sigma delta modulation is achieved with relatively little changes to the overall topology. The main difference is that during the last phase of SAR conversion a register must be toggled that switches in the integrators intermediate to the comparator. Simultaneously the \\(V\Sigma\Delta\pm\\) capacitors are directly connected to the comparator bipolar output instead of the common mode voltage \\(VCM\\) for differential feedback. This configuration is integrated on chip and performs 7 bits of differential SAR quantization with another 5 bits resolved by the noise shaping modulator with an over sampling rate of 32. At the system level, 4 analogue recording channels will be multiplexed to the input of the ADC which implies sampling rate of \\(100 kS/s\\) is required to sample each output at \\(25 kS/s\\).

{{< figure src="technical_1/SAR_Arch.pdf}" width="500" >}}
{{< figure src="technical_1/SAR_Logic.pdf}" title="Figure 37: Schematic configuration of the top level control for the \\(\Delta\Sigma\\)SAR data converter." width="500" >}}


Figure 37 shows the top level configuration of this data converter. By using a specialized register logic slice a small reduction in complexity is achieved in addition to the mitigation of timing issues typical with the conventional self clocking register configuration. This topology uses a bottom plate sampling strategy to neutralize the effect of parasitics and common mode comparator nonlinearities while operating at 1.2V with a 10MHz clock frequency. Although there are only \\(N-K+OSR\\) active phases, settling the output of the recording amplifiers on to the capacitor array will require several cycles because of the band limited behaviour present in the driving stage.

The implementation of the capacitive DAC and second order feed-forward integrator are shown in Figure 37. This configuration also opts to scale the voltage reference for the LSB in order to reduce the total number of capacitor required. As the capacitor array is implemented using CMIM devices the 7 bit differential structure with a split capacitor for \\(M=3\\) will grantee 10.1b for a confidence interval of \\(3\sigma\\) using Equation 16 and process documentation parameters that show a $8\times8 \mu m$ has \\(0.23 %\\) mismatch induced standard deviation. The reasoning for this configuration is that we are guaranteed \\(>9.5 bits\\) without calibration and will allow \\(>12 bits\\) with calibration. For either case the accuracy is sufficient for recording LFP and EAP signals simultaneously. This result was also confirmed with monte-carlo analysis using foundry supplied PSP models.

{{< figure src="technical_1/T1_SDSAR_CDAC.pdf}" width="500" >}}
{{< figure src="technical_1/T1_SDSAR_INT.pdf}" title="Figure 38: Schematic implementation of the \\(\Delta\Sigma\\)SAR structure. " width="500" >}}


The integrator topology primarily deals with the contrasting bandwidth requirement of the SAR operation and the sigma delta integration for the first stage. Particularly when taking the SAR decisions at the oversampled clock the first stage can only provide wideband gain if the capacitor is switched out and a resistive element is used instead. The circuit complexity can be dramatically reduced by using triode region transistors that regulate the PMOS biasing current for a well defined common mode. Because these transistor can be large in area they could slow down the maximum SAR speed. To avoid this the CMFB circuit is semi open loop during the SAR quantization leading to an increase bandwidth by using the common mode voltage that preserved on the integration capacitor. Also by switching the biasing current of the analogue summing stage a constant common mode can be presented to the comparator input thereby reducing any off-set disparity between the two operation phases.

{{< figure src="technical_1/ADC_Label.pdf}" width="500" >}}
{{< figure src="technical_1/ADC_Chip.pdf}" title="Figure 39: Physical implementation of ADC using a 6-metal $0.18   \mu m$ CMOS process measuring $93 \times 147   \mu m^2$ in size." width="500" >}}


Figure 39 shows the fabricated structure of the ADC. Since the capacitors are placed on top of the active circuits this floor plan distances the integrators and the MSB capacitors to physically isolate the digital switching noise sources. A number of shielding structures are employed to improve post layout performance. There include various guard rings and isolating N-wells but due to the proximity of the digital switching the most effective strategy is appropriately orienting fully differential structures in order to equalize the coupling components. Here metal layers 1-3 are used for transistor interconnect, layers 5-6 for the capacitive DAC, and layer 4 is interposed in order to shield the two sections while connected to the common mode voltage. This is because the transient fluctuations on \\(V_{cm}\\) are only due to mismatch and should be the most quiet reference in the system with large capacitive loading.

In order to take advantage of this structure we reveal two distinguishing characteristics that can not be found in either conventional topologies or other hybrid topologies. When the capacitive DAC is considered as a set of weights that need to be determined we realize that the derivative for slow varying signals is predominantly quantized by the sigma delta loop. With the exception when the SAR bits switch the quantization is independent of the mismatch in these weights. As a result all the mismatch coefficients can be accounted for with respect to the $\Sigma \Delta C$ capacitor.

{{< figure src="technical_1/adc_cloop.pdf" title="Figure 40:  Control loop used to perform calibration with a slow test signal at the ADC input." width="500" >}}


The calibration technique discussed is abstractly represented by Figure 40 where there are two IIR control loops with the coefficients \\(a_1\\) and \\(b_1\\). In part this loop performs normal operation by evaluating the signal quantization \\(Q_{sig}\\). This is done adding the SAR quantization with calibrated weights and decimating the oversampled residue with a \\(32^{nd}\\) order FIR window quantized with 8 bit coefficients for each sample. Here \\(a_{1}\\) simply has to be small enough to track the signal and reject noisy components to determine $\Delta Q$. $\Delta Q$ represents DNL nonlinearities that are used to adjust the coefficients \\(K_{DAC}\\). The multiplication operator is in fact a bitwise evaluation that indicates if a coefficient needs to be adjusted due to a correlation between $\Delta Q$ and a change in that bit. Hence \\(b_{1}\\) needs to be small enough to prevent level dependent tuning and \\(V_{test}\\) should be a full range slow varying signal.

{{< figure src="technical_1/adc_UC.pdf}" width="500" >}}
{{< figure src="technical_1/adc_CC.pdf}" title="Figure 41: INL Plots illustrating the mismatch artefact reduction due to calibration." width="500" >}}


The improvement in INL is evident in Figure 41 due to the calibration mechanism with \\(a_1=1/4\\) and \\(b_1=2^{-8}\\). The close interaction between INL & DNL errors over the full dynamic range for a capacitive array in addition to the sigma delta loop's capability of quantizing $\pm 2   LSB$ of the array allows this method to converge accurately. Here it is observed that the calibration improves the quantization accuracy by two additional bits.

{{< figure src="technical_1/adc_thdsnr.pdf" title="Figure 42:  Measured THD and SNR of the fabricated data converter." width="500" >}}


{{< figure src="technical_1/ADC_TEST.jpg}" width="500" >}}
{{< figure src="technical_1/adc_TI.pdf}" title="Figure 43:  Testing setup used for characterizing the ADC." width="500" >}}


Figure 43 shows the test bench used during device characterization. The saleae logic device is a digital probe that offers 100 MS/s digital signal acquisition for measurements of up to 10 seconds. Here the raspberry pi module simply provides real time interaction with the device configuration using automated spi control and a graphical user interface that will indicate ADC precision based on the selected operation. This allows us to tweak the operating conditions and find which noise sources are disturbing the configuration. The analogue bias \\(I_{BIAS}\\) is generated by a 2602A Keithley system source meter and fed in using a guarded triax cable. The differential input signals are generated using a Agilent 33522A arbitrary waveform generator and fed to the ADC input using BNC cables.

Table 6 outlines the characteristics of the implemented ADC configuration while comparing it to recent oversampling/noise shaping data converter publications. Figure 42 demonstrates the spectral characteristics of the quantization output for a input signal at half the full input range after calibration. In comparison to the analogue instrumentation, the resource related specifications are significantly larger. However note that there requirements are distributed over a number of channels as a result of multiplexing this structure.

Table 6: Summary of performance specifications for the \\(\Delta\Sigma\\)SAR data converter and other oversampling/noise shaping data converter structures found in the literature.
|		Parameter     | Units  | This Work  | Lo [^138] | Roermund [^139] |
|----|----|----|----|----|
|		Technology | [nm] | 180 | 65 | 65 |
|		Supply Voltage  | [V]  | (1.2)   | (1.2) | (0.8)         |
|		Total Current   |[(\mu)A]   | (12)   |  (13) |  (1.7)   |
|		Sampling Frequency  | [kS/s] | $200 $ | (8) | (16)   |
|		ENOB           | [bits]  | (11.3) | (17.5) | (14.5) |
|		SFDR           | [dB]    | (86)     | (105) | $ 87 $ |
|		Area           |  [$\mu m^2$]  | $93 \times 147$ | $400 \times 180$ | $600 \times 300$|
|		Power-Area-Product | [$\mu W   \mu m^2$] | $1.9 \cdot 10^5$ | $1.1 \cdot 10^6$ | $2.4 \cdot 10^5$|
|		$P/(fs + 2^N)$           | [fJ/conv] | (10)  | (29) | (6.6) |
|		(SNDR+10log(BW/P))				| [dB] | (166) | (180) | (177) |


The trade off with respect to residue over sampling in Figure 44 demonstrates that there is some flexibility with respect to sampling rate and SINAD performance. In addition this also clarifies that post-fabrication adjustments do not exhibit significant resolution improvements beyond the design point. This is related to the sampling noise of the capacitor array and the noise floor of the analogue integrators that need to be programmable for different oversampling ratios. At which point the decimation also has more strenuous requirements that may result in an inefficient resource overhead. Strictly stated it is significantly more efficient to reject noise with digital bandpass filtering selected frequency components than having the ADC resolve the signal beyond the target precision.

{{< figure src="technical_1/adc_fom.pdf" title="Figure 44:  Measured Figure of Merit as a function of oversampling ratio." width="500" >}}


In the context of miniaturization the topology presented here follows closely to the expected improvement from the model for high resolution signal acquisition. We achieve nearly 12 bits of quantization with a 6 bit equivalent capacitive DAC which is reflected in the compact design foot print. When compared to similar compact ADC implementations found in recent publications we observe a competitive power budget with again significantly smaller area requirement. Some additional digital processing is required opposed to the simplicity of SAR converters to take full advantage of the topology. However such hardware is typically readily available in systems that also perform spike sorting and neural signal classification.

# 28 System Level Abstraction


\label{ch:T1_model}

Numerous specifications such as ADC resolution and input referred noise of the instrumentation amplifiers relate directly to signal specific parameters. Moreover a particular processing algorithm would favour certain filter configurations of others in terms of signal conditioning. In multi stage systems however there is a significant amount of flexibility related to choosing gain for individual stages or their filter parameters that is indifferent to the resulting transfer function. Here we consider such a primitive \\(N\\) stage analogue processing chain and discuss the allocation of resources to gain insight to some of the high level the optimization for selecting a specific configuration. Such a configuration is shown in Figure 45.

{{< figure src="technical_1/ACS.pdf" title="Figure 45: Multistage amplifier configuration using the series G to adjust the allocation power and area. " width="500" >}}


$$  G[n] = A_{g} \left( \beta + \alpha^{n} \right)  \text{where}  A_{g} = √[N]{\frac{G_{T}}{ \prod_{i=1}^{N} (\beta + \alpha^{n} )}} $$

Consider a geometric series for the gain of each stage as expressed in Equation 25. Here \\(G_{T}\\), \\(\alpha\\), \\(\beta\\) represent the total gain required, resource distribution factor, and a minimal contribution factor. The formulation is motivated by the fact that if \\(\alpha\\) is one resources are allocated equally. This means every stage has equal gain but it also implies that the sum of all gain factors is minimal leading to a minimum amount of area due to the feedback capacitors. More typically designs will choose a smaller \\(\alpha\\) such that most of the gain is situated at the first few stages. This allows some reduction in power in the proceeding stages because of the reduced noise requirement. \\(\beta\\) simply allows us to specify that a fraction of the total gain is uniformly distributed but is typically kept small in order to maximize the benefit from resource redistribution. This allows us to express the noise power requirement for a given set of parameters in Equation 26.

$$  P_{Amplifiers} = P_{unit}  \left( 1 + \sum_{k=1}^{N-1}\left[\prod_{i=1}^{k} \frac{1}{A_{g}   \beta + A_{g}   \alpha^{i} }  \right] \right)^2 $$

$$  A_{Gain}= A_{unit}\left( \sum_{k=1}^{N} \left[1 + A_{g} \beta + A_{g} \alpha^{k} \right] \right) $$

Here \\(P_{unit}\\) is simply evaluated from Equation 6 and leads to an area requirement that is simply expressed using Equation 27. Now taking some typical parameters we can evaluate a possible configuration of gains and thereby the associated allocation of resources. This is shown in Figure 46.

{{< figure src="technical_1/RDBG.pdf" title="Figure 46: Resource allocation for analogue power and area using the parameters \\(G_T=500\\), \\(\alpha=0.3\\), and \\(\beta=0.05\\). " width="500" >}}


Lets take \\(A_{unit}\\) as some unit capacitance size that allows the deviation of gain due to mismatch to fall inside the confidence interval. In order to realize Equation 26, each stage has its power and input referred noise reduced by accumulated gain for the preceding stages. This result presents us with the trend illustrated in Figure 47 where it appears that in many stage systems it is relatively beneficial to redistribute the resources to the front-end for a reduction in overall power. However when the number of stages is three or less we observe the increase in area can diminish this improvement for high gain system requirements.

{{< figure src="technical_1/NM_NP.pdf}" width="500" >}}
{{< figure src="technical_1/NM_PAP.pdf}" title="Figure 47: Normalized resource improvements for \\(\alpha\\) with respect the case when \\(\alpha=1\\) for each configuration. " width="500" >}}


So far we have neglected some aspects to the design consideration. The first is the multiplicative increase standard deviation as N is increases and the sensitivity to variance being inversely proportional to closed loop gain. Here we can account for the increased variance by proportionally increasing \\(A_{unit}\\) in order to neutralize this increase according to Equation 28.

$$  \Delta   \sigma^2 =\frac{A_{\mu+\sigma}}{A_{Gain}} \approx \prod_{i=1}^{k} \left( 1 + \sigma   CI \left[ 2 - \frac{2}{√{ A_{g}   \beta + A_{g}   \alpha^i }} \right] \right) $$

Again \\(\sigma\\) represents the deviation for a chosen unit capacitance and \\(CI\\) is our confidence interval. For completeness in estimating area we will also introduce the capacitance required for performing filtering on the last \\(K\\) stages. Rearranging Equation 6 in terms of output referred noise according to Equation 29.

$$  e^2_{out} = \frac{kT}{C}   {NEF^2}{\eta} $$

Combining these terms lets us define a more accurate area requirement that is reformulated in Equation 30.

$$  A_{filt} = A_{unit} \cdot \frac{kT}{C_{unit}}   \frac{NEF^2   SNR^2}{Vdd^2   \eta} \cdot \left( 1 + \sum_{k=1}^{K-1}  \prod_{i=1}^{k}  \left[A_{g} \beta + A_{g} \alpha^{N-i} \right] \right) $$

It is important to point out that SNR here refers to the SNR of the data converter as we have fixed the input referred noise of the system for a systematic comparison and we adjust \\(G_T\\) to fill this dynamic range. And extending this result with the requirements for signal conversion we can estimate system level power \\(P_{Total}\\) and area \\(A_{Total}\\) requirements as a sum of individual components according to Equation 31.

$$  A_{Total} = A_{filt} + A_{Gain} + A_{ADC}  \text{and}  P_{Total} = P_{Amplifiers} + P_{ADC} $$


Taking an appropriate set of parameter values, the system of relations is exemplified in Figure 48 with respect to the dependency on the supply voltage, \\(Vdd\\). As illustrated there are two domains when considering the area requirement. For small \\(Vdd\\) the sampling & filtering noise requirements overwhelm the design particularly in this case if \\(\alpha\\) is not taken small enough and a second order roll off is needed. When there is more voltage overhead available we observe reliably matching in input dynamic range of the ADC is the dominating factor.

{{< figure src="technical_1/NM_TSNA.pdf}" width="500" >}}
{{< figure src="technical_1/NM_TSNAP.pdf}" title="Figure 48: Analogue resource relations with respect to different supply voltages. " width="500" >}}


The area power product also tells an interesting story. When \\(Vdd\\) is larger than 1 V a clear proportional dependency on power is apparent that is mostly related to the total gain & noise requirements of the system because the ADC is not the limiting factor. However for small supply voltage the power dissipation requirement is more closely related to the lower noise quantization requirements presented by the SD-SAR topology. We should be careful because certain circuit topologies are simply not viable below specific supply voltages and as a result it would no be possible to achieve a NEF smaller than 2. Figure 48 also indicates when particular topologies are viable specific to the $0.18   \mu m$ CMOS process where $V_{th} \approx 350 mV$. That said it is likely a system can be designed with \\(0.6 V\\) supply in order to achieve significant power and area savings. The main challenge will be achieving acceptable total harmonic distortion as the supply will not easily allow cascoding transistors. Particularly sub-threshold transistors suffer from \\(Gm\\) nonlinearity as a function of \\(e^{\frac{-V_{DS}}{U_T}}\\) that can only be compensated by increased loop gain and multi-stage topologies. Since it is implementation dependent, it is difficult to quantify what this increase in area an power overhead this will result in. We can assert that \\(60 dB\\) precision with instrumentation has very significant diminishing returns when the conventional design approaches a \\(2 V_{th}\\) supply. The reader can find more details in regard to these comparisons in Section 60.

The approach taken here can be exhaustively extended towards including more detail in the system level design in order to leverage the capability of numerical methods. Higher order Gm-C filtering structures can be accounted for as a single stage by introducing new parameters that reflect the increase in \\(NEF\\) and filtering capacitors. Transistor area per amplifier can arguably be assumed static if chopping techniques are employed or alternatively this can accounted for by considering the flicker noise relations for the input transistors. However these contributions have negligible effect on changing the optimal resource destitution and will be more influenced by strategic positioning of poles to reject certain noise components. The most critical parameters on the systems level is the supply voltage as well as the requirement for channel to channel gain matching. As the power area product has a inverse square dependency as either \\(V_{DD}\\) or gain variance tends to zero. There are only a select number of scenarios where gain matching is of significance which is primarily in the case of distributed LFP recording and multi electrode (i.e. tetrode) recordings where exact coupling of neural circuitry is in question. The supply voltage has significance with respect to the expected power dissipation of the on chip digital processing and it is understandably advantageous to aggressively dissipate more power on the analogue side if the power saving in the digital domain indicate a overall improvement.

We note another aspect to technology selection in addition enabling voltage scaling is the increase in functional capacitor density. In fact we have shown that the dominant factor for area requirement in chopper stabilized structures is capacitance through the strong dependency on gain and filtering elements. More advanced processes have an increased number of metal layers and higher transistor gate capacitance. This ultimately leads to an increased capacitor density per square millimetre. In certain scenarios this should allow us to marginally shrink amplifier configurations while keeping the same filter characteristics. The main concern would be associated with capacitor nonlinearity that requires extra consideration or correction circuits.

\fi

# 29 Conclusion



This chapter has demonstrated the capacity for conventional analogue instrumentation with state-of-the-art circuit techniques. This presents capacity for achieving very compact performance that is sufficient for the full characterization of neural recordings. The fabricated system uses 0.03 mm\\(^2\\) size silicon footprint for 4 recording channels that can characterize 5 mVpp neural signals with over 11 bits of precision. In addition proposed $\Delta\Sigma SAR$ ADC topology demonstrates how oversampling converters can achieve 10fJ/conversion efficiency with minimal circuit complexity. The techniques applied here suggests chopping and sigma-delta modulation are key components for achieving better performance particularly for size constrained systems. In association we suggest immediate digitization & coherent mixed signal processing to leverage a number of advantages. Moreover we expect modern system will allow more processing capabilities in the digital baseband for BMI systems that needs to be used effectively.

The significance of minimizing the noise efficiency factor has been revealed in terms of having profound influence to power dissipation and area. In extension we have presented a number of topologies that excel at achieving excellent power and area efficiency in the case of single stage, two stage, and ADC structures. However we are left with little surprise when methodical optimization of various configurations is limited by the fundamental bounds in terms of noise and dynamic range. In fact various idealized configuration show little benefit with respect to one another if they have been optimized and exploited appropriately with the understanding presented. It is characteristic that improving resource efficiency for full bandwidth signal quantization is difficult because we simultaniously attempt to achieve lower supply voltages.

Although digitization is crucial to most neural recording systems for extracting the signal characteristics used to train and improve signal postprocessing. It is clear that improvements at the system level will lie very much in the domain of specialized instrumentation and analogue to information converters. This notion is motivated by the desire for the system to be limited by the law of equipartition and less so by the quantization process of the data converter. The direct classification of recordings in the analogue domain has significant implications on the responsibilities of the accompanied DSP on chip and the reduction of associated processing bandwidth.

# 53 Conclusion

As brain machine interfaces continue to progress in establishing a better communication link between neural activity and our models for cognitive or behavioural dynamics. We can expect with certainty the design considerations of these systems will remain a very involved process. Using abstractions and resource models will play a pivotal role in realizing these complex systems. Particularly as these systems require operational efficiency far beyond current state-of-the-art to enable chronic and implantable neuro-prothetics for full limb replacement. The models discussed here not only guide the design process towards more optimal systems they also provide excellent insight to inherent design limitations at different stages of design though clarity in system level objectives. A considerable amount of effort was put into realizing highly efficient and ultra-low power amplification of signals which can naturally be extended towards improving on-chip voltage regulators or RF-telemetry circuits to advance the capabilities of these systems while operating with several hundred millivolts of supply head-room.

There still remain many opportunities as emergent processing modalities that find them selves adapting to the current paradigm or platform of operation. Currently that paradigm is nanometre CMOS which suggests nothing other than ''there is plenty of room at the bottom'' [^201]. While the results presented here advocate for transitioning to smaller feature sizes to miniaturize recording and increase the in channel processing capabilities that accommodate the algorithms for extracting information from electrode recordings. We must also give way to software abstraction that deals with the increased complexity of these systems to retain long term utility and higher level adaptive function. Moreover we signify the resulting flexibility empowers electronic sensing systems to meet the broad set of challenges found in fabrication, implantation, and realization of chronic solutions. If we consider the maximal density of the proposed structures, by estimation for two-dimensional sensing arrays it is viable simultaneously record at a density of 400 locations different simultaneously per square millilitre of CMOS chip. That figure for some areas in the visual cortex implies a ratio on the order of 100 neurons per electrode [^202]. This encourages us that this direction is an important step forward towards high fidelity neural decoding systems and will allow precise studies of neural circuits in rodents for disease models.

Putting our findings in perspective of the SAR limit to inducing power inside the body [^203] and state-of-the-art results in midfield powering of millilitre sized implants as coupling scenario for implants deeper than 5cm[^14]. This work suggests the power budget for a 2 mm\\(^2\\) CMOS chip and coil is around 200\\( \mu\\)W at 11% of the maximum safety threshold. This may be improved with near-field coupling of multi coil configurations but either solution is challenged in powering multiple devices without more active electronics. We can be confident that our micro-controller structure in 65 nm CMOS is compact enough that the main limitation is power related. Extrapolating the power requirements from the current 180 nm CMOS design gives us the impression that we can integrate at least 136 reconfigurable instrumentation channels dissipating \\(1.47 \mu\\)W by both analogue and digital domains. In fact integrating 64 channels can already be realized by our 180 nm CMOS implementation with power induction at 71% of the maximum safety threshold. While this seems unattainable by many systems presented in the literature today we argue that this approach will even allow active telemetry with UWB data transmission from the chip because of the highly compressed data-rates [^204].

# 54 Original Contributions

The technical contributions presented by this thesis are detailed in the list below of which some has already been published. These publications are outlined in Section 56.

\begin{minipage}{0.9\textwidth}
\begin{itemize}
	\item{**Chapter 16**}
	\begin{enumerate}
	\item[\\(-\\)]{A 1.26 \\(\mu\\)W instrumentation amplifier with 6 kHz bandwidth that provides 52 dB gain and exhibits a input referred noise figure of 5.6 $\mu V_{rms}$ with a flicker noise corer of 20 Hz.}
	\item[\\(-\\)]{A 14.4 \\(\mu\\)W 11.4 ENOB \\(\Delta\Sigma\\)SAR ADC that can perform 200 kS/s with a 2.4 pF sampling capacitance that achieves a 10 fJ/conversion figure of merit.}
	\item[\\(-\\)]{Fabricated fully integrated signal acquisition front end that uses 0.01 mm\\(^2\\) of silicon area to perform 5 mVpp signal quantization with a 58 dB dynamic range.}
	\end{enumerate}
\end{itemize}
\end{minipage}

\begin{minipage}{0.9\textwidth}
\begin{itemize}
	\item{**Chapter 30**}
	\begin{enumerate}
	\item[\\(-\\)]{PCA & template matching spike sorting method for embedded systems that require 57 operations per sample and 680 bits of memory to perform fully unsupervised classification with \\(>\\)80% accuracy.}
	\item[\\(-\\)]{A 1.52 GOPS/mW distributed processing architecture for neural recording applications that has a 0.02mm\\(^2\\) silicon foot print with fully reconfigurable 8 bit processing capabilities.}
	\item[\\(-\\)]{Linux based development platform for developing decoding techniques with support for C/C++/Python and other functional languages.}
	\end{enumerate}
\end{itemize}
\end{minipage}

\begin{minipage}{0.9\textwidth}
\begin{itemize}
	\item{**Chapter 43**}
	\begin{enumerate}
	\item[\\(-\\)]{A 0.6 V 58 dB SNDR time domain instrumentation architecture with a NEF of 1.18 that generates multiphase PWM encoded digital signals with a sub 0.01 mm\\(^2\\) footprint.}
	\item[\\(-\\)]{A 4\\(^{th}\\) order oscillator based bandpass filter for conditioning the time domain signals with reconfigurable gain that dissipates 120 nW of power.}
	\item[\\(-\\)]{Unsupervised analogue classification technique that achieves over 72% accuracy without necessitating signal quantization or a large number of analogue components.}
	\end{enumerate}
\end{itemize}
\end{minipage}

# 55 Future Work

We have presented some of the most compact high performance instrumentation structures that can be integrated in nano-meter CMOS for wide-band recording of neural activity. This shifts the focus towards careful system integration of electrodes, data processing, wireless communication, and power management in order to realize a truly implantable solution. The first core objective that extends on the work here is stream lining the design with industry standard synthesis for large scale integrated systems. This implies formal silicon verification for proof of concept from our latest developments and involve more conservative design choices associated with improving device lifetime and risk-factors. This is important in providing a more universally translatable platform to allow other components of the system to be integrated arbitrary to the technology node of fabrication.

However we should also consider the long term goal for these systems. Our micro-controller approach dedicates a significant amount of resources just to perform spike sorting or signal characterization. While this is the focus in current systems to allow wireless solutions it is not the primary challenge for a neuro-prosthetic device which instead lies with decoding spike-train data or decomposing LFP activity. This implies that we need to adopt more resource efficient structures to extract features or spikes in neural activity equivalent to that proposed in Section 48. More concise signal acquisition allows us to focus on decoding the collection neural activity rather than single recordings and possibly increase the prevalence where we reconfigure what signal features are extracted based on what is most informative at the system level. Specifically we picture a hierarchical approach where without intervention the system tunes to relevant information to guarantee some level of performance which is then tuned incrementally with off-chip supervision to maximize performance with higher order statistics and better optimization methods to find the best configuration that selects electrodes, LFP/EAP features, denoising bandwidth, etc. Moreover some aspects in regard to the design of a medical grade device are not yet fully investigated. For instance can we make the analysis of spiking activity suitable for long term reliability? This is specifically the endeavour of current research where experimental platforms need to reflect the informed capabilities.

We find it highly probable that integrating processing structures and other auxiliary circuit components will be one of the simpler aspects of realizing BMIs with better decoding performance and capacity. Primarily because the design tools allow directed and precise development following methods already presented in the literature. Innovation in electronics will likely allow the required performance improvement by scaling when it is needed. The principle challenge lies with compact system integration of these devices. Compatible fabrication of penetrating electrode structures with the right impedance characteristics for low noise and sustain unimpaired neural tissue interface for coupling activity may raise significantly more unexpected challenges. In addition we note importance of introducing miniaturized antenna structures that perform harvesting power as well as back-scattering recorded data. Both of these aspects are crucial to scaling integrated recording systems in a distributed fashion. That said, the effort towards developing computational modalities for high dimensional data analysis that specifically use analogue or time domain techniques still hold uncovered potential. Drawing from structures in the brain, bio-inspired ultra-low-power processing architectures for machine learning is an emergent challenge that can also find utility in brain machine interfaces [^205].

# 56 Publications

The relevant conference and journals publications that have emerged from this thesis are summarized in the list below with reference to the corresponding technical chapter.

\begin{itemize}
\item{**Chapter 16**}
\begin{enumerate}
	\item[\\(-\\)]{ L. B. Leene and T. G. Constandinou, ''Ultra-low power design strategy for two-stage amplifier topologies," in Electronics Letters, vol. 50, no. 8, pp. 583-585, April 2014, \href{http://dx.doi.org/10.1049/el.2013.4196} {[Online] doi: 10.1049/el.2013.4196}. }
	\item[\\(-\\)]{ L. B. Leene, Y. Liu and T. G. Constandinou, ''A compact recording array for neural interfaces," IEEE Proceedings of Biomedical Circuits and Systems Conference, pp. 97-100, May 2013, \href{http://dx.doi.org/10.1109/BioCAS.2013.6679648} {[Online] doi: 10.1109/BioCAS.2013.6679648}.}
	\item[\\(-\\)]{ L. Zheng, L. B. Leene, Y. Liu and T. G. Constandinou, ''An adaptive 16/64 kHz, 9-bit SAR ADC with peak-aligned sampling for neural spike recording," IEEE Proceedings of International Symposium on Circuits and Systems, pp. 2385-2388, May 2014, \href{http://dx.doi.org/10.1109/ISCAS.2014.6865652} {[Online] doi: 10.1109/ISCAS.2014.6865652}.}
\end{enumerate}

\item{**Chapter 30**}
\begin{enumerate}
\item[\\(-\\)]{ L. B. Leene and T. G. Constandinou, ''A 2.7\\( \mu\\)W/Mips, 0.88 GOPSmm\\(^2\\) Distributed Processor for Implantable Brain Machine Interfaces," IEEE Proceedings of Biomedical Circuits and Systems Conference, October 2016.}
\end{enumerate}

\item{**Chapter 43**}
\begin{enumerate}
	\item[\\(-\\)]{ L. B. Leene and T. G. Constandinou, ''A 0.45V Continuous Time-Domain Filter using Asynchronous Oscillator Structures," IEEE Proceedings of Electronics Circuits and Systems Conference, December 2016.}
	\item[\\(-\\)]{ M. Elia, L. B. Leene and T. G. Constandinou, ''Continuous-time micropower interface for neural recording applications," IEEE Proceedings of International Symposium on Circuits and Systems, May 2016,\href{http://dx.doi.org/10.1109/ISCAS.2016.7527295} {[Online] doi: 10.1109/ISCAS.2016.7527295}.}
	\item[\\(-\\)]{ K. Faliagkas, L. B. Leene and T. G. Constandinou, ''A novel neural recording system utilising continuous time energy based compression," IEEE Proceedings of International Symposium on Circuits and Systems, pp. 3000-3003, May 2015, \href{http://dx.doi.org/10.1109/ISCAS.2015.7169318} {[Online] doi: 10.1109/ISCAS.2015.7169318}.}
\end{enumerate}

\end{itemize}

# 58 Supplementary Results for the Resource Models

This section will elaborate on some of the analytic findings in Chapter 16 by detailing the derivations and illustrating additional results that emerge from these relations. In particular we will demonstrate the impact of technology related factors to a larger extent that include quantitative measures for some of the more intuitive relations.

# 59 Topology Selection

We first introduced Eq. 18 as a base line for the figure of merit calculations. This reference SAR ADC only dissipates power though the capacitor array and the driving control logic without considering the comparator. We identified the power dissipation in the register logic as;

$$  P_{Register} = 2N   (N+2)   f_s   E_{gate} $$

Eq. 52 simply reflects that a typical SAR operation that resolves N bits requires \\((N+2)\\) per sample inferring the required clock frequency and the standard control logic uses \\(2N\\) gates to perform the binary search operation.

$$  P_{Capacitor \: Array} = E_{search} \cdot f_s C_{unit} V_{ref}^2 (2^{N-2}+2^2) $$

Eq. 53 demonstrates the power dissipation for capacitive switching has three terms. The total amount of capacitance in the DAC is represented as $C_{unit}   (2^{N-2}+2^2)$, the maximum input dynamic range as \\(V^2_{ref}\\), and the average search efficiency for quantization as \\(E_{search}\\). While this dependency is not surprising the term \\(E_{search}\\) needs to be evaluated under the proper assumptions. While we may be inclined to use sinusoidal test signals to extract this parameter if the sensor signals have similar structure but note that this will not reflect an even distribution with respect to the tested input ranges. In this respect triangular ramp test signals are representative to capture even-distribution of output quantization codes.

To realize a model where an analogue pre-amplifier is employed we estimate the power requirements for achieving the required bandwidth for settling. The capacitance for which we evaluate this settling speed is found be considering the output referred noise the results from the capacitor value. These two relations are summarized as follows;

$$  (N+2) f_s   A_{op} \cdot (N+2)   \ln(2) = \frac{I_{amp}}{2 \pi C_{out} \cdot \eta   U_T} $$

The result in Eq. 54 is simply derived from the unity-gain frequency that needs to exceed the clock rate in excess related to the settling requirement that scales by $(N+2)   \ln(2)$.

$$  \frac{V_{ref}}{2^{N+2}} = √{\frac{\zeta}{\eta} \cdot \frac{kT}{C_{amp}}} $$

Here we again refer to \\(\zeta\\) as the amplifier noise excess factor introduced in Eq. 7. After some simplification by taking the most significant terms we arrive at Eq. 19 but evaluated here in full as;

$$  P_{amp} = 32 \pi   \ln(2) \cdot \frac{ \left( U_T   (N+2)   2^N \right)^2 }{V_{ref}   q} \cdot A_{ol} f_s NEF^2 $$

Similarly we derive the power for the dynamic latch type comparator following closely the analysis of [^134]. The derivation for estimating the additional components for the hybrid data converter follows similarly to the pre-amp case where the bandwidth of the integrators is now also related to the order of oversampling but not that of settling. In particular we estimate the output referred noise of the first and most power intensive integrator as;

$$  (1+2^{N-K})   FIR   f_s = \frac{I_{int}}{2 \pi C_{int} \cdot \eta   U_T} $$

Eq. 57 simply evaluates the integration factor required to achieve a consistent output swing irrespective of SAR resolution. This shows us that the input signal level heavily dictates the corresponding biasing current \\(I_{int}\\).

$$  \frac{V_{ref}}{2^{N+2}} = √{\frac{\zeta}{\eta} \cdot \frac{kT}{C_{int}}} $$

Similarly Eq. 58 relates the integration capacitance to the expected output referred noise. Summarizing these assertions gives us a direct relation between ADC resolution and power dissipation;

$$  P_{amp} = 32 \pi \cdot \frac{ \left( U_T   2^N , NEF\right)^2 }{q   V_{ref}} \cdot FIR  f_s  (1+2^{N-K}) $$

For the sake of clarity in the discussion we estimate the \\(FIR\\) order based on the expected variance from a rectangular window operator. Because this digital filter is estimating a DC component such that any up-modulated white noise power will scale as \\(√{FIR}\\) for such a case and the dependency of a specific window operator will follow this upper bound. This result follows from the maximal dynamic range of real signals for window functions and assert that if we require another \\(K\\) bits to be resolved by the oversampling loop the will need a filter order of \\((K+1)^2\\) to grantee that when using a more effective noise shaping window operator we will achieve the desired noise requirement. Applying a similar estimation on digital power dissipation as before such that;

$$  P_{fir} = \left[(N-K)+ K+\log_2(K-1) \right] \cdot \left(FIR + N-K \right) \cdot f_s E_{gate} $$

Eq. 60 states that the required clock frequency is \\(FIR+N-K\\) and the total number of gates being clocked is \\((N-K)\\) for the SAR operation and \\(K+\log_2(K)\\) for the $\Sigma \Delta$ decimation. For completeness we also note the dissipation of the capacitive DAC is estimated as;

$$  P_{\Sigma \Delta \: Array} = E_{search} \cdot f_s C_{unit} V_{ref}^2 (2^{N-K-2}+2^2+ FIR) $$


While we have extracted many of the empirical parameters that are associated with the implementation presented in Sec 27. Let us consider the impact of parameter variation and reflect on the expectations. This will allow us to evaluate the sensitivity of these parameters with regard to performance measures.

{{< figure src="appendix/C32_V12_a.png}" width="500" >}}
{{< figure src="appendix/C32_V12_b.png}" title="Figure 94:  Summary of the performance merit for each topology." width="500" >}}


First we introduce Fig. 94 which is the normalized case that we presented earlier however here we apply a different scaling with regard to increasing resolution. Here the resolution of the SAR and \\(\Sigma\Delta\\) loop are increased simultaneously which again demonstrates that this topology can provide compact quantization for from 8-10 bits. However because we are using vertical Metal-Insulator-Metal Capacitors provided by the technology that exhibit minimal variance per unit area the unit capacitance \\(C_{unit}\\) is \\(32 fF\\). This is relatively big when compared to very aggressive SAR designs presented in the literature that use unit capacitors of several femto-farad.

{{< figure src="appendix/C4_V12_a.png}" width="500" >}}
{{< figure src="appendix/C4_V12_b.png}" title="Figure 95:  Summary of the performance merit for each topology with a \\(4\times\\) reduction in unit capacitance. " width="500" >}}


{{< figure src="appendix/C4_V06_a.png}" width="500" >}}
{{< figure src="appendix/C4_V06_b.png}" title="Figure 96:  Summary of the performance merit for each topology with a \\(2\times\\) reduction in reference voltage and a \\(4\times\\) reduction in unit Capacitance. " width="500" >}}


This leads into results presented by Fig. 95 where the unit capacitance is reduced to \\(4 fF\\). This illustrates that the hybrid topology has difficulty scaling its power budget because there are significantly more analogue components that the simple structures. In fact if we reduce the power supply from \\(1.2 V\\) to \\(0.6 V\\) the inhibitory analogue scaling that the integrators have exacerbates this effect. Particularly the dynamic comparator structure which has good digital scaling characteristics will allow significantly smaller power dissipation. However in all cases we note that for precision that exceeds \\(60 dB\\) the hybrid data converter topology will allow for a more compact designs.

# 60 System Level Abstraction



As most of the relations presented in Sec. \ref{ch:T1_model} follow naturally from Eq. 25. Here we will provide some additional details regarding our assertions and observations. To show that Eq. 28 represents the expected increase in variance, let us consider the typical gain sensitivity to the variance of our normalized unit capacitor.

$$  \frac{\sigma^2_A}{A_{cl}^2} = \frac{\Delta^2_A - A_{cl}^2}{A_{cl}^2}  \text{where}  \Delta_A = \frac{A + √{A_{cl}} CI   \sigma }{1 + CI  \sigma} $$

This expression is similar to that used in estimating the variance of a capacitive DAC in Eq. 16. \\(\Delta_A\\) represents the expected gain deviation from the mean that relates to our confidence interval \\(CI\\). Strictly there are only two components that attribute to gain variance which are the input and the feedback capacitors. These contributions have exactly a ratio of \\(√{A_{cl}}\\) for their respective variances. Expanding this result will reveal;

$$  \frac{\sigma^2_A}{A_{cl}^2} = \sigma   CI \cdot \frac{2   ( A_{cl} - √{ A_{cl} } ) + \sigma   CI ( 1 - A_{cl} ) } {A_{cl} \left( \sigma   CI + 1  \right)^2 } \approx \sigma   CI \cdot \left( 2  - \frac{2}{√{A_{cl}}} \right) $$

For exceedingly larger \\(A_{cl}\\) it makes sense to take the higher order terms however instead we chose include the \\(√{A_{cl}}\\) term to considering the design of low-gain multi-stage configurations. Since the typical deviation of $\sigma CI$ is on the order of several percent it is conceivable that these higher order terms have vanishing contribution irrespective of gain. In order to compensate the increased variance the capacitor sizes need to be adjusted proportionally to that of the change standard deviation. This results in the penalty factor accumulated from every stage as Eq. 28.  

{{< figure src="appendix/LG-NP.png}" width="500" >}}
{{< figure src="appendix/LG-PAP.png}" title="Figure 97:  Normalized resource redistribution dependency in low gain settings \\(G_T=200\\). " width="500" >}}


The results in Fig. 97 show that particularly in low gain settings that relate to smaller \\(V_{DD}\\) configurations the resource distribution becomes more important. This is because the individual gain of each stage is low resulting in very poor noise figures for minimal area configurations. With conventional structures we see that multi-state topologies can benefit greatly from this factor primarily because the baseline performance is much worse than single or two-stage structures.

{{< figure src="appendix/area-R21-B32-sigma.png}" width="500" >}}
{{< figure src="appendix/area-R21-B32-snr.png}" title="Figure 98:  System area requirement for two-Stage/single-Pole (red) and three-stage/double-pole (green) amplifier/filter structures. " width="500" >}}


Fig. 98 reveals some of the more intuitive details associated with gain matching and ADC SNR performance with quantitative measures. In a) we observe the general inverse proportionality that gain matching exhibits with regard to capacitor are requirement. We point out that it can be marginally reduced by reducing \\(G_T\\) or equivalently the supply voltage. On the other hand in b) we see that reducing \\(G_T\\) by increasing the ADC dynamic range is more effective of a solution when we do not consider the associated increase in power dissipation.

{{< figure src="appendix/PAP-AIRN.png" title="Figure 99:  Detailed dependency with regard to system supply voltage and the precision of the two-stage/single-pole (red) and three-stage/double-Pole (green) amplifier/filter structures. " width="500" >}}


Fig. 99 demonstrates a more generic result when the amplifier power budget and gain configuration is actively matching the dynamic range of the ADC. Neglecting linearity we observe that there is an interesting strategy for selecting the appropriate supply voltage in accordance to the targeted ADC resolution. Similarly we make the assertion that there is gain-varience, quantization limited, and linearity limited regimes in each extrema of this graph that will bound viable implementations.

# 61 Transistor level implementation

For clarity the transistor level implementation is detailed here in terms of the transistor sizing.

{{< figure src="appendix/SIZE1.pdf" title="Figure 100: Transistor sizing for the two stage operational amplifier with bandwidth boosting implemented in 0.18\\(\mu\\)m CMOS. Sizing units shown are in microns.}\label{fig:A1_S1" width="500" >}}


{{< figure src="appendix/SIZE2.pdf" title="Figure 101: Transistor sizing for the fully differential $\Delta\Sigma SAR$ switched loop filter implemented in 0.18\\(\mu\\)m CMOS. Sizing units shown are in microns.}\label{fig:A1_S2" width="500" >}}


{{< figure src="appendix/SIZE3.pdf" title="Figure 102: Transistor sizing for the differential low noise complementary instrumentation amplifier implemented in 0.18\\(\mu\\)m CMOS. Sizing units shown are in microns.}\label{fig:A1_S3" width="500" >}}


{{< figure src="appendix/SIZE4.pdf" title="Figure 103: Transistor sizing for the fully differential time domain instrumentation amplifier implemented in 0.18\\(\mu\\)m CMOS. Sizing units shown are in microns.}\label{fig:A1_S4" width="500" >}}


{{< figure src="appendix/SIZE5.pdf" title="Figure 104: Transistor sizing for the time domain instrumentation high pass filter structure implemented in 0.18\\(\mu\\)m CMOS. Sizing units shown are in microns.}\label{fig:A1_S5" width="500" >}}


{{< figure src="appendix/SIZE6.pdf" title="Figure 105: Transistor sizing for the differential time domain filter implemented in 0.18\\(\mu\\)m CMOS. Sizing units shown are in microns.}\label{fig:A1_S6" width="500" >}}

# 62 Supplementary Results for Classification Methods

This section will detail the signal characteristics found in the data sets used extensively for validating the methods proposed here. We will exemplify some of the signal features and demonstrate the implementation of the proposed methods with Matlab code.

# 63 Signal Characteristics

As was mentioned used evaluation recordings contains different sets of synthetically generated spike trains for three classes of neurons each with different spike morphologies. The spike shapes are based on recordings with background noise of similar spikes randomly distributed in time at lower amplitudes. While the these datasets provide time stamp data for when the individual spike wave forms can be found in the recording they do not introduce the low-frequency content that is expected from typical recording. Here we have extracted these low frequency variations from real recordings with a high order FIR filter and added them to the synthetic data. While this will not greatly effect the classification results it assures us that the proposed methods are not inadvertently sensitive to low-frequency components.

{{< figure src="appendix/synthetic_rawa.pdf}" width="500" >}}
{{< figure src="appendix/synthetic_rawb.pdf}" title="Figure 106: Example of synthetic data derived from typical neural recordings." width="500" >}}


Fig. 106 depicts the typical recordings that are used before preprocessing. Whether we extract the finer signal components in the digital domain or in the analogue domain it is necessary to carefully consider the possible dynamic range. Particularly as buffer overflows are not explicitly modelled unless hardware specific data types are used.

{{< figure src="appendix/synthetic_filta.pdf}" width="500" >}}
{{< figure src="appendix/synthetic_filtb.pdf}" title="Figure 107: Filtered components of spiking activity and detection operator output." width="500" >}}


Once the spiking activity is extracted it may appear like that in Fig. 107. Because spikes have a board bandwidth relative to the sampling rate, the white noise is typically more evident than what is presented. Alongside the spiking waveform we present the energy operator. Here there is a clear difference in how apparent the noise is in contrast to the spike amplitude. This disparity improves the more energy each spike had in the high-frequency bands.

{{< figure src="appendix/spike_analoga.pdf}" width="500" >}}
{{< figure src="appendix/spike_digitala.pdf}" title="Figure 108:  Comparison of digital and analogue pre-filtering methods. " width="500" >}}


Fig. 108 compares the characteristic difference between analogue and digital filtering strategies. While we typically expect the group delay is well controlled in digital systems the analogue implementation exhibits more systematic rejection of out of band components. Low order FIR structures in particular suffer from limited leaking these components but allow finer adjustments that accentuate separating features in the signal.

{{< figure src="appendix/spike_analogb.pdf}" width="500" >}}
{{< figure src="appendix/spike_digitalb.pdf}" title="Figure 109:  Comparison of digital and analogue detection methods." width="500" >}}


Similarly Fig. 109 compares the digital and analogue realizations of the detection operators. Since we only use linear blocks to realize the analogue operator we lose the suppression of white noise. Moreover the digital operator can fine tune delay used to correlate derivative with amplitude components allowing for a very explicit single maximum in each waveform.

{{< figure src="appendix/synthetic_spikes.pdf" title="Figure 110: Colour coded spike-waveforms for 16-sample spike windows where the three classes of neurons are coloured (ref,blue,green) and the false positives labelled (black)." width="500" >}}


Finally we illustrate a sub-set of aggregate waveforms captured by the digital methods in Fig. 110. This data is used in the RVD and template-matching methods.

# 64 Implementation structure

Here we will detail the Matlab code implementation for the proposed methods which were used for validation in association with the data. Note alpha represent the smallest representable value which reflects the depth of the registers.

## 65 Introducing noise and LFP content

This code section exemplifies the method by which noise is systematically added to each recording in addition to LFP content. We note that the synthetic spike trains have well defined average rates and consistent amplitudes which allows the additive noise to remain consistent across all tests.

\begin{lstlisting}[language=Matlab]
load(LFP_content)
LFP.Time=LFP.Time-min(LFP.Time);
load(SpikeTrain_dataset)

scale=3;
lpflt = designfilt('lowpassiir', 'FilterOrder', 1,     		...
'HalfPowerFrequency', 6500, 'SampleRate',            		...
scale*10^(3)/samplingInterval, 'DesignMethod', 'butter');

AT=resample(LFP,[1:size(data,2)].*(samplingInterval*10^(-3)));
rdata=awgn(resample(data(1:size(data,2))',scale,2),snr);
rdata=rdata+resample(AT.Data,scale,2);

rdata=filter(lpflt,rdata);
\end{lstlisting}

## 66 Analogue detection operator



The analogue detection operator simply operated on the bandpass filtered sub-components of the original signal and tracks a means threshold at three times that of the average. Because we specifically upsample the waveform sectioning it make sense that the adaptive threshold updates close or below the Nyquist frequency in order to capture slowly varying changed in spiking intensity.

\begin{lstlisting}[language=Matlab]
i=34;
while(i<TS)
i=i+1;
	%Update Threshold value at low frequency
	if(mod(i,128)==0)
			if(2.5.*made(i)>mei)
			mei=mei+alpha;
			else
			mei=mei-alpha;
			end
		%Set treshold at 3x rms with minimum at  0.01
		drms=3*mei+1/64;
	end
	%Upon peak-detection above threshold process data
	if(made(i)>drms && made(i)>made(i+1))
		G(1:200,k)=rdata(i-32:i+167);
		IDX(k)=i*2/scale;
		k=k+1;
		i=i+180;
	end
end
\end{lstlisting}

## 67 Digital detection operator



The digital operator is slightly more sophisticated as it is not sensitive to the rate or spiking when estimating its threshold. While we similarly remove low-frequency content equivalent to the analogue filters. The threshold updates are only performed upon detecting peaks in the energy operator.

\begin{lstlisting}[language=Matlab]
while(i<TS)
	i=i+1;
	%track low-frequency signal
	trv=trv+(rdata(i)-trv)/32;
	%Perform IIR + FIR filtering
	T(i)=rdata(i)-trv+T(i-1).*0.25;
	G(i)= T(i-a3:i)*FIR;
	%Estimate spiking energy and track its noise
	DO(i)=abs((0.25+G(i)).*T(i-round(a3/2+1)));
	nest=nest+(a2*DO(i)-nest)/512;
	if(cnt<9)
		%if new local minima is detected reset analysis else continue
		if(DO(i)>lm)
			lm=DO(i);
			thv = thv + (a1*nest+DO(i)-a1*thv)/512;
			F(k,1:8)=G(i+[-10:2:-4 -3:0]);
			cnt=1;
		else
			F(k,8+cnt)=G(i);
			cnt=cnt+1;
		end
	elseif(cnt<scale*15)
		%do signal analysis clasification here
		cnt=cnt+1;
	elseif(DO(i) > thv )
		%upon detecting threshold crossing initialize buffers
		lm=DO(i);
		k=k+1;
		thv = thv + (a1*nest+DO(i-2)-a1*thv)/512;
		F(k,1:8)=G(i+[-10:2:-4 -3:0]);
		cnt=1;
	end
end
\end{lstlisting}

## 68 \\(\Omega_3\\) optimization



The mixed signal optimization that selected the best sections in the aggregate waveforms is performed iteratively. Here we simply introduce normalization factors K and section pointers T.

\begin{lstlisting}[language=Matlab]
for i = repmat(1:size(G,2),1,1)
	% for each \\(\Omega\\) feature find the best section
	for j = 1:3
		%offset with reference point
		ref=3.*sum(G(RP(j),i));
		%integrate current section current section
		rng=round(K(j)*10)+1;
		acc=sum(G([-rng:rng]+round(T(j)),i));
		%nomalize the integration to reference
		if(ref < acc && K(j) > 0.1)
			K(j)=K(j) - alpha;
		elseif(K(j)<1)
			K(j)=K(j) + alpha;
		end
		%Compare signal deviation and increment on sections
		G1=abs(ref-sum(G([-rng:rng]+round(T(j)+2),i)));
		G2=abs(ref-sum(G([-rng:rng]+round(T(j)-2),i)));
		if(T(j)>70 && G2>G1)
			T(j)=T(j)-alpha;
		elseif(T(j)<90 && G1>G2)
			T(j)=T(j)+alpha;
		end
	end
end
\end{lstlisting}

## 69 K-means with centroid splitting



Here we present the means by which we explicitly multiplex active clusters and the iterative splitting of each centroid.

\begin{lstlisting}[language=Matlab]
seed=randi(size(F,1)-5,1);
U(1:4,:)=F(seed+[1:4],:);
for NM=[1, 2, 4]
	%if new iteration duplicate new centroid from previous
	switch NM
		case 2
			U(2,:)=U(1,:)-ones(1,size(U,2)).*alpha;
		case 4
			U(3,:)=U(1,:)-ones(1,size(U,2)).*alpha;
			U(4,:)=U(2,:)-ones(1,size(U,2)).*alpha;
	end
	% Track centroids using data in F
	for i = repmat(1:size(F,1),1,1)
		%multiplex centroid adjustment
		if(CS==0)
			CA=mod(CA,NM)+1;
		end
		CS=mod(CS+1,4);
		[dist, mc]=min(sum(abs(repmat(F(i,:),NM,1)'-U(1:NM,:)')));
		%if current centroid is minimum then adjust
		if(CA==mc)
			U(mc,:)=U(mc,:)+sign(F(i,:)-U(mc,:) ).*alpha;
		end
	end
end
\end{lstlisting}

## 70 Recursive variance decomposition



Similarly this implementation realizes the estimation of loading vectors that provide a basis for the spikes in F.

\begin{lstlisting}[language=Matlab]
for i = repmat(1:size(F,1),1,1)
	%First track mean xu and first loading vetor s1
	for j = 1:size(F,2)
		d(j) = F(i,j)-xu(j);
		xu(j) = xu(j) + sign(d(j)-xu(j))*alpha;
		ad(j) = abs(d(j));
		s1(j) = s1(j) + sign(ad(j).*g1-s1(j))*alpha*2;
	end
	%get dot product s and project on it-self to check gain g1
	s=ad*s1;
	if( (ad'-s1.*(s))'*s1 > 0 )g1=g1+alpha;
		else g1=g1-alpha;
	end
	%using varience residues esitimate second loading vector s2
	for j = 1:size(F,2)
		ad(j) = ad(j)-s1(j).*s;
		s2(j) = s2(j) + sign(ad(j).*g2-s2(j))*alpha*2;
	end
	%get dot product of s2 and project to normalize with g2
	s=ad*s2;
	if( (ad'-s2.*(s))'*s2 > 0 )
		g2=g2+alpha;
	else
		g2=g2-alpha;
	end
end
\end{lstlisting}





# References:

[^1]: R.Q. Quiroga, Z.Nadasdy, and Y.Ben-Shaul, ''Unsupervised spike detection and  sorting with wavelets and superparamagnetic clustering,'' Neural  Computation, vol.16, pp. 1661--1687, April 2004. [Online]:  http://dx.doi.org/10.1162/089976604774201631
[^2]: R.A. Normann, ''Technology insight: future neuroprosthetic therapies for  disorders of the nervous system,'' Nature Clinical Practice Neurology,  vol.3, pp. 444--452, August 2007. [Online]:  http://dx.doi.org/10.1038/ncpneuro0556
[^3]: K.Birmingham, V.Gradinaru, P.Anikeeva, W.M. Grill, B.Pikov,  VictorMcLaughlin, P.Pasricha, K.Weber, DouglasLudwig, and K.Famm,  ''Bioelectronic medicines: a research roadmap,'' Nature Reviews Drug  Discovery, vol.13, pp. 399--400, May 2014. [Online]:  http://dx.doi.org/10.1038/nrd4351
[^4]: ''Bridging the bio-electronic divide,'' Defense Advanced Research Projects  Agency, Arlington, Texas, January 2016. [Online]:  http://www.darpa.mil/news-events/2015-01-19
[^5]: G.Fritsch and E.Hitzig, ''ber die elektrische erregbarkeit des grosshirns,''  Archiv für Anatomie, Physiologie und Wissenschaftliche Medicin.,  vol.37, pp. 300--332, 1870.
[^6]: G.E. Loeb, ''Cochlear prosthetics,'' Annual Review of Neuroscience,  vol.13, no.1, pp. 357--371, 1990, pMID: 2183680. [Online]:  http://dx.doi.org/10.1146/annurev.ne.13.030190.002041
[^7]: ''Annual update bcig uk cochlear implant provision,'' British Cochlear Implant  Group, London WC1X 8EE, UK, pp. 1--2, March 2015. [Online]:  http://www.bcig.org.uk/wp-content/uploads/2015/12/CI-activity-2015.pdf
[^8]: M.Alexander, ''Neuro-numbers,'' Association of British Neurologists (ABN),  London SW9 6WY, UK, pp. 1--12, April 2003. [Online]:  http://www.neural.org.uk/store/assets/files/20/original/NeuroNumbers.pdf
[^9]: A.Jackson and J.B. Zimmermann, ''Neural interfaces for the brain and spinal  cord — restoring motor function,'' Nature Reviews Neurology, vol.8,  pp. 690--699, December 2012. [Online]:  http://dx.doi.org/10.1038/nrneurol.2012.219
[^10]: M.Gilliaux, A.Renders, D.Dispa, D.Holvoet, J.Sapin, B.Dehez,  C.Detrembleur, T.M. Lejeune, and G.Stoquart, ''Upper limb robot-assisted  therapy in cerebral palsy: A single-blind randomized controlled trial,''  Neurorehabilitation AND Neural Repair, vol.29, no.2, pp. 183--192,  February 2015. [Online]:  http://nnr.sagepub.com/content/29/2/183.abstract
[^11]: P.Osten and T.W. Margrie, ''Mapping brain circuitry with a light  microscope,'' Nature Methods, vol.10, pp. 515--523, June 2013.  [Online]: http://dx.doi.org/10.1038/nmeth.2477
[^12]: S.M. Gomez-Amaya, M.F. Barbe, W.C. deGroat, J.M. Brown, J.Tuite, Gerald  F.ANDCorcos, S.B. Fecho, A.S. Braverman, and M.R. RuggieriSr, ''Neural  reconstruction methods of restoring bladder function,'' Nature Reviews  Urology, vol.12, pp. 100--118, February 2015. [Online]:  http://dx.doi.org/10.1038/nrurol.2015.4
[^13]: H.Yu, W.Xiong, H.Zhang, W.Wang, and Z.Li, ''A parylene self-locking cuff  electrode for peripheral nerve stimulation and recording,'' IEEE/ASME  Journal of Microelectromechanical Systems, vol.23, no.5, pp. 1025--1035,  Oct 2014. [Online]: http://dx.doi.org/10.1109/JMEMS.2014.2333733
[^14]: J.S. Ho, S.Kim, and A.S.Y. Poon, ''Midfield wireless powering for  implantable systems,'' Proceedings of the IEEE, vol. 101, no.6, pp.  1369--1378, June 2013. [Online]:  http://dx.doi.org/10.1109/JPROC.2013.2251851
[^15]: R.D. KEYNES, ''Excitable membranes,'' Nature, vol. 239, pp. 29--32,  September 1972. [Online]: http://dx.doi.org/10.1038/239029a0
[^16]: A.D. Grosmark and G.Buzs\'aki, ''Diversity in neural firing dynamics  supports both rigid and learned hippocampal sequences,'' Science, vol.  351, no. 6280, pp. 1440--1443, March 2016. [Online]:  http://science.sciencemag.org/content/351/6280/1440
[^17]: B.Sakmann and E.Neher, ''Patch clamp techniques for studying ionic channels  in excitable membranes,'' Annual Review of Physiology, vol.46, no.1,  pp. 455--472, October 1984, pMID: 6143532. [Online]:  http://dx.doi.org/10.1146/annurev.ph.46.030184.002323
[^18]: M.P. Ward, P.Rajdev, C.Ellison, and P.P. Irazoqui, ''Toward a comparison of  microelectrodes for acute and chronic recordings,'' Brain Research,  vol. 1282, pp. 183 -- 200, July 2009. [Online]:  http://www.sciencedirect.com/science/article/pii/S0006899309010841
[^19]: J.E.B. Randles, ''Kinetics of rapid electrode reactions,'' Discuss.  Faraday Soc., vol.1, pp. 11--19, 1947. [Online]:  http://dx.doi.org/10.1039/DF9470100011
[^20]: M.E. Spira and A.Hai, ''Multi-electrode array technologies for neuroscience  and cardiology,'' Nature Nanotechnology, vol.8, pp. 83 -- 94,  February 2013. [Online]: http://dx.doi.org/10.1038/nnano.2012.265
[^21]: G.E. Moore, ''Cramming more components onto integrated circuits,''  Proceedings of the IEEE, vol.86, no.1, pp. 82--85, January 1998.  [Online]: http://dx.doi.org/10.1109/JPROC.1998.658762
[^22]: I.Ferain, C.A. Colinge, and J.-P. Colinge, ''Multigate transistors as the  future of classical metal-oxide-semiconductor field-effect transistors,''  Nature, vol. 479, pp. 310--316, November 2011. [Online]:  http://dx.doi.org/10.1038/nature10676
[^23]: I.H. Stevenson and K.P. Kording, ''How advances in neural recording affect  data analysis,'' Nature neuroscience, vol.14, no.2, pp. 139--142,  February 2011. [Online]: http://dx.doi.org/10.1038/nn.2731
[^24]: C.Thomas, P.Springer, G.Loeb, Y.Berwald-Netter, and L.Okun, ''A miniature  microelectrode array to monitor the bioelectric activity of cultured cells,''  Experimental cell research, vol.74, no.1, pp. 61--66, September  1972. [Online]: http://dx.doi.org/0.1016/0014-4827(72)90481-8
[^25]: R.A. Andersen, E.J. Hwang, and G.H. Mulliken, ''Cognitive neural  prosthetics,'' Annual review of Psychology, vol.61, pp. 169--190,  December 2010, pMID: 19575625. [Online]:  http://dx.doi.org/10.1146/annurev.psych.093008.100503
[^26]: L.A. Jorgenson, W.T. Newsome, D.J. Anderson, C.I. Bargmann, E.N. Brown,  K.Deisseroth, J.P. Donoghue, K.L. Hudson, G.S. Ling, P.R. MacLeish  etal., ''The brain initiative: developing technology to catalyse  neuroscience discovery,'' Philosophical Transactions of the Royal  Society of London B: Biological Sciences, vol. 370, no. 1668, p. 20140164,  2015.
[^27]: E.DAngelo, G.Danese, G.Florimbi, F.Leporati, A.Majani, S.Masoli,  S.Solinas, and E.Torti, ''The human brain project: High performance  computing for brain cells hw/sw simulation and understanding,'' in  Proceedings of the Digital System Design Conference, August 2015, pp.  740--747. [Online]: http://dx.doi.org/10.1109/DSD.2015.80
[^28]: K.Famm, B.Litt, K.J. Tracey, E.S. Boyden, and M.Slaoui, ''Drug discovery:  a jump-start for electroceuticals,'' Nature, vol. 496, no. 7444, pp.  159--161, April 2013. [Online]: http://dx.doi.org/0.1038/496159a
[^29]: K.Deisseroth, ''Optogenetics,'' Nature methods, vol.8, no.1, pp.  26--29, January 2011. [Online]: http://dx.doi.org/10.1038/nmeth.f.324
[^30]: M.Velliste, S.Perel, M.C. Spalding, A.S. Whitford, and A.B. Schwartz,  ''Cortical control of a prosthetic arm for self-feeding,'' Nature,  vol. 453, no. 7198, pp. 1098--1101, June 2008. [Online]:  http://dx.doi.org/10.1038/nature06996
[^31]: T.N. Theis and P.M. Solomon, ''In quest of the "next switch" prospects for  greatly reduced power dissipation in a successor to the silicon field-effect  transistor,'' Proceedings of the IEEE, vol.98, no.12, pp.  2005--2014, December 2010. [Online]:  http://dx.doi.org/10.1109/JPROC.2010.2066531
[^32]: G.M. Amdahl, ''Validity of the single processor approach to achieving large  scale computing capabilities, reprinted from the afips conference  proceedings, vol. 30 (atlantic city, n.j., apr. 18-20), afips press, reston,  va., 1967, pp. 483-485, when dr. amdahl was at international business  machines corporation, sunnyvale, california,'' in AFIPS Conference  Proceedings, Vol. 30 (Atlantic City, N.J., Apr. 18-20), vol.12,  no.3.\hskip 1em plus 0.5em minus 0.4emelax IEEE, Summer 2007, pp. 19--20.  [Online]: http://dx.doi.org/0.1109/N-SSC.2007.4785615
[^33]: J.G. Koller and W.C. Athas, ''Adiabatic switching, low energy computing, and  the physics of storing and erasing information,'' in IEEE Proceedings  of the Workshop on Physics and Computation.\hskip 1em plus 0.5em minus  0.4emelax IEEE, October 1992, pp. 267--270. [Online]:  http://dx.doi.org/10.1109/PHYCMP.1992.615554
[^34]: E.P. DeBenedictis, J.E. Cook, M.F. Hoemmen, and T.S. Metodi, ''Optimal  adiabatic scaling and the processor-in-memory-and-storage architecture (oas  :pims),'' in IEEE Proceedings of the International Symposium on  Nanoscale Architectures.\hskip 1em plus 0.5em minus 0.4emelax IEEE, July  2015, pp. 69--74. [Online]:  http://dx.doi.org/10.1109/NANOARCH.2015.7180589
[^35]: S.Houri, G.Billiot, M.Belleville, A.Valentian, and H.Fanet, ''Limits of  cmos technology and interest of nems relays for adiabatic logic  applications,'' IEEE Transactions on Circuits and Systems---Part I:  Fundamental Theory and Applications, vol.62, no.6, pp. 1546--1554, June  2015. [Online]: http://dx.doi.org/10.1109/TCSI.2015.2415177
[^36]: S.K. Arfin and R.Sarpeshkar, ''An energy-efficient, adiabatic electrode  stimulator with inductive energy recycling and feedback current regulation,''  IEEE Transactions on Biomedical Circuits and Systems, vol.6, no.1,  pp. 1--14, February 2012. [Online]:  http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6036003&isnumber=6138606
[^37]: P.R. Kinget, ''Scaling analog circuits into deep nanoscale cmos: Obstacles and  ways to overcome them,'' in IEEE Proceedings of the Custom Integrated  Circuits Conference.\hskip 1em plus 0.5em minus 0.4emelax IEEE, September  2015, pp. 1--8. [Online]: http://dx.doi.org/10.1109/CICC.2015.7338394
[^38]: K.Bernstein, D.J. Frank, A.E. Gattiker, W.Haensch, B.L. Ji, S.R. Nassif,  E.J. Nowak, D.J. Pearson, and N.J. Rohrer, ''High-performance cmos  variability in the 65-nm regime and beyond,'' IBM Journal of Research  AND Development, vol.50, no. 4.5, pp. 433--449, July 2006. [Online]:  http://dx.doi.org/10.1147/rd.504.0433
[^39]: L.L. Lewyn, T.Ytterdal, C.Wulff, and K.Martin, ''Analog circuit design in  nanoscale cmos technologies,'' Proceedings of the IEEE, vol.97,  no.10, pp. 1687--1714, October 2009. [Online]:  http://dx.doi.org/10.1109/JPROC.2009.2024663
[^40]: Y.Xin, W.X.Y. Li, Z.Zhang, R.C.C. Cheung, D.Song, and T.W. Berger, ''An  application specific instruction set processor (asip) for adaptive filters in  neural prosthetics,'' IEEE/ACM Transactions on Computational Biology  and Bioinformatics, vol.12, no.5, pp. 1034--1047, September 2015.  [Online]: http://dx.doi.org/10.1109/TCBB.2015.2440248
[^41]: G.Schalk, P.Brunner, L.A. Gerhardt, H.Bischof, and J.R. Wolpaw,  ''Brain-computer interfaces (bcis): detection instead of classification,''  Journal of neuroscience methods, vol. 167, no.1, pp. 51--62, 2008,  brain-Computer Interfaces (BCIs). [Online]:  http://www.sciencedirect.com/science/article/pii/S0165027007004116
[^42]: Z.Li, J.E. O'Doherty, T.L. Hanson, M.A. Lebedev, C.S. Henriquez, and M.A.  Nicolelis, ''Unscented kalman filter for brain-machine interfaces,''  PloS one, vol.4, no.7, pp. 1--18, 2009. [Online]:  http://dx.doi.org/10.1371/journal.pone.0006243
[^43]: A.L. Orsborn, H.G. Moorman, S.A. Overduin, M.M. Shanechi, D.F. Dimitrov,  and J.M. Carmena, ''Closed-loop decoder adaptation shapes neural plasticity  for skillful neuroprosthetic control,'' Neuron, vol.82, pp. 1380 --  1393, March 2016. [Online]:  http://dx.doi.org/10.1016/j.neuron.2014.04.048
[^44]: Y.Yan, X.Qin, Y.Wu, N.Zhang, J.Fan, and L.Wang, ''A restricted boltzmann  machine based two-lead electrocardiography classification,'' in IEEE  Proceedings of the International Conference on Wearable and Implantable Body  Sensor Networks.\hskip 1em plus 0.5em minus 0.4emelax IEEE, June 2015, pp.  1--9. [Online]: http://dx.doi.org/10.1109/BSN.2015.7299399
[^45]: B.M. Yu and J.P. Cunningham, ''Dimensionality reduction for large-scale  neural recordings,'' Nature Neuroscience, vol.17, pp. 1500 -- 1509,  November 2014. [Online]: http://dx.doi.org/10.1038/nn.3776
[^46]: S.Makeig, C.Kothe, T.Mullen, N.Bigdely-Shamlo, Z.Zhang, and  K.Kreutz-Delgado, ''Evolving signal processing for brain: Computer  interfaces,'' Proceedings of the IEEE, vol. 100, no. Special  Centennial Issue, pp. 1567--1584, May 2012. [Online]:  http://dx.doi.org/10.1109/JPROC.2012.2185009
[^47]: G.Indiveri and S.C. Liu, ''Memory and information processing in neuromorphic  systems,'' Proceedings of the IEEE, vol. 103, no.8, pp. 1379--1397,  August 2015. [Online]: http://dx.doi.org/10.1109/JPROC.2015.2444094
[^48]: Y.Chen, E.Yao, and A.Basu, ''A 128-channel extreme learning machine-based  neural decoder for brain machine interfaces,'' IEEE Transactions on  Biomedical Circuits and Systems, vol.10, no.3, pp. 679--692, June 2016.  [Online]: http://dx.doi.org/10.1109/TBCAS.2015.2483618
[^49]: V.Karkare, S.Gibson, and D.Marković, ''A 75- $\mu$w, 16-channel neural  spike-sorting processor with unsupervised clustering,'' IEEE Journal  of Solid-State Circuits, vol.48, no.9, pp. 2230--2238, September 2013.  [Online]: http://dx.doi.org/10.1109/JSSC.2013.2264616
[^50]: T.C. Chen, W.Liu, and L.G. Chen, ''128-channel spike sorting processor with  a parallel-folding structure in 90nm process,'' in IEEE Proceedings  of the International Symposium on Circuits and Systems, May 2009, pp.  1253--1256. [Online]: http://dx.doi.org/10.1109/ISCAS.2009.5117990
[^51]: G.Baranauskas, ''What limits the performance of current invasive brain machine  interfaces?'' Frontiers in Systems Neuroscience, vol.8, no.68, April  2014. [Online]:  http://www.frontiersin.org/systems_neuroscience/10.3389/fnsys.2014.00068
[^52]: E.F. Chang, ''Towards large-scale, human-based, mesoscopic  neurotechnologies,'' Neuron, vol.86, pp. 68--78, March 2016.  [Online]: http://dx.doi.org/10.1016/j.neuron.2015.03.037
[^53]: M.A.L. Nicolelis and M.A. Lebedev, ''Principles of neural ensemble  physiology underlying the operation of brain-machine,'' Nature Reviews  Neuroscience, vol.10, pp. 530--540, July 2009. [Online]:  http://dx.doi.org/10.1038/nrn2653
[^54]: Z.Fekete, ''Recent advances in silicon-based neural microelectrodes and  microsystems: a review,'' Sensors AND Actuators B: Chemical, vol. 215,  pp. 300 -- 315, 2015. [Online]:  http://www.sciencedirect.com/science/article/pii/S092540051500386X
[^55]: N.Saeidi, M.Schuettler, A.Demosthenous, and N.Donaldson, ''Technology for  integrated circuit micropackages for neural interfaces, based on  gold–silicon wafer bonding,'' Journal of Micromechanics AND  Microengineering, vol.23, no.7, p. 075021, June 2013. [Online]:  http://stacks.iop.org/0960-1317/23/i=7/a=075021
[^56]: K.Seidl, S.Herwik, T.Torfs, H.P. Neves, O.Paul, and P.Ruther,  ''Cmos-based high-density silicon microprobe arrays for electronic depth  control in intracortical neural recording,'' IEEE Journal of  Microelectromechanical Systems, vol.20, no.6, pp. 1439--1448, December  2011. [Online]:  http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6033040&isnumber=6075219
[^57]: T.D.Y. Kozai, N.B. Langhals, P.R. Patel, X.Deng, H.Zhang, K.L. Smith,  J.Lahann, N.A. Kotov, and D.R. Kipke, ''Ultrasmall implantable composite  microelectrodes with bioactive surfaces for chronic neural interfaces,''  Nature Materials, vol.11, pp. 1065--1073, December 2012. [Online]:  http://dx.doi.org/10.1038/nmat3468
[^58]: D.A. Schwarz, M.A. Lebedev, T.L. Hanson, D.F. Dimitrov, G.Lehew, J.Meloy,  S.Rajangam, V.Subramanian, P.J. Ifft, Z.Li, A.Ramakrishnan, A.Tate,  K.Z. Zhuang, and M.A.L. Nicolelis, ''Chronic, wireless recordings of  large-scale brain activity in freely moving rhesus monkeys,'' Nature  Methods, vol.11, pp. 670--676, April 2014. [Online]:  http://dx.doi.org/10.1038/nmeth.2936
[^59]: P.Ruther, S.Herwik, S.Kisban, K.Seidl, and O.Paul, ''Recent progress in  neural probes using silicon mems technology,'' IEEJ Transactions on  Electrical and Electronic Engineering, vol.5, no.5, pp. 505--515, 2010.  [Online]: http://dx.doi.org/10.1002/tee.20566
[^60]: ibitem3d-printH.-W. Kang, S.J. Lee, I.K. Ko, C.Kengla, J.J. Yoo, and A.Atala, ''A 3d  bioprinting system to produce human-scale tissue constructs with structural  integrity,'' Nature Biotechnology, vol.34, pp. 312--319, March 2016.  [Online]: http://dx.doi.org/10.1038/nbt.3413
[^61]: ibitemdistrib-electC.Xie, J.Liu, T.-M. Fu, X.Dai, W.Zhou, and C.M. Lieber,  ''Three-dimensional macroporous nanoelectronic networks as minimally invasive  brain probes,'' Nature Materials, vol.14, pp. 1286--1292, May 2015.  [Online]: http://dx.doi.org/10.1038/nmat4427
[^62]: R.R. Harrison, P.T. Watkins, R.J. Kier, R.O. Lovejoy, D.J. Black,  B.Greger, and F.Solzbacher, ''A low-power integrated circuit for a wireless  100-electrode neural recording system,'' IEEE Journal of Solid-State  Circuits, vol.42, no.1, pp. 123--133, Jan 2007. [Online]:  http://dx.doi.org/10.1109/JSSC.2006.886567
[^63]: J.Guo, W.Ng, J.Yuan, S.Li, and M.Chan, ''A 200-channel  area-power-efficient chemical and electrical dual-mode acquisition ic for the  study of neurodegenerative diseases,'' IEEE Transactions on  Biomedical Circuits and Systems, vol.10, no.3, pp. 567--578, June 2016.  [Online]: http://dx.doi.org/10.1109/TBCAS.2015.2468052
[^64]: W.Biederman, D.J. Yeager, N.Narevsky, J.Leverett, R.Neely, J.M. Carmena,  E.Alon, and J.M. Rabaey, ''A 4.78 mm 2 fully-integrated neuromodulation soc  combining 64 acquisition channels with digital compression and simultaneous  dual stimulation,'' IEEE Journal of Solid-State Circuits, vol.50,  no.4, pp. 1038--1047, April 2015. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2384736
[^65]: R.Muller, S.Gambini, and J.M. Rabaey, ''A 0.013mm$^2$, $5 \mu w$,  dc-coupled neural signal acquisition ic with 0.5v supply,'' IEEE  Journal of Solid-State Circuits, vol.47, no.1, pp. 232--243, Jan 2012.  [Online]: http://dx.doi.org/10.1109/JSSC.2011.2163552
[^66]: H.Kassiri, A.Bagheri, N.Soltani, K.Abdelhalim, H.M. Jafari, M.T. Salam,  J.L.P. Velazquez, and R.Genov, ''Battery-less tri-band-radio neuro-monitor  and responsive neurostimulator for diagnostics and treatment of neurological  disorders,'' IEEE Journal of Solid-State Circuits, vol.51, no.5,  pp. 1274--1289, May 2016. [Online]:  http://dx.doi.org/10.1109/JSSC.2016.2528999
[^67]: M.Ballini, J.Müller, P.Livi, Y.Chen, U.Frey, A.Stettler, A.Shadmani,  V.Viswam, I.L. Jones, D.Jäckel, M.Radivojevic, M.K. Lewandowska,  W.Gong, M.Fiscella, D.J. Bakkum, F.Heer, and A.Hierlemann, ''A  1024-channel cmos microelectrode array with 26,400 electrodes for recording  and stimulation of electrogenic cells in vitro,'' IEEE Journal of  Solid-State Circuits, vol.49, no.11, pp. 2705--2719, Nov 2014. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2359219
[^68]: P.D. Wolf, Thermal considerations for the design of an implanted  cortical brain--machine interface (BMI).\hskip 1em plus 0.5em minus  0.4emelax CRC Press Boca Raton, FL, 2008, pMID: 21204402. [Online]:  http://www.ncbi.nlm.nih.gov/books/NBK3932
[^69]: T.Denison, K.Consoer, W.Santa, A.T. Avestruz, J.Cooley, and A.Kelly, ''A  2 $\mu$w 100 nv/rthz chopper-stabilized instrumentation amplifier for chronic  measurement of neural field potentials,'' IEEE Journal of Solid-State  Circuits, vol.42, no.12, pp. 2934--2945, December 2007. [Online]:  http://dx.doi.org/10.1109/JSSC.2007.908664
[^70]: B.Johnson, S.T. Peace, A.Wang, T.A. Cleland, and A.Molnar, ''A 768-channel  cmos microelectrode array with angle sensitive pixels for neuronal  recording,'' IEEE Sensors Journal, vol.13, no.9, pp. 3211--3218,  Sept 2013. [Online]: http://dx.doi.org/10.1109/JSEN.2013.2266894
[^71]: C.M. Lopez, A.Andrei, S.Mitra, M.Welkenhuysen, W.Eberle, C.Bartic,  R.Puers, R.F. Yazicioglu, and G.G.E. Gielen, ''An implantable  455-active-electrode 52-channel cmos neural probe,'' IEEE Journal of  Solid-State Circuits, vol.49, no.1, pp. 248--261, January 2014. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2284347
[^72]: J.Scholvin, J.P. Kinney, J.G. Bernstein, C.Moore-Kochlacs, N.Kopell, C.G.  Fonstad, and E.S. Boyden, ''Close-packed silicon microelectrodes for  scalable spatially oversampled neural recording,'' IEEE Transactions  on Biomedical Engineering, vol.63, no.1, pp. 120--130, Jan 2016. [Online]:  http://dx.doi.org/10.1109/TBME.2015.2406113
[^73]: M.Han, B.Kim, Y.A. Chen, H.Lee, S.H. Park, E.Cheong, J.Hong, G.Han, and  Y.Chae, ''Bulk switching instrumentation amplifier for a high-impedance  source in neural signal recording,'' IEEE Transactions on Circuits  and Systems---Part II: Express Briefs, vol.62, no.2, pp. 194--198, Feb  2015. [Online]: http://dx.doi.org/10.1109/TCSII.2014.2368615
[^74]: R.Muller, S.Gambini, and J.M. Rabaey, ''A 0.013$ $mm$^2$, 5$ \mu$w,  dc-coupled neural signal acquisition ic with 0.5 v supply,'' IEEE  Journal of Solid-State Circuits, vol.47, no.1, pp. 232--243, Jan 2012.  [Online]: http://dx.doi.org/10.1109/JSSC.2011.2163552
[^75]: ''Rhd2164 digital electrophysiology interface chip - data sheet,'' Intan  Technologies, Los Angeles, California, December 2013. [Online]:  http://www.intantech.com/files/Intan_RHD2164_datasheet.pdf
[^76]: K.M. Al-Ashmouny, S.I. Chang, and E.Yoon, ''A 4 $\mu$w/ch analog front-end  module with moderate inversion and power-scalable sampling operation for 3-d  neural microsystems,'' IEEE Transactions on Biomedical Circuits and  Systems, vol.6, no.5, pp. 403--413, October 2012. [Online]:  http://dx.doi.org/10.1109/TBCAS.2012.2218105
[^77]: D.Han, Y.Zheng, R.Rajkumar, G.S. Dawe, and M.Je, ''A 0.45 v 100-channel  neural-recording ic with sub-$\mu$w/channel consumption in 0.18$\mu$m cmos,''  IEEE Transactions on Biomedical Circuits and Systems, vol.7, no.6,  pp. 735--746, December 2013. [Online]:  http://dx.doi.org/10.1109/TBCAS.2014.2298860
[^78]: S.B. Lee, H.M. Lee, M.Kiani, U.M. Jow, and M.Ghovanloo, ''An inductively  powered scalable 32-channel wireless neural recording system-on-a-chip for  neuroscience applications,'' IEEE Transactions on Biomedical Circuits  and Systems, vol.4, no.6, pp. 360--371, Dec 2010. [Online]:  http://dx.doi.org/10.1109/TBCAS.2010.2078814
[^79]: J.Yoo, L.Yan, D.El-Damak, M.A.B. Altaf, A.H. Shoeb, and A.P.  Chandrakasan, ''An 8-channel scalable eeg acquisition soc with  patient-specific seizure classification and recording processor,''  IEEE Journal of Solid-State Circuits, vol.48, no.1, pp. 214--228,  Jan 2013. [Online]: http://dx.doi.org/10.1109/JSSC.2012.2221220
[^80]: M.A.B. Altaf and J.Yoo, ''A 1.83$ \mu$j/classification, 8-channel,  patient-specific epileptic seizure classification soc using a non-linear  support vector machine,'' IEEE Transactions on Biomedical Circuits  and Systems, vol.10, no.1, pp. 49--60, Feb 2016. [Online]:  http://dx.doi.org/10.1109/TBCAS.2014.2386891
[^81]: K.Abdelhalim, H.M. Jafari, L.Kokarovtseva, J.L.P. Velazquez, and R.Genov,  ''64-channel uwb wireless neural vector analyzer soc with a closed-loop phase  synchrony-triggered neurostimulator,'' IEEE Journal of Solid-State  Circuits, vol.48, no.10, pp. 2494--2510, Oct 2013. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2272952
[^82]: A.Bagheri, S.R.I. Gabran, M.T. Salam, J.L.P. Velazquez, R.R. Mansour,  M.M.A. Salama, and R.Genov, ''Massively-parallel neuromonitoring and  neurostimulation rodent headset with nanotextured flexible microelectrodes,''  IEEE Transactions on Biomedical Circuits and Systems, vol.7, no.5,  pp. 601--609, Oct 2013. [Online]:  http://dx.doi.org/10.1109/TBCAS.2013.2281772
[^83]: H.G. Rhew, J.Jeong, J.A. Fredenburg, S.Dodani, P.G. Patil, and M.P.  Flynn, ''A fully self-contained logarithmic closed-loop deep brain  stimulation soc with wireless telemetry and wireless power management,''  IEEE Journal of Solid-State Circuits, vol.49, no.10, pp.  2213--2227, Oct 2014. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2346779
[^84]: W.Biederman, D.J. Yeager, N.Narevsky, J.Leverett, R.Neely, J.M. Carmena,  E.Alon, and J.M. Rabaey, ''A 4.78 mm 2 fully-integrated neuromodulation soc  combining 64 acquisition channels with digital compression and simultaneous  dual stimulation,'' IEEE Journal of Solid-State Circuits, vol.50,  no.4, pp. 1038--1047, April 2015. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2384736
[^85]: A.Mendez, A.Belghith, and M.Sawan, ''A dsp for sensing the bladder volume  through afferent neural pathways,'' IEEE Transactions on Biomedical  Circuits and Systems, vol.8, no.4, pp. 552--564, Aug 2014. [Online]:  http://dx.doi.org/10.1109/TBCAS.2013.2282087
[^86]: T.T. Liu and J.M. Rabaey, ''A 0.25 v 460 nw asynchronous neural signal  processor with inherent leakage suppression,'' IEEE Journal of  Solid-State Circuits, vol.48, no.4, pp. 897--906, April 2013. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2239096
[^87]: D.Han, Y.Zheng, R.Rajkumar, G.S. Dawe, and M.Je, ''A 0.45 v 100-channel  neural-recording ic with sub-$\mu$w/channel consumption in 0.18$ \mu$m  cmos,'' IEEE Transactions on Biomedical Circuits and Systems,  vol.7, no.6, pp. 735--746, Dec 2013. [Online]:  http://dx.doi.org/10.1109/TBCAS.2014.2298860
[^88]: R.Muller, H.P. Le, W.Li, P.Ledochowitsch, S.Gambini, T.Bjorninen,  A.Koralek, J.M. Carmena, M.M. Maharbiz, E.Alon, and J.M. Rabaey, ''A  minimally invasive 64-channel wireless $\mu$ecog implant,'' IEEE  Journal of Solid-State Circuits, vol.50, no.1, pp. 344--359, Jan 2015.  [Online]: http://dx.doi.org/10.1109/JSSC.2014.2364824
[^89]: B.Vigraham, J.Kuppambatti, and P.R. Kinget, ''Switched-mode operational  amplifiers and their application to continuous-time filters in nanoscale  cmos,'' IEEE Journal of Solid-State Circuits, vol.49, no.12, pp.  2758--2772, December 2014. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2354641
[^90]: V.Karkare, H.Chandrakumar, D.Rozgić, and D.Marković, ''Robust,  reconfigurable, and power-efficient biosignal recording systems,'' in  IEEE Proceedings of the Custom Integrated Circuits Conference, Sept  2014, pp. 1--8. [Online]: http://dx.doi.org/10.1109/CICC.2014.6946018
[^91]: L.B. Leene and T.G. Constandinou, ''A 0.45v continuous time-domain filter  using asynchronous oscillator structures,'' in IEEE Proceedings of  the International Conference on Electronics, Circuits and Systems, December  2016.
[^92]: R.Mohan, L.Yan, G.Gielen, C.V. Hoof, and R.F. Yazicioglu, ''0.35 v  time-domain-based instrumentation amplifier,'' Electronics Letters,  vol.50, no.21, pp. 1513--1514, October 2014. [Online]:  http://dx.doi.org/10.1049/el.2014.2471
[^93]: X.Zhang, Z.Zhang, Y.Li, C.Liu, Y.X. Guo, and Y.Lian, ''A 2.89$ \mu$w  dry-electrode enabled clockless wireless ecg soc for wearable applications,''  IEEE Journal of Solid-State Circuits, vol.51, no.10, pp.  2287--2298, Oct 2016. [Online]:  http://dx.doi.org/10.1109/JSSC.2016.2582863
[^94]: M.Elia, L.B. Leene, and T.G. Constandinou, ''Continuous-time micropower  interface for neural recording applications,'' in IEEE Proceedings of  the International Symposium on Circuits and Systems, May 2016, pp. 534--537.  [Online]: http://dx.doi.org/10.1109/ISCAS.2016.7527295
[^95]: N.Guo, Y.Huang, T.Mai, S.Patil, C.Cao, M.Seok, S.Sethumadhavan, and  Y.Tsividis, ''Energy-efficient hybrid analog/digital approximate computation  in continuous time,'' IEEE Journal of Solid-State Circuits, vol.51,  no.7, pp. 1514--1524, July 2016. [Online]:  http://dx.doi.org/10.1109/JSSC.2016.2543729
[^96]: B.Bozorgzadeh, D.R. Schuweiler, M.J. Bobak, P.A. Garris, and P.Mohseni,  ''Neurochemostat: A neural interface soc with integrated chemometrics for  closed-loop regulation of brain dopamine,'' IEEE Transactions on  Biomedical Circuits and Systems, vol.10, no.3, pp. 654--667, June 2016.  [Online]: http://dx.doi.org/10.1109/TBCAS.2015.2453791
[^97]: E.B. Myers and M.L. Roukes, ''Comparative advantages of mechanical  biosensors,'' Nature nanotechnology, vol.6, no.4, pp. 1748--3387,  April 2011. [Online]: http://dx.doi.org/10.1038/nnano.2011.44
[^98]: R.Machado, N.Soltani, S.Dufour, M.T. Salam, P.L. Carlen, R.Genov, and  M.Thompson, ''Biofouling-resistant impedimetric sensor for array  high-resolution extracellular potassium monitoring in the brain,''  Biosensors, vol.6, no.4, p.53, October 2016. [Online]:  http://dx.doi.org/10.3390/bios6040053
[^99]: J.Guo, W.Ng, J.Yuan, S.Li, and M.Chan, ''A 200-channel  area-power-efficient chemical and electrical dual-mode acquisition ic for the  study of neurodegenerative diseases,'' IEEE Transactions on  Biomedical Circuits and Systems, vol.10, no.3, pp. 567--578, June 2016.  [Online]: http://dx.doi.org/10.1109/TBCAS.2015.2468052
[^100]: D.A. Dombeck, A.N. Khabbaz, F.Collman, T.L. Adelman, and D.W. Tank,  ''Imaging large-scale neural activity with cellular resolution in awake,  mobile mice.'' Neuron, vol.56, no.1, pp. 43--57, October 2007.  [Online]: http://dx.doi.org/10.1016/j.neuron.2007.08.003
[^101]: T.York, S.B. Powell, S.Gao, L.Kahan, T.Charanya, D.Saha, N.W. Roberts,  T.W. Cronin, J.Marshall, S.Achilefu, S.P. Lake, B.Raman, and V.Gruev,  ''Bioinspired polarization imaging sensors: From circuits and optics to  signal processing algorithms and biomedical applications,'' Proceedings  of the IEEE, vol. 102, no.10, pp. 1450--1469, Oct 2014. [Online]:  http://dx.doi.org/10.1109/JPROC.2014.2342537
[^102]: K.Paralikar, P.Cong, O.Yizhar, L.E. Fenno, W.Santa, C.Nielsen,  D.Dinsmoor, B.Hocken, G.O. Munns, J.Giftakis, K.Deisseroth, and  T.Denison, ''An implantable optical stimulation delivery system for  actuating an excitable biosubstrate,'' IEEE Journal of Solid-State  Circuits, vol.46, no.1, pp. 321--332, Jan 2011. [Online]:  http://dx.doi.org/10.1109/JSSC.2010.2074110
[^103]: N.Ji and S.L. Smith, ''Technologies for imaging neural activity in large  volumes,'' Nature Neuroscience, vol.19, pp. 1154--1164, September  2016. [Online]: http://dx.doi.org/10.1038/nn.4358
[^104]: S.Song, K.D. Miller, and L.F. Abbott, ''Competitive hebbian learning through  spike-timing-dependent synaptic plasticity,'' Nature Neuroscience,  vol.3, pp. 919--926, September 2000. [Online]:  http://dx.doi.org/10.1038/78829
[^105]: T.Kurafuji, M.Haraguchi, M.Nakajima, T.Nishijima, T.Tanizaki, H.Yamasaki,  T.Sugimura, Y.Imai, M.Ishizaki, T.Kumaki, K.Murata, K.Yoshida,  E.Shimomura, H.Noda, Y.Okuno, S.Kamijo, T.Koide, H.J. Mattausch, and  K.Arimoto, ''A scalable massively parallel processor for real-time image  processing,'' IEEE Journal of Solid-State Circuits, vol.46, no.10,  pp. 2363--2373, October 2011. [Online]:  http://dx.doi.org/10.1109/JSSC.2011.2159528
[^106]: J.Y. Kim, M.Kim, S.Lee, J.Oh, K.Kim, and H.J. Yoo, ''A 201.4 gops 496 mw  real-time multi-object recognition processor with bio-inspired neural  perception engine,'' IEEE Journal of Solid-State Circuits, vol.45,  no.1, pp. 32--45, Jan 2010. [Online]:  http://dx.doi.org/10.1109/JSSC.2009.2031768
[^107]: C.C. Cheng, C.H. Lin, C.T. Li, and L.G. Chen, ''ivisual: An intelligent  visual sensor soc with 2790 fps cmos image sensor and 205 gops/w vision  processor,'' IEEE Journal of Solid-State Circuits, vol.44, no.1,  pp. 127--135, Jan 2009. [Online]:  http://dx.doi.org/10.1109/JSSC.2008.2007158
[^108]: H.Noda, M.Nakajima, K.Dosaka, K.Nakata, M.Higashida, O.Yamamoto,  K.Mizumoto, T.Tanizaki, T.Gyohten, Y.Okuno, H.Kondo, Y.Shimazu,  K.Arimoto, K.Saito, and T.Shimizu, ''The design and implementation of the  massively parallel processor based on the matrix architecture,'' IEEE  Journal of Solid-State Circuits, vol.42, no.1, pp. 183--192, Jan 2007.  [Online]: http://dx.doi.org/10.1109/JSSC.2006.886545
[^109]: M.S. Chae, W.Liu, and M.Sivaprakasam, ''Design optimization for integrated  neural recording systems,'' IEEE Journal of Solid-State Circuits,  vol.43, no.9, pp. 1931--1939, September 2008. [Online]:  http://dx.doi.org/10.1109/JSSC.2008.2001877
[^110]: K.J. Miller, L.B. Sorensen, J.G. Ojemann, and M.den Nijs, ''Power-law  scaling in the brain surface electric potential,'' PLoS Comput Biol,  vol.5, no.12, pp. 1--10, 12 2009. [Online]:  http://dx.doi.org/10.1371%2Fjournal.pcbi.1000609
[^111]: R.Harrison and C.Charles, ''A low-power low-noise cmos amplifier for neural  recording applications,'' IEEE Journal of Solid-State Circuits,  vol.38, no.6, pp. 958--965, June 2003. [Online]:  http://dx.doi.org/10.1109/JSSC.2003.811979
[^112]: W.Sansen, ''1.3 analog cmos from 5 micrometer to 5 nanometer,'' in  IEEE Proceedings of the International Solid-State Circuits  Conference.\hskip 1em plus 0.5em minus 0.4emelax IEEE, February 2015, pp.  1--6. [Online]: http://dx.doi.org/10.1109/ISSCC.2015.7062848
[^113]: M.S.J. Steyaert and W.M.C. Sansen, ''A micropower low-noise monolithic  instrumentation amplifier for medical purposes,'' IEEE Journal of  Solid-State Circuits, vol.22, no.6, pp. 1163--1168, December 1987.  [Online]: http://dx.doi.org/10.1109/JSSC.1987.1052869
[^114]: W.Wattanapanitch, M.Fee, and R.Sarpeshkar, ''An energy-efficient micropower  neural recording amplifier,'' IEEE Transactions on Biomedical  Circuits and Systems, vol.1, no.2, pp. 136--147, June 2007. [Online]:  http://dx.doi.org/10.1109/TBCAS.2007.907868
[^115]: B.Johnson and A.Molnar, ''An orthogonal current-reuse amplifier for  multi-channel sensing,'' IEEE Journal of Solid-State Circuits,  vol.48, no.6, pp. 1487--1496, June 2013. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2257478
[^116]: C.Qian, J.Parramon, and E.Sanchez-Sinencio, ''A micropower low-noise neural  recording front-end circuit for epileptic seizure detection,'' IEEE  Journal of Solid-State Circuits, vol.46, no.6, pp. 1392--1405, June 2011.  [Online]: http://dx.doi.org/10.1109/JSSC.2011.2126370
[^117]: X.Zou, L.Liu, J.H. Cheong, L.Yao, P.Li, M.-Y. Cheng, W.L. Goh,  R.Rajkumar, G.Dawe, K.-W. Cheng, and M.Je, ''A 100-channel 1-mw  implantable neural recording ic,'' IEEE Transactions on Circuits and  Systems---Part I: Regular Papers, vol.60, no.10, pp. 2584--2596, October  2013. [Online]: http://dx.doi.org/10.1109/TCSI.2013.2249175
[^118]: V.Majidzadeh, A.Schmid, and Y.Leblebici, ''Energy efficient low-noise neural  recording amplifier with enhanced noise efficiency factor,'' IEEE  Transactions on Biomedical Circuits and Systems, vol.5, no.3, pp.  262--271, June 2011. [Online]:  http://dx.doi.org/10.1109/TBCAS.2010.2078815
[^119]: ibitemQ-basedC.C. Enz and E.A. Vittoz, Charge-based MOS transistor modeling: the EKV  model for low-power AND RF IC design.\hskip 1em plus 0.5em minus 0.4emelax  John Wiley & Sons, August 2006. [Online]:  http://eu.wiley.com/WileyCDA/WileyTitle/productCd-0470855452.html
[^120]: Y.Yasuda, T.-J.K. Liu, and C.Hu, ''Flicker-noise impact on scaling of  mixed-signal cmos with hfsion,'' IEEE Transactions on Electron  Devices, vol.55, no.1, pp. 417--422, January 2008. [Online]:  http://dx.doi.org/10.1109/TED.2007.910759
[^121]: S.-Y. Wu, C.Lin, M.Chiang, J.Liaw, J.Cheng, S.Yang, M.Liang,  T.Miyashita, C.Tsai, B.Hsu, H.Chen, T.Yamamoto, S.Chang, V.Chang,  C.Chang, J.Chen, H.Chen, K.Ting, Y.Wu, K.Pan, R.Tsui, C.Yao,  P.Chang, H.Lien, T.Lee, H.Lee, W.Chang, T.Chang, R.Chen, M.Yeh,  C.Chen, Y.Chiu, Y.Chen, H.Huang, Y.Lu, C.Chang, M.Tsai, C.Liu,  K.Chen, C.Kuo, H.Lin, S.Jang, and Y.Ku, ''A 16nm finfet cmos technology  for mobile soc and computing applications,'' in IEEE Proceedings of  the International Electron Devices Meeting, December 2013, pp. 9.1.1--9.1.4.  [Online]: http://dx.doi.org/10.1109/IEDM.2013.6724591
[^122]: L.B. Leene, Y.Liu, and T.G. Constandinou, ''A compact recording array for  neural interfaces,'' in IEEE Proceedings of the Biomedical Circuits  and Systems Conference, October 2013, pp. 97--100. [Online]:  http://dx.doi.org/10.1109/BioCAS.2013.6679648
[^123]: Q.Fan, F.Sebastiano, J.Huijsing, and K.Makinwa, ''A $1.8 \mu  w\:60 nv/√Hz$ capacitively-coupled chopper instrumentation amplifier  in 65 nm cmos for wireless sensor nodes,'' IEEE Journal of  Solid-State Circuits, vol.46, no.7, pp. 1534--1543, July 2011. [Online]:  http://dx.doi.org/10.1109/JSSC.2011.2143610
[^124]: H.Chandrakumar and D.Markovic, ''A simple area-efficient ripple-rejection  technique for chopped biosignal amplifiers,'' IEEE Transactions on  Circuits and Systems---Part II: Express Briefs, vol.62, no.2, pp.  189--193, February 2015. [Online]:  http://dx.doi.org/10.1109/TCSII.2014.2387686
[^125]: H.Chandrakumar and D.Markovic, ''A 2$\mu$w 40mvpp linear-input-range  chopper-stabilized bio-signal amplifier with boosted input impedance of  300mohm and electrode-offset filtering,'' in IEEE Proceedings of the  International Solid-State Circuits Conference.\hskip 1em plus 0.5em minus  0.4emelax IEEE, January 2016, pp. 96--97. [Online]:  http://dx.doi.org/10.1109/ISSCC.2016.7417924
[^126]: H.Rezaee-Dehsorkh, N.Ravanshad, R.Lotfi, K.Mafinezhad, and A.M. Sodagar,  ''Analysis and design of tunable amplifiers for implantable neural recording  applications,'' IEEE Transactions on Emerging and Selected Topics in  Circuits and Systems, vol.1, no.4, pp. 546--556, December 2011. [Online]:  http://dx.doi.org/10.1109/JETCAS.2011.2174492
[^127]: X.Zou, X.Xu, L.Yao, and Y.Lian, ''A 1-v 450-nw fully integrated  programmable biomedical sensor interface chip,'' IEEE Journal of  Solid-State Circuits, vol.44, no.4, pp. 1067--1077, April 2009. [Online]:  http://dx.doi.org/10.1109/JSSC.2009.2014707
[^128]: L.Leene and T.Constandinou, ''Ultra-low power design strategy for two-stage  amplifier topologies,'' Electronics Letters, vol.50, no.8, pp.  583--585, April 2014. [Online]: http://dx.doi.org/10.1049/el.2013.4196
[^129]: H.G. Rey, C.Pedreira, and R.Q. Quiroga, ''Past, present and future of spike  sorting techniques,'' Brain Research Bulletin, vol. 119, Part B, pp.  106--117, October 2015, advances in electrophysiological data analysis.  [Online]:  http://www.sciencedirect.com/science/article/pii/S0361923015000684
[^130]: Y.Chen, A.Basu, L.Liu, X.Zou, R.Rajkumar, G.S. Dawe, and M.Je, ''A  digitally assisted, signal folding neural recording amplifier,'' IEEE  Transactions on Biomedical Circuits and Systems, vol.8, no.4, pp.  528--542, August 2014. [Online]:  http://dx.doi.org/10.1109/TBCAS.2013.2288680
[^131]: X.Yue, ''Determining the reliable minimum unit capacitance for the dac  capacitor array of sar adcs,'' Microelectronics Journal, vol.44,  no.6, pp. 473 -- 478, 2013. [Online]:  http://www.sciencedirect.com/science/article/pii/S0026269213000815
[^132]: Y.Zhu, C.-H. Chan, U.-F. Chio, S.-W. Sin, S.-P. U, R.Martins, and  F.Maloberti, ''Split-sar adcs: Improved linearity with power and speed  optimization,'' IEEE Transactions on Very Large Scale Integration  (VLSI) Systems, vol.22, no.2, pp. 372--383, February 2014. [Online]:  http://dx.doi.org/10.1109/TVLSI.2013.2242501
[^133]: L.Xie, G.Wen, J.Liu, and Y.Wang, ''Energy-efficient hybrid capacitor  switching scheme for sar adc,'' Electronics Letters, vol.50, no.1,  pp. 22--23, January 2014. [Online]:  http://dx.doi.org/10.1049/el.2013.2794
[^134]: P.Nuzzo, F.DeBernardinis, P.Terreni, and G.Vander Plas, ''Noise analysis  of regenerative comparators for reconfigurable adc architectures,''  IEEE Transactions on Circuits and Systems---Part I: Regular  Papers, vol.55, no.6, pp. 1441--1454, July 2008. [Online]:  http://dx.doi.org/10.1109/TCSI.2008.917991
[^135]: G.Heinzel, A.R\"udiger, and R.Schilling, ''Spectrum and spectral density  estimation by the discrete fourier transform (dft), including a comprehensive  list of window functions and some new at-top windows,'' pp. 25--27, February  2002. [Online]: http://hdl.handle.net/11858/00-001M-0000-0013-557A-5
[^136]: F.Gerfers, M.Ortmanns, and Y.Manoli, ''A 1.5-v 12-bit power-efficient  continuous-time third-order sigma; delta; modulator,'' IEEE Journal  of Solid-State Circuits, vol.38, no.8, pp. 1343--1352, Aug 2003. [Online]:  http://dx.doi.org/10.1109/JSSC.2003.814432
[^137]: Y.Chae, K.Souri, and K.A.A. Makinwa, ''A 6.3$ \mu$w 20$ $bit incremental  zoom-adc with 6 ppm inl and 1 $\mu$v offset,'' IEEE Journal of  Solid-State Circuits, vol.48, no.12, pp. 3019--3027, Dec 2013. [Online]:  http://dx.doi.org/10.1109/JSSC.2013.2278737
[^138]: Y.S. Shu, L.T. Kuo, and T.Y. Lo, ''An oversampling sar adc with dac mismatch  error shaping achieving 105db sfdr and 101db sndr over 1khz bw in 55nm  cmos,'' in IEEE Proceedings of the International Solid-State Circuits  Conference, January 2016, pp. 458--459. [Online]:  http://dx.doi.org/10.1109/ISSCC.2016.7418105
[^139]: P.Harpe, E.Cantatore, and A.van Roermund, ''An oversampled 12/14b sar adc  with noise reduction and linearity enhancements achieving up to 79.1db  sndr,'' in IEEE Proceedings of the International Solid-State Circuits  Conference, February 2014, pp. 194--195. [Online]:  http://dx.doi.org/10.1109/ISSCC.2014.6757396
[^140]: ibitemchrch-turingM.Braverman, J.Schneider, and C.Rojas, ''Space-bounded church-turing thesis  and computational tractability of closed systems,'' Physical Review  Letters, vol. 115, August 2015. [Online]:  http://link.aps.org/doi/10.1103/PhysRevLett.115.098701
[^141]: M.Verhelst and A.Bahai, ''Where analog meets digital: Analog-to-information  conversion and beyond,'' IEEE Solid-State Circuits Magazine, vol.7,  no.3, pp. 67--80, September 2015. [Online]:  http://dx.doi.org/10.1109/MSSC.2015.2442394
[^142]: H.A. Marblestone, M.B. Zamft, G.Y. Maguire, G.M. Shapiro, R.T. Cybulski,  I.J. Glaser, D.Amodei, P.B. Stranges, R.Kalhor, A.D. Dalrymple, D.Seo,  E.Alon, M.M. Maharbiz, M.J. Carmena, M.J. Rabaey, S.E. Boyden, M.G.  Church, and P.K. Kording, ''Physical principles for scalable neural  recording,'' Frontiers in Computational Neuroscience, vol.7, no. 137,  2013. [Online]:  http://www.frontiersin.org/computational_neuroscience/10.3389/fncom.2013.00137
[^143]: L.Traver, C.Tarin, P.Marti, and N.Cardona, ''Adaptive-threshold neural  spike by noise-envelope tracking,'' Electronics Letters, vol.43,  no.24, pp. 1333--1335, November 2007. [Online]:  http://dx.doi.org/10.1049/el:20071631
[^144]: I.Obeid and P.Wolf, ''Evaluation of spike-detection algorithms fora  brain-machine interface application,'' IEEE Transactions on  Biomedical Engineering, vol.51, no.6, pp. 905--911, June 2004. [Online]:  http://dx.doi.org/10.1109/TBME.2004.826683
[^145]: P.Watkins, G.Santhanam, K.Shenoy, and R.Harrison, ''Validation of adaptive  threshold spike detector for neural recording,'' in IEEE Proceedings  of the International Conference on Engineering in Medicine and Biology  Society, vol.2, September 2004, pp. 4079--4082. [Online]:  http://dx.doi.org/10.1109/IEMBS.2004.1404138
[^146]: T.Takekawa, Y.Isomura, and T.Fukai, ''Accurate spike sorting for multi-unit  recordings,'' European Journal of Neuroscience, vol.31, no.2, pp.  263--272, 2010. [Online]:  http://dx.doi.org/10.1111/j.1460-9568.2009.07068.x
[^147]: A.Zviagintsev, Y.Perelman, and R.Ginosar, ''Low-power architectures for  spike sorting,'' in IEEE Proceedings of the International Conference  on Neural Engineering, March 2005, pp. 162--165. [Online]:  http://dx.doi.org/10.1109/CNE.2005.1419579
[^148]: A.Rodriguez-Perez, J.Ruiz-Amaya, M.Delgado-Restituto, and  A.Rodriguez-Vazquez, ''A low-power programmable neural spike detection  channel with embedded calibration and data compression,'' IEEE  Transactions on Biomedical Circuits and Systems, vol.6, no.2, pp. 87--100,  April 2012. [Online]: http://dx.doi.org/10.1109/TBCAS.2012.2187352
[^149]: U.Rutishauser, E.M. Schuman, and A.N. Mamelak, ''Online detection and  sorting of extracellularly recorded action potentials in human medial  temporal lobe recordings, in vivo,'' Journal of Neuroscience Methods,  vol. 154, no. 1–2, pp. 204 -- 224, 2006. [Online]:  http://www.sciencedirect.com/science/article/pii/S0165027006000033
[^150]: F.Franke, M.Natora, C.Boucsein, M.Munk, and K.Obermayer,  ''\BIBforeignlanguageEnglishAn online spike detection and spike  classification algorithm capable of instantaneous resolution of overlapping  spikes,'' \BIBforeignlanguageEnglishJournal of Computational  Neuroscience, vol.29, no. 1-2, pp. 127--148, 2010. [Online]:  http://dx.doi.org/10.1007/s10827-009-0163-5
[^151]: M.S. Chae, Z.Yang, M.Yuce, L.Hoang, and W.Liu, ''A 128-channel 6 mw  wireless neural recording ic with spike feature extraction and uwb  transmitter,'' IEEE Transactions on Neural Systems and Rehabilitation  Engineering, vol.17, no.4, pp. 312--321, August 2009. [Online]:  http://dx.doi.org/10.1109/TNSRE.2009.2021607
[^152]: P.H. Thakur, H.Lu, S.S. Hsiao, and K.O. Johnson, ''Automated optimal  detection and classification of neural action potentials in extra-cellular  recordings,'' Journal of Neuroscience Methods, vol. 162, no. 1–2,  pp. 364 -- 376, 2007. [Online]:  ttp://www.sciencedirect.com/science/article/pii/S0165027007000477
[^153]: J.Zhang, Y.Suo, S.Mitra, S.Chin, S.Hsiao, R.Yazicioglu, T.Tran, and  R.Etienne-Cummings, ''An efficient and compact compressed sensing  microsystem for implantable neural recordings,'' IEEE Transactions on  Biomedical Circuits and Systems, vol.8, no.4, pp. 485--496, August 2014.  [Online]: http://dx.doi.org/10.1109/TBCAS.2013.2284254
[^154]: Y.Suo, J.Zhang, T.Xiong, P.S. Chin, R.Etienne-Cummings, and T.D. Tran,  ''Energy-efficient multi-mode compressed sensing system for implantable  neural recordings,'' IEEE Transactions on Biomedical Circuits and  Systems, vol.8, no.5, pp. 648--659, October 2014. [Online]:  http://dx.doi.org/10.1109/TBCAS.2014.2359180
[^155]: B.Yu, T.Mak, X.Li, F.Xia, A.Yakovlev, Y.Sun, and C.S. Poon, ''Real-time  fpga-based multichannel spike sorting using hebbian eigenfilters,''  IEEE Transactions on Emerging and Selected Topics in Circuits and  Systems, vol.1, no.4, pp. 502--515, December 2011. [Online]:  http://dx.doi.org/10.1109/JETCAS.2012.2183430
[^156]: V.Ventura, ''Automatic spike sorting using tuning information,'' Neural  computation, vol.21, no.9, pp. 2466--2501, September 2009. [Online]:  http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4167425/
[^157]: D.Y. Barsakcioglu, A.Eftekhar, and T.G. Constandinou, ''Design optimisation  of front-end neural interfaces for spike sorting systems,'' in IEEE  Proceedings of the International Symposium on Circuits and Systems, May  2013, pp. 2501--2504. [Online]:  http://dx.doi.org/10.1109/ISCAS.2013.6572387
[^158]: A.M. Sodagar, K.D. Wise, and K.Najafi, ''A fully integrated mixed-signal  neural processor for implantable multichannel cortical recording,''  IEEE Transactions on Biomedical Engineering, vol.54, no.6, pp.  1075--1088, June 2007. [Online]:  http://dx.doi.org/10.1109/TBME.2007.894986
[^159]: Y.Xin, W.X. Li, R.C. Cheung, R.H. Chan, H.Yan, D.Song, and T.W. Berger,  ''An fpga based scalable architecture of a stochastic state point process  filter (ssppf) to track the nonlinear dynamics underlying neural spiking,''  Microelectronics Journal, vol.45, no.6, pp. 690 -- 701, June 2014.  [Online]:  http://www.sciencedirect.com/science/article/pii/S0026269214000913
[^160]: C.Qian, J.Shi, J.Parramon, and E.Sánchez-Sinencio, ''A low-power  configurable neural recording system for epileptic seizure detection,''  IEEE Transactions on Biomedical Circuits and Systems, vol.7, no.4,  pp. 499--512, August 2013. [Online]:  http://dx.doi.org/10.1109/TBCAS.2012.2228857
[^161]: K.C. Chun, P.Jain, J.H. Lee, and C.H. Kim, ''A 3t gain cell embedded dram  utilizing preferential boosting for high density and low power on-die  caches,'' IEEE Journal of Solid-State Circuits, vol.46, no.6, pp.  1495--1505, June 2011. [Online]:  http://dx.doi.org/10.1109/JSSC.2011.2128150
[^162]: R.E. Matick and S.E. Schuster, ''Logic-based edram: Origins and rationale for  use,'' IBM Journal of Research AND Development, vol.49, no.1, pp.  145--165, January 2005. [Online]: http://dx.doi.org/10.1147/rd.491.0145
[^163]: R.Nair, ''Evolution of memory architecture,'' Proceedings of the  IEEE, vol. 103, no.8, pp. 1331--1345, August 2015. [Online]:  http://dx.doi.org/10.1109/JPROC.2015.2435018
[^164]: C.E. Molnar and I.W. Jones, ''Simple circuits that work for complicated  reasons,'' in IEEE Proceedings of the International Symposium on  Advanced Research in Asynchronous Circuits and Systems, 2000, pp. 138--149.  [Online]: http://dx.doi.org/10.1109/ASYNC.2000.836995
[^165]: ibitemBN-formH.Schorr, ''Computer-aided digital system design and analysis using a register  transfer language,'' IEEE Transactions on Electronic Computers, vol.  EC-13, no.6, pp. 730--737, December 1964. [Online]:  http://dx.doi.org/10.1109/PGEC.1964.263907
[^166]: D.Wang, A.Rajendiran, S.Ananthanarayanan, H.Patel, M.Tripunitara, and  S.Garg, ''Reliable computing with ultra-reduced instruction set  coprocessors,'' IEEE Micro, vol.34, no.6, pp. 86--94, November  2014. [Online]: http://dx.doi.org/10.1109/MM.2013.130
[^167]: ''Msp430g2x53 mixed signal microcontroller - data sheet,'' Texas Instruments  Incorporated, Dallas, Texas, pp. 403--413, May 2013. [Online]:  http://www.ti.com/lit/ds/symlink/msp430g2553.pdf
[^168]: F.L. Yuan, C.C. Wang, T.H. Yu, and D.Marković, ''A multi-granularity fpga  with hierarchical interconnects for efficient and flexible mobile  computing,'' IEEE Journal of Solid-State Circuits, vol.50, no.1,  pp. 137--149, January 2015. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2372034
[^169]: B.Vigraham, J.Kuppambatti, and P.R. Kinget, ''Switched-mode operational  amplifiers and their application to continuous-time filters in nanoscale  cmos,'' IEEE Journal of Solid-State Circuits, vol.49, no.12, pp.  2758--2772, December 2014. [Online]:  http://dx.doi.org/10.1109/JSSC.2014.2354641
[^170]: Y.Tsividis, ''Event-driven data acquisition and continuous-time digital signal  processing,'' in IEEE Proceedings of the Custom Integrated Circuits  Conference, September 2010, pp. 1--8. [Online]:  http://dx.doi.org/10.1109/CICC.2010.5617618
[^171]: I.Lee, D.Sylvester, and D.Blaauw, ''A constant energy-per-cycle ring  oscillator over a wide frequency range for wireless sensor nodes,''  IEEE Journal of Solid-State Circuits, vol.51, no.3, pp. 697--711,  March 2016. [Online]: http://dx.doi.org/10.1109/JSSC.2016.2517133
[^172]: B.Drost, M.Talegaonkar, and P.K. Hanumolu, ''Analog filter design using ring  oscillator integrators,'' IEEE Journal of Solid-State Circuits,  vol.47, no.12, pp. 3120--3129, December 2012. [Online]:  http://dx.doi.org/10.1109/JSSC.2012.2225738
[^173]: V.Unnikrishnan and M.Vesterbacka, ''Time-mode analog-to-digital conversion  using standard cells,'' IEEE Transactions on Circuits and  Systems---Part I: Fundamental Theory and Applications, vol.61, no.12,  pp. 3348--3357, December 2014. [Online]:  http://dx.doi.org/10.1109/TCSI.2014.2340551
[^174]: K.Yang, D.Blaauw, and D.Sylvester, ''An all-digital edge racing true random  number generator robust against pvt variations,'' IEEE Journal of  Solid-State Circuits, vol.51, no.4, pp. 1022--1031, April 2016. [Online]:  http://dx.doi.org/10.1109/JSSC.2016.2519383
[^175]: ibitem0.5V-CircuitS.Chatterjee, Y.Tsividis, and P.Kinget, ''0.5-v analog circuit techniques  and their application in ota and filter design,'' IEEE Journal of  Solid-State Circuits, vol.40, no.12, pp. 2373--2387, December 2005.  [Online]: http://dx.doi.org/10.1109/JSSC.2005.856280
[^176]: M.Alioto, ''Understanding dc behavior of subthreshold cmos logic through  closed-form analysis,'' IEEE Transactions on Circuits and  Systems---Part I: Fundamental Theory and Applications, vol.57, no.7, pp.  1597--1607, July 2010. [Online]:  http://dx.doi.org/10.1109/TCSI.2009.2034233
[^177]: A.Hajimiri and T.Lee, ''A general theory of phase noise in electrical  oscillators,'' IEEE Journal of Solid-State Circuits, vol.33, no.2,  pp. 179--194, February 1998. [Online]:  http://dx.doi.org/10.1109/4.658619
[^178]: A.Demir, A.Mehrotra, and J.Roychowdhury, ''Phase noise in oscillators: a  unifying theory and numerical methods for characterization,'' IEEE  Transactions on Circuits and Systems---Part I: Fundamental Theory and  Applications, vol.47, no.5, pp. 655--674, May 2000. [Online]:  http://dx.doi.org/10.1109/81.847872
[^179]: A.Hajimiri, S.Limotyrakis, and T.Lee, ''Phase noise in multi-gigahertz cmos  ring oscillators,'' in IEEE Proceedings of the Custom Integrated  Circuits Conference, May 1998, pp. 49--52. [Online]:  http://dx.doi.org/10.1109/CICC.1998.694905
[^180]: W.Jiang, V.Hokhikyan, H.Chandrakumar, V.Karkare, and D.Markovic, ''A  ±50mv linear-input-range vco-based neural-recording front-end with  digital nonlinearity correction,'' in IEEE Proceedings of the  International Solid-State Circuits Conference, January 2016, pp. 484--485.  [Online]: http://dx.doi.org/10.1109/ISSCC.2016.7418118
[^181]: C.Weltin-Wu and Y.Tsividis, ''An event-driven clockless level-crossing adc  with signal-dependent adaptive resolution,'' IEEE Journal of  Solid-State Circuits, vol.48, no.9, pp. 2180--2190, September 2013.  [Online]: http://dx.doi.org/10.1109/JSSC.2013.2262738
[^182]: H.Y. Yang and R.Sarpeshkar, ''A bio-inspired ultra-energy-efficient  analog-to-digital converter for biomedical applications,'' IEEE  Transactions on Circuits and Systems---Part I: Fundamental Theory and  Applications, vol.53, no.11, pp. 2349--2356, November 2006. [Online]:  http://dx.doi.org/10.1109/TCSI.2006.884463
[^183]: F.Corradi and G.Indiveri, ''A neuromorphic event-based neural recording  system for smart brain-machine-interfaces,'' IEEE Transactions on  Biomedical Circuits and Systems, vol.9, no.5, pp. 699--709, October 2015.  [Online]: http://dx.doi.org/10.1109/TBCAS.2015.2479256
[^184]: K.A. Ng and Y.P. Xu, ''A compact, low input capacitance neural recording  amplifier,'' IEEE Transactions on Biomedical Circuits and Systems,  vol.7, no.5, pp. 610--620, October 2013. [Online]:  http://dx.doi.org/10.1109/TBCAS.2013.2280066
[^185]: J.Agustin and M.Lopez-Vallejo, ''An in-depth analysis of ring oscillators:  Exploiting their configurable duty-cycle,'' IEEE Transactions on  Circuits and Systems---Part I: Fundamental Theory and Applications,  vol.62, no.10, pp. 2485--2494, October 2015. [Online]:  http://dx.doi.org/10.1109/TCSI.2015.2476300
[^186]: K.Ng and Y.P. Xu, ''A compact, low input capacitance neural recording  amplifier,'' IEEE Transactions on Biomedical Circuits and Systems,  vol.7, no.5, pp. 610--620, October 2013. [Online]:  http://dx.doi.org/10.1109/TBCAS.2013.2280066
[^187]: M.Elia, L.B. Leene, and T.G. Constandinou, ''Continuous-time micropower  interface for neural recording applications,'' in IEEE Proceedings of  the International Symposium on Circuits and Systems, May 2016.
[^188]: Y.W. Li, K.L. Shepard, and Y.P. Tsividis, ''A continuous-time programmable  digital fir filter,'' IEEE Journal of Solid-State Circuits, vol.41,  no.11, pp. 2512--2520, November 2006. [Online]:  http://dx.doi.org/10.1109/JSSC.2006.883314
[^189]: B.Schell and Y.Tsividis, ''A continuous-time adc/dsp/dac system with no clock  and with activity-dependent power dissipation,'' IEEE Journal of  Solid-State Circuits, vol.43, no.11, pp. 2472--2481, November 2008.  [Online]: http://dx.doi.org/10.1109/JSSC.2008.2005456
[^190]: S.Aouini, K.Chuai, and G.W. Roberts, ''Anti-imaging time-mode filter design  using a pll structure with transfer function dft,'' IEEE Transactions  on Circuits and Systems---Part I: Fundamental Theory and Applications,  vol.59, no.1, pp. 66--79, January 2012. [Online]:  http://dx.doi.org/10.1109/TCSI.2011.2161411
[^191]: X.Xing and G.G.E. Gielen, ''A 42 fj/step-fom two-step vco-based delta-sigma  adc in 40 nm cmos,'' IEEE Journal of Solid-State Circuits, vol.50,  no.3, pp. 714--723, March 2015. [Online]:  http://dx.doi.org/10.1109/JSSC.2015.2393814
[^192]: K.Reddy, S.Rao, R.Inti, B.Young, A.Elshazly, M.Talegaonkar, and P.K.  Hanumolu, ''A 16-mw 78-db sndr 10-mhz bw ct $\delta \sigma$ adc using  residue-cancelling vco-based quantizer,'' IEEE Journal of Solid-State  Circuits, vol.47, no.12, pp. 2916--2927, December 2012. [Online]:  http://dx.doi.org/10.1109/JSSC.2012.2218062
[^193]: J.Daniels, W.Dehaene, M.S.J. Steyaert, and A.Wiesbauer, ''A/d conversion  using asynchronous delta-sigma modulation and time-to-digital conversion,''  IEEE Transactions on Circuits and Systems---Part I: Fundamental  Theory and Applications, vol.57, no.9, pp. 2404--2412, September 2010.  [Online]: http://dx.doi.org/10.1109/TCSI.2010.2043169
[^194]: F.M. Yaul and A.P. Chandrakasan, ''A sub-$\mu$w 36nv/$√Hz$ chopper  amplifier for sensors using a noise-efficient inverter-based 0.2v-supply  input stage,'' in IEEE Proceedings of the International Solid-State  Circuits Conference, January 2016, pp. 94--95. [Online]:  http://dx.doi.org/10.1109/ISSCC.2016.7417923
[^195]: S.Patil, A.Ratiu, D.Morche, and Y.Tsividis, ''A 3-10 fj/conv-step  error-shaping alias-free continuous-time adc,'' IEEE Journal of  Solid-State Circuits, vol.51, no.4, pp. 908--918, April 2016. [Online]:  http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7433385&isnumber=7446371
[^196]: J.M. Duarte-Carvajalino and G.Sapiro, ''Learning to sense sparse signals:  Simultaneous sensing matrix and sparsifying dictionary optimization,''  IEEE Transactions on Image Processing, vol.18, no.7, pp.  1395--1408, July 2009. [Online]:  http://dx.doi.org/10.1109/TIP.2009.2022459
[^197]: R.S. Schneider and H.C. Card, ''Analog hardware implementation issues in  deterministic boltzmann machines,'' IEEE Transactions on Circuits and  Systems---Part II: Analog and Digital Signal Processing, vol.45, no.3,  pp. 352--360, Mar 1998. [Online]: http://dx.doi.org/10.1109/82.664241
[^198]: J.Lu, S.Young, I.Arel, and J.Holleman, ''A 1 tops/w analog deep  machine-learning engine with floating-gate storage in 0.13$\mu$m cmos,''  IEEE Journal of Solid-State Circuits, vol.50, no.1, pp. 270--281,  January 2015. [Online]: http://dx.doi.org/10.1109/JSSC.2014.2356197
[^199]: M.T. Wolf and J.W. Burdick, ''A bayesian clustering method for tracking  neural signals over successive intervals,'' IEEE Transactions on  Biomedical Engineering, vol.56, no.11, pp. 2649--2659, November 2009.  [Online]: http://dx.doi.org/10.1109/TBME.2009.2027604
[^200]: D.Y. Barsakcioglu and T.G. Constandinou, ''A 32-channel mcu-based feature  extraction and classification for scalable on-node spike sorting,'' in  IEEE Proceedings of the International Symposium on Circuits and  Systems, May 2016.
[^201]: R.P. Feynman, ''There's plenty of room at the bottom,'' American  Physical Society, vol.23, no.5, pp. 22--36, February 1960. [Online]:  http://www.zyvex.com/nanotech/feynman.html
[^202]: G.Leuba and L.J. Garey, ''Comparison of neuronal and glial numerical density  in primary and secondary visual cortex of man,'' Experimental Brain  Research, vol.77, no.1, pp. 31--38, 1989. [Online]:  http://dx.doi.org/10.1007/BF00250564
[^203]: I.Guideline, ''Guidelines for limiting exposure to time-varying electric,  magnetic, and electromagnetic fields (up to 300 ghz),'' Health  Physics, vol.74, no.4, pp. 494--522, October 1998. [Online]:  http://www.icnirp.org/cms/upload/publications/ICNIRPemfgdl.pdf
[^204]: L.B. Leene, S.Luan, and T.G. Constandinou, ''A 890fj/bit uwb transmitter for  soc integration in high bit-rate transcutaneous bio-implants,'' in  IEEE Proceedings of the International Symposium on Circuits and  Systems, May 2013, pp. 2271--2274. [Online]:  http://dx.doi.org/10.1109/ISCAS.2013.6572330
[^205]: ''Unconventional processing of signals for intelligent data exploitation  (upside),'' Defense Advanced Research Projects Agency, Arlington, Texas,  January 2016. [Online]:  http://www.darpa.mil/program/unconventional-processing-of-signals-for-intelligent-data-exploitation
