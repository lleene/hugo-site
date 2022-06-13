---
title: "Implantable Biotelemetry"
date: 2012-09-13T15:26:46+01:00
draft: false
toc: true
type: posts
math: true
tags:
  - chapter
  - wireless
  - CMOS
  - biomedical
  - implants
---


Lieuwe B. Leene

B.Eng Electronic Engineering Hong Kong University of Science & Technology, 2011

Supervised by: Dr Timothy G. Constandinou

A Thesis submitted in fulfilment of requirements for the degree of Master of Science Analogue and Digital Integrated Circuit Design of Imperial College London

Department of Electrical and Electronic Engineering Imperial College London

# Abstract

Recent developments in the field of neuroscience and health monitoring have identified the need for biotelemetry systems based around a ultra efficient power standard to allow for next generation biomedical implants and distributed en vivo sensory networks. The work presented here engages the design of the biotelemetry forward and reverse links with a top down perspective exploring the loss mechanics and inefficiencies of concern. This development has led to the the design of an optimized class-E based inductive link that includes a improved modulation scheme specific to the operation of the power amplifier as well as a integrated low complexity BPSK demodulator. In addition a frame work was developed around a scalable UWB delay modulation scheme that improves transmitter efficiency as well as circuit level designs for a widely tunable digital oscillator and a particularly energy efficient UWB pulse generator based off the impulse response of a LC resonator. In extension an UWB antenna is designed with significant improvements in the low-frequency group-delay and reflection co-efficient and a simple energy detection receiver is developed that will allow testing of the full custom digital layout that is designed for fully integrated the UWB transceiver system in $0.18 \mu m$ CMOS technology. The presented forward link achieves achieve a power transmission efficiency of 46% and 34% while transmitting 250kb/s. The UWB transmitter consumed $68.9\mu W$ of power for a PRF of 10MHz that corresponds to a data rate of 77.5 Mb/s.

# Acknowledgment

I would like to sincerely thank Dr Timothy G. Constandinou for supervising this project. His insightful support and valuable opportunities that has enabled me take this project from vague ideas to a taped out chip design. I would also like to thank Song Luan for his continuous feedback and technical expertise that has allowed me to rapidly develop some of the prototyped devices through out this project. In addition I would like to thank Olive Murphy for advice on testing antennas and allowing me to use the CST MICROWAVE STUDIO software to support my project. Finally, I would like to thank my family for their support over the past year and Ching Chen Ma for always providing that inspiring ambition.


# 1 Motivation

It has been slightly over 100 years since the advent of the world’s first ‘transistor’ and even more now than a decade ago, revolution has almost become synonymous with the advancement of the microelectronics industry with impacts that change the very backbone of society. The revolution of the last decade surely belonged to that of mobile devices industry which experienced an increase in user end data demand by over a hundred fold. On the other end of the spectrum however this surge of wireless connectivity of the past decade has synergized and inspired a new foundation of ideas for biomedical systems.

These novel systems are based around digitizing the medical diagnosis and treatment trough wireless en vivo sensory networks for true personalized medicine. By employing electronic implants that have demonstrated incredible potential due to the dense functionality of CMOS technology, the implantable system on chip have shown potential for restoring vision, treating paralysis, severe epilepsy and Parkinson’s disease [^2]. In addition to applications for novel heath monitoring systems and home-stay medication, bio-telemetry links to implanted devices have enabled the simultaneous study of several hundreds of functioning neurons in a localized area through multi electrode arrays (MEAs). These studies have given crucial insight to behavioral models of the brain for fields such as neuroscience. Recent advances have allowed patients with a spinal impairment to interact with the world through a brain machine interface bringing society closer to visions such as J. C. R. Licklider’s Man-Computer Symbiosis.

Although the idea of wireless powering of implanted devices has been around since the early 1960s for long term artificial cardiac pacemakers, the focus of current generation bio-telemetry systems has shifted from a functional orientation to building a framework for reliability and performance directed at commercial applications. As a result of new applications finding their way to employing bio-telemetry links where there are a net set challenges associated with handling the transmission of substantial data rates. The more recent neural recording system-on-chip (SOC) in particular has presented very challenging power requirements for the radio frequency (RF) transmitter driven by the restriction on heat dissapation inorder to prevent cell damage. As the demand for number of simultaneously neurons recorded exponentially increases every year, a significant amount of interest has been directed at finding more efficient alternatives for transmitting data out of the implant wirelessly and exploiting specialized encryption algorithms that reduce data rate requirements such as inter-spike-interval figures & spike-feature extraction [^3].

In similitude to the miniaturization principle of microelectronics, biomedical system miniaturization is also seen as an important merit that improves the comfort of the subject. Consequently the size of radiating elements inherent to the telemetry system is also an important topic for consideration that with recent demonstrations has brought to light the viability of power and data transmission via GHz radiation and may change bio-telemetry to a more specialized RFID tag based medical system in the future.

This thesis presents various system level reductions and efficiency optimizations on both the forward transmission link, from the external system towards the implant, as well as the reverse transmission link, from the implant to the external system. The overall focus revolves around presenting scalable topologies that may allow significant improvements in power consumption of the overhead transmission components which is key in enabling future neural studies and ultra-low power telemetry systems that can be incorporated with RF energy harvesting technologies to give way for next generation biomedical implants based on multi-element sensory networks.

All schematic designs presented in this document are based on a 0.18\\(\mu\\)m CMOS technology using a 1.2V supply. Circuit level simulations were carried out using Cadence IC5.1.41 with foundry provided PSP models. 2D & 3D electromagnetic simulations were carried out using the CST MICROWAVE STUDIO package.

# 2 Report Outline

Chapter 2 is based on introducing several general principles of conventional telemetry systems. A brief review shall be presented of the various system level topologies that have been used bio-telemetry systems by evaluating the strengths and weaknesses of each design methodology. In extension a design methodology is presented for the class-E power amplifier that is found in virtually all inductively coupled power links for bio-medical applications. We shall also present a brief introduction to UWB technology as well as a review of state-of-the-art neural interface systems to project our system requirements and topology.

Chapter 3 focuses on the forward link design by introducing a analytical description of the coil link in order to formulate target figures of merit followed by the employed power amplifier design with the associated simulation results.  Techniques that minimize the loss introduced by phase transitions from BPSK modulation will be a very particular consideration that will be made at the end of the chapter together with the corresponding low complexity BSPK demodulator.

Chapter 4 in analogy focuses on the reverse link design by first introducing the basis for UWB techniques and proposing a scalable modulation technique for low power applications.  This is followed by the design considerations of a digitally calibrated oscillator as well as an energy efficient bi-phasic UWB pulse generator. We shall also present the UWB antenna design considerations and propose a receiver topology for testing purposes.

Chapter 5 concludes upon the developments made throughout this thesis in addition to presenting a generalized evaluation. Finally aspects for future work and improvement shall be noted.

# 3 Contributions

The main contribution presented by this thesis are outlined below
 - A complete wireless power transmission link trough coupled coil that achieves a net 45% efficiency with the measured coil characteristics as well study on the trade offs of circular and rectangular coil geometries.
 - With the developed class E power amplifier an energy efficient BPSK modulation technique is introduced that not require additional supply modulation techniques in addition to a low power BPSK demodulator that consumes 1.5 uW from the unregulated supply.
 - Framework for the UWB delay modulation scheme with conservative estimated on BER values and a scalable architecture for implementation.
 - Complete UWB transceiver architecture is developed that transmits data at 890 fj/bit for which a full custom digital layout is designed that occupies 200 um by 300 um.
 - Miniaturized UWB antenna design that occupies 1.3 cm² and achieves -12 dB reflection coefficient and sub 50 ps group delay over a bandwidth of 4GHz.

# 4 Introduction

The neural sensory implants of interest is generally located in a vital location such as under the skull and characteristically needs to process large aggregates of data as a multitude of neurons are recorded simultaneously for prolonged periods of time. As a result it is particularly challenging to power the implant as monthly operations to replace a battery can severely endanger the subject to infection. Moreover power requirements of several milliwatt would require a large battery. The inductive link in principle allows for a relatively efficient transmission of power without puncturing the skin while giving room for data transmission.

The overall design of telemetry systems pertains to the field of radio frequency electronic circuit design with the inclusion of a few essential aspects from power electronics. The biomedical telemetry application however tends to relax the high frequency requirements and focus more on efficient power induction that is more suitable below the 100 MHz frequency range for maximizing power gain [^4]. Although elaborate antenna systems are still designed to allow for full system-on-chip (SOC) integration the trend towards ubiquitous adoption of integrated UWB transmitters in implants seems to have given a different spin on the RF design aspect. As most bio-telemetry communication links are enabled trough near field coupling there is little gained for high antenna directivity and un-optimized RF coils have been demonstrated sufficient for UWB trough-skin broundary transmission [^5]. Moreover design theory behind UWB is more based on time-domain analysis aimed at minimizing pulse distortion where the traditional harmonic frequency analysis fails to give sufficient insight.

In this chapter, a review of the various system level topologies that have been used in recent bio-telemetry systems is presented by evaluating the strengths and weaknesses of each design methodology. In extension, a design methodology is briefly presented for the class-E power amplifier that ubiquitus inl inductively coupled power links. In addition, an introduction to UWB technology is presented together with a review of state-of-the-art neural interface systems to project our system requirements and topology.

# 5 Bio-Telemetry Schemes

Abstractly speaking, modern telemetry systems can be seen as a 3 channel system. As illustrated in figure 1 these channels correspond to power transmission, forward data transmission, and reverse data transmission. Although 3-channel systems have been reported where each channel is optimized for a single function in terms of carrier frequency and coil/antenna designs the component count is very high. In accordance to the characteristic of the reverse link where a fast bit rate is generally desired, the reverse link is often designed with explicit RF considerations by introducing a far field antenna but it has been demonstrated that single loop coils have considerable potential for near field coupling of RF radiation through the skin [^6]. The power transmission is generally done through inductive coupling at a frequency where the Q-factor of the coils is maximized and losses from the environment are kept to a minimum [^7]. The forward link may very similarly be designed trough inductive coupling but a higher carrier frequency is preferred to allow for more substantial data rates while trading off losses induced by the coils which have been shown to dominate over tissue absorbtions for frequencies above 100KHz [^8].

{{< figure src="/images/msc-thesis/s1.png" title="Figure 1: Generalized system architechture of a bi-directional telemetry system for medical implants." width="500" >}}

Contemporary implant systems have mainly focused on improving the system by choosing the right modulation techniques that allow two channels to by combined into one while still achieving similar performance and there by significantly reducing the number of off chip components on the implant side. In some sense this also relaxes the inter-channel interference as the as the interaction between power forward data transmission, for example, is modeled much more explicitly when combined without interference being prone to variations in the coupling coefficients.

The simplest implementatio for data modulation is amplitude modulation, ASK, of power wave form, where the DC-DC regulator driving the supply of the PA is directly adjusted according to a binary bit stream. However a supply regulation control loop is generally implemented on a system level that fixes the average induced power such that the supply at the implant side maintains a stable voltage. This control loop is rather essential as the coils may misalign or move during operation such that the supply must be recalibrated to avoid component damage or injuries due to overheating hence it is not desirable to introduce modulation noise directly into the control loop.

The alternative to ASK is FSK or PSK which allow for much faster data rates due to the fact that the detection of the phase/frequency shift is not limited by the relaxation time of the resonant pair at the implant side and since the Q-factors of the inductors is desirably large to minimize losses this response time limits modulation speeds [^9]. FSK generally doubles the number of resonant components required for power transmission to be efficient at both frequencies and may be considered undesirable but, unlike ASK and PSK, modulation does not degrade the power transmission efficiency. A binary phase shift keying can achieve faster uplink data rates than ASK without the need of additional passives but as will be discussed in chapter 3 the resonant modes of the two phase states are complementary to one another such that during phase transition a significant amount of power lost which results in the degradation in transmission efficiency when data is being transmitted trough the link. Technically speaking, inefficiency during modulation is not a major concern as data sent through the forward link is primarily used during system set up and remains inactive for the majority of the implant’s lifetime but it requires additional consideration to avoid system failure during the transmission of large amount of calibration data.

More recently the reverse link has also been integrated into the power transmission channel as well by using Load Shift Keying (LSK). This modulation technique is based on the fact that the current drained from the secondary power coil L2 is coupled to the total power drained from the power amplifier. A common implementation of this illustrated in figure 2 where a simple transistor driven by a OOK modulated data stream pulses a short circuit current from L2 which can be detected at the primary power coil. Note that the PA can still be modulated with the forward link data stream. This approach introduces a significant amount of simplicity into the design as power and bi-directional data is transmitted through a single coil potentially eliminating all off-chip components. In addition power hungry driver circuitry required for driving the antenna/coil of the reverse link has also been eliminated. The drawback naturally lies with the fact that the two data channels interfere with one another more severely than with separate coils regardless of the modulation schemes and moreover all data rates are limited by the bandwidth the inductive link. In addition, a significant amount of strain is put on the requirements of the on-chip supply regulator as the average power induced from the coil is continuously being modulated with higher frequency components from the OOK switching characteristic and may require the high-performance analog instrumentation components to have differential architectures that require more power and area.

{{< figure src="/images/msc-thesis/s2.png" title="Figure 2: LSK based telemetry system architechture" width="500" >}}

# 6 Power Amplifiers for Biomedical Applications

A quintessential aspect of power induction is minimizing losses at all stages of the power transmission link where the power amplifier used to be at the centre of attention but with the introduction of switch mode power amplifiers the near lossless operation has now become standard for MHz PA applications. The more classical load driving techniques that use class B or class C modes of operation made achieving over 70% efficiency with a varying load such as an implant challenging due to the matching requirements. Switch mode power amplifiers generally refer to amplifier topologies where the main driving transistor is severely over driven to the extent that the output is far into the non-linear domain by clipping effects such that the transistor can essentially be treated as an ideal switch. The basis of lossless switch mode operation lies with making sure the power transistor does not dissipate power and disregarding how nonlinear the intermediate waveforms are as long as a high-Q LC components are used to terminate all unwanted harmonics an ideal efficiency is expected at the load as all the sources of loss are negated. Since the switch mode structure inherently requires a LC pair it is ideal for driving an inductive load as the coil can be absorbed into the network without additional design considerations.

In order to gain further insight to the operation of switch mode amplifiers we shall present a time domain analysis of the switch mode Class E amplifier topology which allows us to mitigate nearly all losses by absorbing the power transistor paracitics into the network.

{{< figure src="/images/msc-thesis/pa1.png" title="Figure 3: Detailed Class-E PA schematic and the inductive link." width="500" >}}

The topology illustrated in figure 3 shows a power transistor biased by a choke inductor driving the primary coil which is coupled to the secondary coil that drives a half-wave rectifier. It is assumed that the DC load, coil Q-factor, and coil inductance is known for this analysis as well as \\(C_{L2}\\) being choosen according to the required switching frequency such that it forms a resonant tank with \\(L_2\\). The actual Class-E operation is derived trough the biasing condition of the transistor with a over-driven digital input which allows the transistor to be approximated by an ideal switch. More over it can be assumed that the current driving the primary & secondary coils is purely sinusoidal as the $L_1 C_{L1}$ tank is used to filter out non linearities introduced by the swithcing operation of the transistors. Before going into analytical details, the overall circuit needs to be reduced to a simple PA structure driving a single complex load. Note that the effective AC load that the rectifier presents to the secondary coil can be approximated in term of expected voltage drop across the diode bridge and the DC load resistor, that is;

$$  R_{AC} = \frac{1}{2} \frac{(V_{Load} + V_{Diode})^2}{P_{Load} P_{Diode}} || R_{Q2}  $$

Now, using simple circuit techniques the circuit can be further reduced at the resonant switching frequency $\omega_s = (C_{L2} \cdot L_2 )^{-1/2}$ where the resonant tank at the secondary coil provides the largest reduction in coil losses [^10].

{{< figure src="/images/msc-thesis/pa2.png" title="Figure 4: Circuit schematic illustrating circuit reductions." width="500" >}}

{{< figure src="/images/msc-thesis/pa3.png" title="Figure 5: Schematic of the reduced circuit representing a Class-E PA with inductive load." width="500" >}}

Note that the series resistance of \\(L_1\\) may directly be absorbed by the effective real load \\(R_{EL}\\) and the series resistnace of \\(L_2\\) is absrobed trough equivilent loss of the the unloaded Q-factor corresponding to the resonant $L_2 C_{L2}$ tank. Formally, it has been assumed that the ac current observed at the resistive load purely sinusoidal and expressed as follows;

$$ i_{R}(\theta) = I_{rf} \cdot cos( \omega_s t ) =  m I_{dc} \cdot cos( \theta ) $$

Where m is the ratio between \\(I_{rf}\\) and \\(I_{dc}\\) and $\omega_s t$ is normalized to \\(\theta\\) as the system is periodic over $T = 2\pi \backslash \omega_s$. Furthermore, let the switch be closed for some abitrary reference frame defined by \\(-a_1\\) and \\(a_2\\) centered around 0, such that;

$$ i_{sw} = \begin{cases} I_{dc} \left[1+m\cdot cos( \theta ) \right], & \mbox{for } -a_1 \textless \theta \textless a_2  0, & \mbox{ otherwise} \end{cases} $$

Note that the parameter \\(m\\) may be found be evaluating the charge conservation at the node \\(V_d\\) of the capcitor \\(C_{ds}\\) by;

$$ I_{dc} = \frac{I_{dc}}{2\pi} \int \limits_{-a_1}^{a_2} \left[1+m\cdot cos( \theta ) \right] d\theta  $$

Similarly by integration the at the node \\(V_d\\) is given by;

$$ v_d (\theta) = \begin{cases} 0 , & \mbox{for } -a_1 \textless \theta \textless a_2  \frac{I_{dc}}{\omega C_{ds}} [ \theta - m \cdot sin(\theta) - a_2 - m \cdot sin ( a_2 ) ], & \mbox{ otherwise} \end{cases} $$

Given these waveforms one may perform a transform integral to find the power of the fundamental quadrature components which is expected to drive the load with the sinusoidal current \\(I_{rf}\\).

$$  V_{di} = \frac{I_{dc}}{\pi \cdot \omega C_{ds}} \cdot \frac{1}{2m} [ m \cdot sin^2 ( a_1 ) - m \cdot sin^2 (a_2) + 2 \cdot cos^2 ( a_1 ) - 2 \cdot cos^2 ( a_2 )] $$

$$  V_{dq} = \frac{m \cdot I_{dc}}{2 \pi \cdot \omega C_{ds}} \left[ m \left( sin^2 ( a_1 ) + sin^2 (a_2) \right) + \frac{ sin (2 a_1 ) - sin (2 a_2 ) }{2} + 2 \cdot cos ( a_1 ) sin ( a_2 ) \right] $$


With these components the phasor at the \\(V_d\\) side of \\(C_{L1}\\) must be match to the phasor at the known load $X_L + R_{EL}$ which specifies the coupling capacitor \\(C_{L1}\\) by impedence matching.

$$ R_{EL} =\frac{ - V_{di}}{m \cdot I_{dc}}  $$

$$ C_{L1} =\frac{ V_{dq}}{m \cdot I_{dc}} - X_{L} $$

Finally we need to consider the conduction angle of the transisor, that is $a_1 + a_2$ in degrees. Intuetively, the larger the conduction angle (bouned by a maximum value of 180 degrees) of the transistor the more dynamic current oscillating trough the primary tank of the circuit for a given capacitance \\(C_{ds}\\) but this also results in a very large peak voltage at the drain of the power transistor inducing a significant amound of stress at the pinch-off region in the channel. For high power applications a conduction angle of 110 degrees is generally suggested for trading off driving capability and compoent lifetime but since bio-telemetry power requirements are small and a direct interface with digital control components is desirable, the PA presented in chapter 3 has a conduction angle of 180 degrees.

Note that one can also extract the DC component through using a transform integral which illustrates explicitly the linear scaling associated with the supply voltage and current load at the inductor. This characteristic is particularly useful for fine tuning the final PA configuration as it is initially difficult to specify the exact waveform at the rectifier, hence minimizing the power dissipated by the diodes remains challenging from the first cut design but is done at ease with simulation support.

# 7 Ultra Wide Band Technology

The UWB system is historically based on the spark gap transmitters developed by Marconi in the 1900s [^11]. Although there was potential for ground breaking data rates, the ability to control the UWB spectrum at the time was still in its infancy and made inter channel and multi user interference a serious problem. This ultimately resulted in the disregard for wide band communication in favor for the narrowband technology that was easier to regulate with respect to multiple end-users. The more recent 3.1GHz to 10.6GHz spectrum allocation for UWB applications that occupy at least 500MHz by the Federal Communications Commission (FCC) of United States in 2002 has sparked new interests in the field as commercial use is now permitted with a limited power spectral density of -41.3 dBm/MHz [^12].

The recent developments in ultra-wideband (UWB) technology have made a significant impact on a broad range of applications because it presents a set of relatively unique advantages: very short duty cycles, low power consumption and simple architectures which are ideal for modern cost efficient SOC miniaturizations that are often the focus of state-of-the-art research projects. In this respect, UWB has promised phenomenal performance for short range wireless channels allowing up to 100Mb/s data rates under very strict sub-mili watt power budgets with all-digital transmitter architectures that are much more robust in performance than their analog wave-mixing counterpart that can often not be integrated on the same chip due to substrate interference issues from other system components.

{{< figure src="/images/msc-thesis/spec.png" title="Figure 6: Illustration of the spectral characteristics for the three main classes of communication technologies and the associated modulation schemes." width="500" >}}

The foundation of UWB systems based around the characteristic low spectral density that results from very short pulses of energy but embody a very wide signal bandwidth. This characteristic allows the transmission of a signal with spectral energy distributed below the noise floor eliminating the chance of interference with coherent narrowband systems. The basis on which UWB is assured to attain the phenomenal bit rates suggested earlier comes from the well-known Shannon-Nyquist criterion that dictates the maximum channel capacity, \\(C\\), which can be achieved with arbitrarily small but nonzero probability of error and is given by [^13];

$$ C = BW \cdot log_2 \left( 1 + \frac{E_{signal}}{E_{noise}} \right) $$

Where  \\(BW\\), \\(E_{signal}\\), \\(E_{noise}\\) are the channel bandwith, recieved in-band signal energy, recieved in-band noise energy respectively. Recognizing that SNR, \\(E_{signal}\\) / \\(E_{noise}\\) scales almost linearly with the total system power on both the transmitter and receiver side we observe that improving SNR by dissipating more power will, as disappointing as it is for high SNR environments such as nearfield biotelemetry, only improve the channel capacity in logarithmic fashion. However with a given bandwidth of several GHz we can still assure ourselves a Mb/s bit rate even with poor SNR ratios due to ultra low power transmitter operation from ther linear dependency of bandwidth.

Some of the most significant developments in this field lie with the fully integrated CMOS pulse shapers that adhere to the FCC mask regulations [^14]. Pulse shapers not pertaining to the field of biomedical implants generally quote the energy dissipated per pulse FOM which ranges from 2nJ/pulse to some of the more recent work that nearly achievies 4pJ/pulse [^15]. There have been several publication have proposed using a UWB reverse link data transmission for biomedical telemetry with much success in terms of low power operation and have achieved 900fJ/pulse but did not present spectral compliance[^16].

There are three performance metrics of the UWB pulse that are of interest for commercial applications as they allow complete specification of the signal to noise and interference ratios for linear receivers [^17]. These three metrics correspond to spectral efficiency, out-of-band emissions, and time-bandwidth product [^18].

The first of which being the most intuitive, that is the spectral efficiency, which indicates how efficiently the designated spectrum is used in terms of how well all the radiated energy is confined within the 10dB ultra-wide bandwidth. This is expressed as;

$$ \eta_{ch} = \frac{E_{ch}}{BW_{-10dB} \cdot max ( PSD_{W / MHz})} $$

Where the total in band spectral energy, \\(E_{ch}\\), is given by

$$ E_{ch} = \frac{1}{2 \pi} \int_{BW_{-10dB}} PSD ( \omega ) d\omega $$

The second figure of merit for UWB pulses evaluates the normalized amount of spurious spectral energy is generated by the pulse. That is;

$$ \eta_{0} = \frac{E_{tot} - E_{ch}}{E_{ch}} $$

Where the total radiated energy, \\(E_{tot}\\), is given by the time-domain integral

$$ E_{tot} = \int^{\infty}_{-\infty} p(t)^2 dt $$

Finally, the time-bandwidth product primarily indicates the utility of the pulse in terms of being able to carry information. Consider for example the Sinc function which precisely has 0% out of band emissions however its time domain square power is unbounded indicated by the divergent integral for \\(d^2\\). This implies that modulation based on a ideal Sinc wavelet is non-realizable by a causal system. The time-bandwidth product being related to the standard deviation in the spectral intensity and time domain intensity which is formulated as follows;

$$ D^2 = \frac{1}{2 \pi \cdot E_s}  \int^{\infty}_{-\infty} \omega^2 \cdot | PSD(\omega)|^2 d \omega $$

Where the total radiated spectral energy, \\(E_{s}\\), is given by the frequency-domain integral\

$$ E_s = \frac{1}{2\pi}  \int^{\infty}_{-\infty} | PSD(\omega)|^2 d \omega $$

$$ d^2 = \frac{1}{E_{tot}}  \int^{\infty}_{-\infty} t^2 \cdot | f(t) |^2 dt $$

Such that the time-bandwidth product is summarized as;

$$ B_{t \omega} = D \cdot d $$

Table 1: Summary of the UWB FOM performance for different classes of analytic pulses[^1].
| | Spectral Efficiency | Out-of-Band Emissions | Time-BW Product|
|----|----|----|----|
|Sinc | 100% | 0% | (\infty) |
|Square | 60% | 12.8% | (\infty) |
|(2^{nd}) order | 59.2% | (2.8%) | 0.55 |
|Root-Raised cosine | 84.6% | (0.4%) | 0.85 |
|Gaussian | 56.5% | (3.3%) | 0.50 |
|Tanh | (58.4%) | (2.7%) | 0.53 |

A significant amount of progress has already been made towards to maximizing these figures of merit in a more general UWB framework by means of photonics and microwave systems [^19]. Only a select few of these advances are fully integrated systems and since compact integrability is the strict requirement for the implant side system there is a still lot of room for improvement for current implant-compatible UWB transceivers.

# 8 UWB Pulse Generation

Fully integrated UWB technology is a relatively recent breakthrough, as previous pulse generation systems were primarily based on step recovery and tunnel diodes that under pulsed excitation produced a very different radiation spectrum that carrier based modulation schemes [^20]. Interestingly the spectrum used for time domain UWB encoding was essentially the modulated impulse response of the diode in operation. Moreover these wideband spectrums were found to allow much more accurate special resolution as well as exhibit some degree of immunity to passive interference (i.e. echos) [^21]. The integrated UWB framework bases its pulse generation on a more synthetic approach as the GHz operation of current CMOS technology allows pulse modulation with pulse width far below the average temporal UWB pulse duration which is around 1ns. This in many cases has allowed for piece wise reconstruction of a theoretically derive pulse shape such as those mentioned in table 1.

{{< figure src="/images/msc-thesis/pl2.png" title="Figure 7: (left) spectrial representation of the oscilator and modulation waveforms (right) resulting UWB spectrum due to mixing." width="500" >}}

The most elementary form of fully integrated UWB pulse generation is derived from sub GHz OOK modulation of the GHz oscillator [^22]. With the frequency domain transforms are illustrated in figure 7, since digital and analog oscillators are relatively disposable in the FCC UWB band this approach is arguably the most elementary topology that can achieve relatively good performance if the startup and dead times are well calibrated. The challenging aspect of this topology is it is difficult to both suppress the spurious frequency sidebands as well as the DC component at the output.

{{< figure src="/images/msc-thesis/pl1.png" title="Figure 8: Illustration of the spectral characteristic of \\(1^{st}\\), \\(5^{th}\\), and \\(7^{th}\\) derivative based gaussian UWB pulses." width="500" >}}

An alternative approach to generating UWB pulses is based on the spectrum of Gaussian derivatives [^14]. The family of Gaussian functions are generally well known for their transform limited behavior and as illustrated in the previous section the Gaussian pulse has the most optimal time bandwidth product out of all analytic reference pulses. Since the actual Gaussian pulse has a strong DC component the derivatives are more realizable in RF systems.

$$ g^{(n)}(t) = \frac{d^n}{d t^n} \left( \frac{ A }{ √{2\pi} \cdot \sigma} \cdot exp \left\{ \frac{-t^2}{2 \sigma^2} \right\} \right) $$

$$ |G^{(n)} (\omega) | = A \cdot (\omega)^n \cdot exp \left\{ \frac{-( \omega \cdot \sigma )^2}{2} \right\} $$

From the expression of the Gaussian UWB spectrum it can be observed that there are two parameters for spectral tunability that allow fitting under the FCC mask which has been done extensively [^23]. These two parameters are \\(\sigma\\) and the n which correspond to the temporal pulse width and the derivative order of the Gaussian pulse. By increasing the derivative order of the generated gaussian pulse the overall spectrum is expected to shift to the higher frequencies while simutaniously becomming more concave at the fundamental lobe. By reducing \\(\sigma\\) the spectrum also shifts towards the higher frequency spectrum but in contrast does not affect the fractional bandwith of the fundametal lobe. The \\(1^{st}\\), \\(4^{th}\\), \\(5^{th}\\), and \\(7^{th}\\) order Gaussian derivatives have been demonstrated to fit the FCC mask in literature and are thier allocation under the FCC mask is illustrated in figure 8 for a relative comparison.

{{< figure src="/images/msc-thesis/pls1.png" title="Figure 9:  Schematic of a simple Gaussian Pulse shaper." width="500" >}}

{{< figure src="/images/msc-thesis/pls3.png" title="Figure 10: (left) Ultra short pulse control signals driving the Gaussian pulse shaper. (right) Piece wise constructed gaussian outout pulse fed to the antenna." width="500" >}}

The integrated circuit implementation of these Gaussian pulse generators are typically fitted by a series of consecutive current pulses feeding into a coupling capacitor toward the antenna load. The pulses are typically under a 100ps long depending on the CMOS technology and by adjusting the driving capability of the MOSFET that is active during a particular phase the amplitude of the corresponding pulse can be adjusted according to the configuration that best fits the target Gaussian model. This topology has demonstrated some of the most energy efficient pulse generators yet, achieving a spectral energy density that nearly matches the FCC mask while consuming more than 4pJ per pulse.

In extension to the Gaussian pulse generator topologies, a more generalized structure has also been introduced which focuses on efficiently generating a very board band pulse and filtering out the unwanted spectral components after amplification trough by an RF power amplifier. The filter can be implemented as an integrated on-chip LC filter or using a microwave distributed element filter topology [^24]. A particularly challenging aspect of this topology is that, although the implementation is the most robust, the filter is required to have a near constant group delay over the pass band to maintain ultra-short pulse durations and avoid pulse distortion.

{{< figure src="/images/msc-thesis/pl3.png" title="Figure 11: (left) Schematic illustrating a RF PA amplifying a Broad band pulse that is then filtered by a lumped LC network. (right) Illustration showing how the broad band pulse is filtered to meet the FCC mask requirements by using a highpass filter. " width="500" >}}

Overall these three topologies allows for fully integrated systems where often the implementation can be translated into a completely digital architecture where only the transistors driving the RF output need to be considered in analog terms. This benefit allow for rapid prototyping with very small chip area requirements, complete generation of a UWB transmitter by digital synthesis has also been demonstrated [^25].

# 9 Projecting System Requirements

Due to the very rich physiological information neural signals carry, an overwhelming amount of interest has been seen in the monitoring of en vivo neural activity. The neural interface SOCs have since developed impressive set of performance standards that is expected to be maintained for the next few years. By cross-referencing the expected advances in neural recording technology a projection can be made on system requirements in the next 3 years [^26].

Table 2: Performance overview of the most recent state-of-the-art work on neural interfaces.
| | 2009 [^27] | 2010 [^28] | 2010 [^29] | 2011 [^30] | 2011 [^31]  | 2012 [^32] |
|----|----|----|----|----|----|----|
|Technology | $0.35\mu m$ | $0.35\mu m$ | $0.35\mu m$ | $0.13\mu m$ | $0.18\mu m$ | $0.13\mu m$ |
|Channels | 1 | 128 | 128 | 1 | 32 | 96 |
|max BW (Hz) | 0.3k | 20k | 5k | 11.5k | 12k | 10k |
|ADC Resolution | 12b | 9b | 8b | 8b | 8b | 10b|
|ADC Sampling Rate (kS/s) |  1 | 640 | 111 | 10-100 | 125 | 31 |
|Data Rate per Channel (kb/s) | 12 | 360 | 111 | 100 | 250 | 313 |
|Power per Channel (W) | 895n | 344u | 190u | 75u | 10u | 68u |
|Power to Transmitter | - | 1.6mW | - | 400uW | - | - |

From the references in table one can observe that although the effective power consumption per channel is steadily decreasing below $100 \mu W$. The sample resolutions and channel bandwidths tend to be slightly over 8b and 10kHz respectively as it appears to be the sweet spot that maximizes SNR with minimal power requirements. Given the expection to see 512+ channel neural SOCs in the coming 3 years it theoretically corresponds to an uncompressed data rate of 82Mb/s that needs to be transmitted through the reverse RF link. A similar analysis would estimate the required system power budget to be an optimistic 5mW system or a more pessimistic 15mW prototyping system that considers systems that have demonstrated neural recording from animal trails with more significant weighting.

In summary, this chapter has given way for the target specification given in table 3 with the corresponding topology given by figure 12.

{{< figure src="/images/msc-thesis/s3.png" title="Figure 12: System level abstraction of the proposed biotelemetry topology." width="500" >}}

Table 3:  Performance requirements for the implantable biotelemetry system.
|Parameter | Specification |
|----|----|
|Power Delivered to load | 15mW |
|Forwardlink Data rate | 300kb/s |
|Modulation Scheme | BPSK |
|Reverselink Data rate | 80Mb/s |
|Power to Transmitter | $\textless100\mu W$ |

# 10 Forwardlink

The forward link has been the primary focus of biotelemetry systems as the induction of wireless power into the body is a challenge that has been receiving attention since the 1960s and has continued to develop alongside the innovations made in power electronics and the more recent RFID technology [^8]. However, regardless of the modulation techniques presented in chapter 2, there is a very inherent limitation that the inductive link imposes in terms of data transmission.

{{< figure src="/images/msc-thesis/s5.png" title="Figure 13: System block diagram of the forward link channel." width="500" >}}


With reference to figure 13, the system of interest here may be abstracted into four separate sections; the power amplifier, the inductive link, the demodulator, and the rectifier. Each of which substantiates a complete technical topic on its own and in association with the technical specifications given. This chapter will focus on first presenting an analytical description of the coil link in order to formulate target figures of merit followed by the employed power amplifier design with the associated simulation results.  Techniques that minimize the loss introduced by phase transitions from BPSK modulation will be a very particular consideration that will be made at the end of this chapter together with the corresponding low complexity BSPK demodulator.

# 11 Inductive Link Design

{{< figure src="/images/msc-thesis/pa4.png" title="Figure 14: Circuit model of the inductive link driven by an ideal source." width="500" >}}

With particular focus on maximizing the induced power onto the rectifier load which has be reduced to the ac equivalent \\(R_{AC}\\). With the reduced circuit illustrated in figure 14 one may be able to identify the two loss mechanisms that govern the power transmission transfer function. The first being the reflection coefficient associated with the resistive loading of inductor \\(L_1\\) due the secondary coil that is in series with the parasitic resistance of the inductor itself \\(R_1\\). The second loss mechanism abstractly lies with the self-loading of secondary inductor due to the parasitic resistor \\(R_2\\). Both of these parasitics are directly related to the Q-factor of the two inductive coils used to couple the two systems. In brief, the analytic expression for the efficiency of power induction may be derived at the resonant switching frequency, again that is $\omega_s = (C_{L2} \cdot L_2 )^{-1/2}$ , as [^33];

$$ \eta = \left[ \frac{V_L \cdot I_L}{V_s \cdot I_s} \right] = \frac{R_{eff}}{R_{eff} + R_{1}} \cdot \frac{L_2}{L_2 + R_{2} \cdot R_{AC} \cdot C_{L2}} $$

Where the effective impedance seen at the primary coil, \\(R_{eff}\\), is

$$ R_{eff} = k^2 \cdot \frac{\omega^2 \cdot L_1 \cdot L_2}{R_2 + \frac{L_2}{R_{AC} \cdot C_{L2}}} $$

Further expansion will show that this equation may be optimized for a given k in terms of the load \\(R_{AC}\\) with respect to the inductor Q of coils \\(L_1\\) & \\(L_2\\).

$$ R_{AC} \bigg|_{\eta=\eta_{max}} = \frac{\omega_s \cdot L_2}{k} \cdot √{\frac{R_1 \cdot L_2}{R_2 \cdot L_1}} =  \frac{\omega_s \cdot L_2}{k} \cdot √{\frac{Q_2 }{Q_1}} $$

Such that the peak efficiency, \\(\eta_{max}\\) may be expressed as

$$ \eta_{max} = \frac{k^2 \cdot Q_{L1} \cdot Q_{L2}}{(1+ k \cdot Q_{L1})(1+ k \cdot Q_{L2})} $$

The limiting factor associated with the coils is primarily the total chip area hence the coil geometry should maximize the coupling quality factor product per unit area. Previous systems will either opt for a coil integrated on to the PCB which allows improves the ability manufacture the end result or a coil that is implemented by a wrapped linz wire which makes scalable prototyping challenging but provides much better performance in terms of inductor Q-factors [^34]. PCB integrated inductors tend to be more lossy for a given inductance primarily because of the space requirements on the traces which prevent the dense inductance one may expect from a wire wrapped coil. The majority of published literature tends to prefer using circular geometries as their properties are accurately predicted by analytic formulas, it should be noted however that rectangular coils achieve higher coupling coefficients per unit area. With this in mind, the coils that tested in the laboratory were based on copper wire wrapped rectangular geometries. In analogy to closely space circular coils where it has been demonstrated that the mutual inductance is maximized when the primary and secondary coils have the same geometry we expect the same from the rectangular coils [^35].

{{< figure src="/images/msc-thesis/l3.png" title="Figure 15: (left) Circular Coil geometry. (center) Square coil geomerty. (right) in plane view of coils." width="500" >}}

Using EM simulation tools a simple study was conducted to confirm these findings. Using a single turn circular loop with a diameter normalized to the parameter r and a square loop with the side length also normalized to the parameter r, we studied the behavior of the coupling coefficient k with respect the out of plane distance, d, from two identical coils and the lateral in plane displacement a. The results illustrated in figure 16 confirmed that, although circular coils achieve better quality factor, the square coils achieve better coupling coefficients implying with reference to equation 24 that square coils achieve higher peak efficiency .

\\(\\) \frac{Q_{circle}}{Q_{square}} = 1.87  &  \frac{k_{circle}}{k_{square}} = 1.88 \\(\\)

{{< figure src="/images/msc-thesis/KUPL.eps" title="Figure 16: EM simulation results of the coupling coefficient with respect to the in-plane and out-of-plane normalized displacements." width="500" >}}

In accordance to the above considerations and estimates on the ac load expected to be loading the secondary coil a two coil rectangular link was prototyped. The primary coil and secondary coil were measured in the lab to evaluate the mutual inductance values where the mutual inductance was evaluated through a differential measurement [^36].

Table 4: Measured characteristics of the two inductive coils measured at coil distance of 10mm.
|Parameter | Primary Coil (L_1) | Secondary Coil (L_2)|
|----|----|----|
|Turns | 29 | 15 |
|Dimensions (mm) | 12 x 24 | 12 x 24 |
|Inductance (uH) | 46.59 | 12.67 |
|(R_s) ((\Omega) at 1MHz) | 7.49 | 3.19 |
|(k_{21}) | 0.134|

{{< figure src="/images/msc-thesis/loop.png" title="Figure 17:  Photograph of the prototype rectangular coil used for power induction." width="500" >}}

Given the measured coil characteristics, the Class-E PA was designed in accordance with the method presented in chapter 2. By introducing the simulation models of commercially available components the design was fine tuned to achieve a power transmission efficiency of 46%. The derived system delivers 15mW to a 600 ohm load corresponding to an unregulated supply of 3V. The losses from the primary and secondary contribute to 30% and 14% of the total power dissipation respectively. The off chip rectifier dissipated 8% of the total power which actually correspond to a marginal efficiency of 85%. The remaining 3% is dissipated by the RF choke and the power transistor.

{{< figure src="/images/msc-thesis/pa0.png" title="Figure 18: Detailed circuit schematic of the complete power transmission system with the component names/models annotated." width="500" >}}

Note that a the power transistor in figure 18 is a 2N7000 Fairchild N-Channel Enhancement Mode Field Effect Transistor with a maximum drain voltage rating of 60V.

{{< figure src="/images/msc-thesis/power.png" title="Figure 19: Simulation results of the power induction system in operation illustrating a average 46% PTE." width="500" >}}

# 12 Switch mode BPSK Modulation

In one respect the input waveform of the Class E amplifier is no longer trivially related to the waveform driving the load in time domain and strictly speaking the degrees of freedom at the driving transistor are now limited to two states; open circuit, and closed circuit. As a result the dynamic range of this class of amplifier is limited to the unit gain circle on the constellation diagram. This inherently presents a problem for BPSK modulation as the state transitions through the zero crossing as shown in figure 20 which for many amplifier topologies is undesirable due the fact that is strains the dynamic range requirement. In the RF domain regulating the transition behavior is rather strict as state transitions that lie beyond the capability of the amplifier result in spurious frequency components from distortion that lie outside of the designated frequency band. In the case of biomedical telemetry we shall observe that such a careless transition results a significant amount of loss in the system. To alleviate this problem we shall introduce an intermediate state to allow a smoother transition without introducing additional system complexity.

{{< figure src="/images/msc-thesis/cnst2.png" title="Figure 20: (left) Standard BPSK constellation diagram. (right) Constellation diagram of the proposed BPSK modulation scheme." width="500" >}}

Figure 21 shows the simulation results of phase transition of two BPSK modulation techniques, the first in blue being the simple BPSK modulation of a square wave and the second in red being the proposed BPSK modulation of a square wave with an intermediate state. It is obvious that there is a dramatic difference with respect to the voltage waveform seen at the rectifier input. The simple modulation technique not only results in a slow transition but there is no energy induced for a number of cycles which is detrimental to the system PTE \\(\eta\\). The proposed modulation scheme first transitions to \\(+\pi/2\\) for half a cycle before completing the phase shift towards \\(+\pi\\). It is important to note that open circuit state of the RF switch maintains its temporal duration as this is the mechanism that provides harmonic termination to the higher order harmonics that are reflected by the LC tank.

{{< figure src="/images/msc-thesis/MOD.eps" title="Figure 21: Simulation results illustrating the gain in average PTE and the destructive inteference of the two phase states during the phase transition without the intermediate state." width="500" >}}


Even with this modulation technique a linear trade off with respect to the carrier frequency and the forward data rate is still to be expected as one cycle for every phase transition fails to induce power. The expected power transfer efficiency, \\(\eta\\), during modulation is asymptotic to and approximated by the following expression.

$$ E \left[ \eta \right] = \eta_{s} \cdot ( 1 - N \cdot \frac{f_{data}}{f_{carr}} )  $$

Where \\(\eta_{s}\\), \\(f_{carr}\\), \\(f_{data}\\) are the un-modulated PTE, carrier frequency, and data rate respectively. N is the model parameter that corresponds to the number of cycles skipped as a result of a phase transition which our fitting estimates to be approximately 1 for the proposed modulation scheme. It is now clear that faster switching frequencies driving the PA will also allow for proportionally faster data rates without having to sacrifice efficiency.

{{< figure src="/images/msc-thesis/swtmd.eps" title="Figure 22: Simulation results of the PTE with respect to different data rates and the fitting parameters of the extracted model." width="500" >}}


# 13 Integrated BPSK Demodulator

To reduce overhead, the demodulator illustrated in figure 23 recovers the transmitted data stream is not based on a delay locked loop topology but based on detecting the cycle skipping of phase transitions. Although it is arguable that this type of detection is prone to failure due to coil displacement when the designated patient moves these kind of environmental factors influence the induced voltage waveform in the very low frequency spectrum that typically do not exceed 100Hz. Hence a high-pass filter behavior is introduced to the peak voltage detector using the parasitic capacitance and leakage current of the transistor M9.

{{< figure src="/images/msc-thesis/bddd.png" title="Figure 23: (left) Transistor level schematic of the threshold based phase detector. (right) Digital State machine that detects phase changes in the induced voltage waveform." width="500" >}}

The remaining operation of the circuit is intuitive, M1 shifts the voltage wave at the input of the rectifier down so that is falls below the supply voltage and the transistors M5-M7 determine & compare the voltage \\(V_{bias}\\) and the peak voltage which is $max(V_{in}-V_{thm1} - V_{thm8})$. Due to the over driving effects the output is approximately digital in characteristic where Vclk is low then Vin is larger than \\(V_{bias}\\) and \\(V_{sig}\\) is low when Vin larger than the stored peak value. These signals are processed by some simple digital circuitry to detect when \\(V_{in}\\) drops below its peak value by more than one NMOS threshold voltage. The near digital operation of this circuit the power consumption is just under $1.5 \mu W$ and simulation results of phase detection is shown below in figure 24.

{{< figure src="/images/msc-thesis/DBPSK.eps" title="Figure 24: Simulation results showing the operation of the threshold based phase detector" width="500" >}}

# 14 System Summary

In this chapter a class-E based forward transmission link was presented that couples power and transmits data. To engage the discussion on system design a common framework for coupled coils was presented to formulate a objective that brought forth the efficiency figure of merit. In addition to the schematic specifications of the transmitter, the modulation scheme was considered in detail with respect to the switch mode amplifier by identifying the underlying phase transition inefficiencies. By introducing an intermediate state the power transmission efficiency during modulation was improved an a accurate model describing the trade off between modulation rates and carrier frequency was presented. Finally the a low power BPSK demodulator was proposed.

# Reverselink

The reverse link of the biotelemetry system primarily pertains to the RF communication link that sends large amounts of data acquired in vivo by the sensory instrumentation devices to a receiver external to the body. The focus of this chapter will revolve around how this reverse link achieves a very high data rate with the minimum amount of power consumption, that is minimizing the energy per bit transmitted, and proposing a scalable modulation technique for low power applications. Followed by the design considerations of a digitally calibrated oscillator as well as an energy efficient bi-phasic UWB pulse generator, a  UWB antenna design shall be presented with considerations towards near field pulse transmission. Finally a energy detection based UWB receiver topology is proposed for testing purposes.

{{< figure src="/images/msc-thesis/s4.png" title="Figure 25: System level abstraction of the UWB transceiver." width="500" >}}

# 15 UWB Pulse Modulation

Let us first consider the two principle modulation techniques illustrated figure 26 that have been the most successful in UWB communication systems, which are binary phase shift keying (BPSK) and pulse position modulation (PPM). BPSK can be directly associated with the continuous wave modulation techniques and has shown to be a good alternative for pulse modulation that does not distort the output spectrum significantly [^37]. PPM is based on temporal delays and advances of the UWB pulse to modulate the signal. Current PPM systems are based on modulation with reference to a receiver oscillator that is locked through a digital Costas loop equivalent that requires transmitter dead time for synchronization. As current pulse generators consume at least several pJ per pulse we may assume that over 80% of the system's power consumption will be due to the actual output pulse driving the antenna.The interest here lies with encoding a single pulse with multiple bits to maximize efficiency. Simply combining the two modulation techniques is the easy way to boost efficiency but may not be worth the increase in system complexity.

{{< figure src="/images/msc-thesis/cnst.png" title="Figure 26: (left) Time-domain representation of BPSK & PPM modulation schemes. (right) Constellation diagrams of  BPSK & PPM modulation schemes illustrating the inherent SNR reduction for PPM." width="500" >}}

The bottle neck that prevents a scalable system that encodes multiple pulse positions lies with how the temporal delay are generated in contemporary designs. For non-coherent detection systems these delays must be relatively small and accurate to maintain correct detection on the receiver end which if scaled up would result in too much calibration overhead to tune each pulse position. For coherent based UWB receivers the pulses must be orthogonal with respect to the detection window which is even more challenging for detecting multiple phase states.  Instead if the delay of a fixed period is used from a calibrated digital oscillator (DCO) and multiple pulses are allowed within a short reference frame, the scaling of the position encoding mechanism can be improved in a fundamental way while maintaining system simplicity. More importantly, using a DCO allows us to dedicate a lot of resources for fine tuning the delay of a single element where if multiple delay elements need to be used the restricted resources would limit the tuning of the resulting delay and introduce unwanted phase noise.

{{< figure src="/images/msc-thesis/n2.png" title="Figure 27: (left) Simple delay encoded pulses with reference to a DCO clock. (right) Pulses encoded by the cascading of two delay symbols in a single data word." width="500" >}}

As illustrated above in figure 27, the data is essentially encoded in the delay between pulses. More importantly, note that the pulse package is encoded with reference to the first pulse which allows for accurate receiver phase locking. The implications of this type of ‘delay encoding’ are quite significant. First and foremost the energy detection receiver can now actually be asynchronous negating the need for startup dead time. Since efficiency improves only by the logarithm of the maximum delay it is not area efficient to encode large delays but by cascading multiple encoded delays after one another bit rate, area, and efficiency can be traded off with a significant amount of flexibility. Moreover by omitting the last pulse of the package a delay of 0 can be encoded for improved efficiency.

It should also be apparent that this approach has two main draw backs, the first being that it is particularly sensitive to the DCO frequency off sets for long delays that integrate to large amount of phase noise over the signal window. The other drawback is to maintain FCC mask compliance the peak output power of the UWB pulse must be reduced which degrades the signal to noise ratio. On the other hand however this modulation technique can tolerate a temporal equivalent of phase noise equal to half the DCO’s period.

To give further insight to the expected degradation in the bit error rate (BER), let us consider the absolute worst case scenario where the entire word needs to be detected by a linear receiver. That is, each symbol transmitted needs to be detected at the receiver and is subject to the same AWGN from the channel. For simplicity a threshold detection receiver model has been adopted that integrates the incident RF power waveform by self mixing and samples the accumulated energy before resetting the integrator for the next reference window at a period of \\(T_w\\). In addition, let us assume the signal band with is known such that the probability of detecting a pulse, \\(P_{bit}\\), for \\(\frac{E_b}{N_0}\\)\textless $\frac{T_w BW}{2}$ is given by [^17];

$$ P_{bit}=Q\left(  \frac{E_b / N_0}{√{2T_w \cdot BW + 2E_b / N_0}} \right)   where  Q(x)=\int^{\infty}_x \frac{exp(\frac{-t^2}{2})}{√{2\pi}} dt $$

Here \\(E_b\\) and \\(N_0\\) denote the energy in the pulse and AWG noise over the integration window \\(T_w\\). In extension the expected value of the BER for this particular modulation scheme may be evaluated by considering the probability of detecting the whole word correctly, the probability of sending that particular word, and the number of bits transmitted per word. For simplicity assume each word is equiprobable, which is sub-optimal source coding but regardless, then for the simple case of non-cascaded delay encoding the BER may be expressed as;

$$ BER_1 = \frac{1 - \sum\limits_{i=1}^{D_{max}} \left[ \frac{(1-P_{bit})^{i+1}}{D_{max}}\right]    }{2+log_2(D_{max})} $$

Where \\(D_{max}\\) is the maximum delay encoded by the transmitter. If the BER of a N times cascaded delay system is to be evaluated then the previous expression is simply adjusted in the same regard to recomputing the expected value and the number of bits per word.

$$ BER_N = \frac{1}{1 + N + \sum\limits_{j=1}^{N} log_2(A_j)} \cdot  \left\{ 1 - \frac{1 - \sum\limits_{i=N}^{D_{max}} \left[a_i \cdot (1-P_{bit})^{i+1}\right]    } {(\sum\limits_{i=N}^{D_{max}} a_i)} \right\} $$

Here the series \\(a_i\\) denoted the number of ways one can encode a word in the cascaded system with \\(i\\) delays, note that for each cascade of delays the minimum number of delays is 1. The series \\(A_j\\) denotes the maximum possible delay ecoded by the \\(j^{th}\\) cascaded delay and N denotes the number of cascaded delays. To find a closed form expression for th series \\(a_i\\) one must consider the problem of sorting i elements in N sets that are constrained to the carnality given by the series \\(A_j\\). For the proposed system where \\(N=2\\), the series is given by;

$$ a_i \bigg|_{N=2}= (1+ i) - \sum\limits_{j=1}^{2} \left[ \sum\limits_{k=Aj+1}^{i} 1 \right] $$

Where $A_j=\{8 , 4\}$. These results confirm our previous statement that the expected BER worsens as the maximum possible encoded delay is increased but by increasing N this degredation can be aleviated by as the bit rate is increased by N and the N sum over the log maximum delay of each cascaded delay.

# 16 System Architecture

The system architecture abstraction illustrated in figure 28 is the proposed integrated UWB transmitter which consists of three main components; DCO, Delay Modulator, and Pulse shaper. Although the previous discussion has pointed out the general purpose of using an on-chip oscillator it should also be noted that such high frequency oscillators can dissipate a significant amount of power. To alleviate the power hungry behavior of the DCO a feedback loop is introduced into the system that enables very exact duty cycles such that the oscillator is only switched on to generate the required number of delays and is turned off once the delay encoded package is generated saving a significant amount of power as the complete package duration is on average only half the maximum encoded delay for single delay encoded equiproportional set of words.

{{< figure src="/images/msc-thesis/mod.png" title="Figure 28: System level abstraction of the UWB transmitter architecture." width="500" >}}

The proposed system uses a 10MHz reference input clock generated by an accurate crystal oscillator and will be used to both calibrate the DCO trough a frequency locked loop (FLL) as well as being the reference for the first pulse of the data package that partly acts as a preamble. The delay modulator is essentially a pulse swallow circuit where the decision to swallow a pulse (i.e. introduce a delay) is encoded in a shift register feeding the D flip flop.

# 17 Digitally Calibrated Oscillator

The main challenge in designing the DCO lies with the fact the digital oscillators are very prone to variation in the oscillation frequency as a result of variation in supply, process parameters, and layout parasitics/mismatch. The Monte Carlo simulation in figure 29 shows that, if the presented DCO topology were uncalibrated, the oscillation frequency would have a standard deviation of 45MHz which as discussed previously results in large amounts of phase noise at the receiver. To alleviate this problem a two stage calibration mechanism has introduced with a total resolution of 8 bit to assure a large and accurate tunability range of the oscillation center frequency. The 4 most significant bits calibrate the main capacitive load of the DCO which is a binary weighted Metal-Insulator-Metal capacitive array, with unit capacitance of 5fF, by connecting an arbitrary combination of capacitors to ground and leaving the rest floating. The 4 least significant bits calibrate the NMOS driving capability of an inverter which inherently allows for tuning at a much more precise scale as the transistors can be well matched without taking up a considerable amount of area with only fractional differences in their size.

{{< figure src="/images/msc-thesis/MC.eps" title="Figure 29: Monte-Carlo simulation result of the uncalibrated Oscillation frequency." width="500" >}}

The DCO also includes a Frequency Locked Loop (FLL) that during the calibration phase will tune the DCO output frequency to match that of an accurate reference clock. A fully digital implementation was chosen so minimize area and so that the self-calibration loop can be switched off during normal operation. Although Phase Locked Loops (PLLs) are generally preferred for this particular kind of functionality due to their quicker lock-on time, the all-digital FLL in figure 30 surpasses the all-digital PLL in simplicity as no digital loop filter is required.

The principle of operation of the FLL is based on detecting which clock has a faster rate of rising edges by using a simple set reset latch that is set by reference clock and reset by the DCO clock. If the DCO is resetting the latch more often than the reference lock is setting the latch a pulse is generated at the output of the frequency detector that increments or decrements an 8 bit counter that calibrates the DCO proportionally. Similarly if the latch is set more often than reset a pulse is also generated such that the rate of pulses at the output of the frequency detector is directly equal to the absolute difference in frequency between the reference and DCO clock. The state that persists while these pulses are generated indicates whether the DCO frequency must increase or decrease. Note that the generated DCO clock is divided by a factor of 50 such that the 500MHz clock can be calibrated with respect to a low cost off the shelf 10MHz crystal.

{{< figure src="/images/msc-thesis/dco.png" title="Figure 30: Schematic of the Frequency locked loop used to enable self-calibration of the DCO" width="500" >}}

Figure 31 Illustrates that the presented DCO exceeds a 3 sigma tunability range with respect to the expected standard deviation in DCO frequency with a resolution of 1.58MHz which corresponds to oscillation period that is accurate to ±4ps. The DCO consumes an average of $72 \mu W$ during continuous operation.

{{< figure src="/images/msc-thesis/DCO.eps" title="Figure 31: Simulation result of the frequency range capability of the DCO." width="500" >}}

{{< figure src="/images/msc-thesis/step.eps" title="Figure 32: Transient simulation illustrating the response of the FLL due to a step decrease in reference frequency." width="500" >}}

# 18 Bi-phasic UWB Pulse Generator

In order to satisfy the FCC regulations for UWB communication [^12], two different approaches have been presented in previous literature. One approach is based on modulating the envelope of a RF oscillator output which allows for simultaneous UWB communication in multiple frequency bands [^22]. The other approach is based on maximizing the spectral efficiency by fitting the UWB pulse shape to a Gaussian derivative that optimally fits the FCC mask by piecewise modulation of multiple current pulses [^38]. The design proposed here is a hybrid between these two approaches employing a simple all-digital architecture that generates a UWB pulse with improved energy efficiency using an oscillator output shaped by piece wise current pulses.

The pulse generation techniquest presented are has been partly adopted from previous work that used integrated LC components to filter out the unwanted spectrum to meet the FCC mask requirements [^39]. However instead of dissipating the unwanted spectral energy, a lossy LC resonator is used to recycle the unwanted spectral energy and modulate this to its resonant frequency. Abstractly speaking, the inductor is pulsed with current over 180ps. This induces energy that is stored in the magnetic field and is gradually dissipated in the load (over 1ns while the LC pair resonates in response to the impulse). This integrated pulse generator designed is based on a 0.18\\(\mu\\)m CMOS technology using a 1.2V supply and assuming a 50\\(\Omega\\) termination.

{{< figure src="/images/msc-thesis/puls.png" title="Figure 33: Schematic Illustration of the Digital pre-shaping. Note that the relative temporal delays are not to scale." width="500" >}}

The Digital pre-shaper is shown in figure 33. This uses a popular glitch generator to generate 180ps long Gaussian like pulses, which are demultiplexed to two inverter chains to boost the driving capability of the output. It is important to note that these chains have a different output polarity but both output the buffered pulse together with a delayed and inverted pulse, driving the transistors sourcing the inductor with pulsed current (shown in figure 34). The purpose of the delayed pulse is to cancel the DC component generated by the transient impulse response of the lossy LC resonator, by injecting an equal but complementary pulse at the opposite port of the inductor. By driving either the end connected to the load, or the \\(C_{res}\\) end of the inductor first, the polarity of the UWB pulse is well controlled.

The illustration in figure 33 also shows how a simple shift register can interface the UWB transmitter with a parallel input data stream. With reference to fig, it is interesting to note that since the transistor pairs M1, M4, M2, and M3 are matched in terms of driving capability this particular topology is immune to variation in pulse length which may easily distort the performance of aggressive UWB pulse generators that use multiple glitch generators to shape the pulse.

{{< figure src="/images/msc-thesis/rf.png" title="Figure 34: Circuit schematic of the RF section (parasitics not shown) - Lres = 4nH; Cres = 200fF." width="500" >}}

Since both the total pulse energy and pulse width (due to ringing) is directly proportional to the Q of the resonator, one must trade off pulse length for amplitude where a higher Q results in longer ringing but also larger peak to peak values. In this particular case, a single layer 6-turn 8-sided spiral 4nH inductor with poly-silicon ground plane was used with the dimensions 4\\(\mu\\)m, 2:8\\(\mu\\)m, 96\\(\mu\\)m corresponding to the trace width, trace spacing, and outer radius respectively. The pulse energy was tuned to fall below 5% within 1ns to avoid inter symbol interference corresponding to the resonant capacitance of 200fF.

{{< figure src="/images/msc-thesis/TRAN.eps" title="Figure 35: Simulation Results of the bi-phase UWB temporal response illustrating a 350mVpp Amplitude" width="500" >}}

{{< figure src="/images/msc-thesis/DFT.eps" title="Figure 36: Simulated PSD of the designed UWB pulse & the indoor UWB FCC mask as annotated" width="500" >}}

It can be observed in figure 36 that the current output spectrum does not meet the sub 2GHz FCC mask specifications and thus future work based on this UWB pulse generator will filter this particular spectrum using the geometric resonance of the UWB antenna which can efficiently implement a high Q high pass filter and has already been demonstrated feasible [^24]. On that note, this system consumes 1.65pJ/pulse, which corresponds to an average of 16.5\\(\mu\\)W with a pulse rate frequency of 10MHz and has a competitive edge over many previous publications in terms of the energy per pulse figure of merit shown in table.

Table 5:  Performance summary and comparison of UWB transmitter.
|Reference | Output (V_{pp}) | Pulse width/BW | Power (pJ/pulse)|
|----|----|----|----|
|[^14] | 700mV | 0.38ns/7.2GHz | 15.4|
|[^40] | 600mV | 0.4ns/7.5GHz | 26.4 |
|[^15] | 500mV | 0.8ns/2GHz | 4.7 |
|[^41] | 180mV | 3.5ns/0.5GHz | 18|
|[^38] | 165-710 mV | 2.4ns/300MHz | 17.5 |
|This Work | 350mV | 1ns/4GHz | 1.65|

# 19 UWB Antenna

With fresh insights from the UWB pulse shaper presented in the previous section, there are a number of observations that can be made with respect to the requirements of the antenna with respect to bandwidth and input impedance. In particular, we require a 22dB rejection of the sub 1.6GHz band with respect to the pass band and a 50 ohm impedance across the 3-7GHz band that needs to be radiated out to the environment. The remaining standard requirements of an antenna are primarily associated with the directionality and gain of the radiation pattern which for the biotelemetry system depend on the orientation of the two antennas which is illustrated below. The antennas will essentially be coupled in the near field which is not ideal in terms of radiation efficiency but sufficient for simple SOC applications where the receiver end is not limited as strictly by power requirements such that additional gain in the RF band can be attained.

{{< figure src="/images/msc-thesis/chnl.png" title="Figure 37: Illustration showing orientation of the antennas with reference to the inductive coils and skin barrier." width="500" >}}

A planar antenna that is directional with one lobe tangential to the plane would be the most desirable for the proposed antenna orientation but the compactness of the antenna is a far more valued requirement. Note that this particular orientation avoids capacitive loading on the antenna where current densities at the highest and allows the UWB antennas to be conveniently distanced from one another without compromising the implant size. Another challenging antenna property that is required is that the radiation pattern must be stable across the ultra-wide band and more importantly that the radiated energy maintains a constant group delay at the receiver side to avoid excessive distortion of the UWB pulse. The last requirement is ultimately the most challenging as it requires the single mode of radiation retained over a bandwidth of several GHz for simple electrically small antenna structures.

A comment should be made with regard to the fundamental limitation of electrically small dipole antennas, as it can be shown that the fractional bandwidth of the antenna explicitly inverse to the quality factor of the antenna and hence it is theoretically possible to achieve UWB specification using these structures. However, the quality factor is directly related to the radiation efficiency by the Chu-Harrington limitations which inhibits the use of compact quarter wavelength dipole structures [^42]. Instead a class of “fat” monopole antennas has been introduced that provide a similar foundation for simple geometric structures that show adequate performance for UWB applications. The success of these structures lie with the many overlapping resonant modes that the geometries exhibit and hence appear to resonate over a large bandwidth. The most successful planar structure according to the demonstrated radiation efficiencies presented in literature has been the elliptical monopole off which we have based our primitive antenna design as well [^43].

{{< figure src="/images/msc-thesis/ant.jpg" title="Figure 38: (left) illustration of the UWB antenna geometric variables. (right) Photo of the exposed prototype UWB antenna. Note the darker gray rectangle indicates high dielectric substrate on both sides of the metalization." width="500" >}}

In addition to the matching requirements of the antenna, it is highly desirable if the antenna is scaled down to the smallest possible size. UWB antennas from literature are primarily based on off the self FR4 substrate have a radiating patch is on the order of $16 cm^2$. In order to scale down the antenna to around the \\(1cm^2\\) area a high dielectric substrate, RO3010, was used. More specifically, the elliptic lobe that is used to match the $50 \Omega$ co-planar transmission line is enclosed by the high dielectric substrate on both sides of the metalization leaving the radiating gap between the ground plane and the ellipse partly exposed on one face in order to avoid deteriorating the radiation efficiency.

{{< figure src="/images/msc-thesis/PROT.eps" title="Figure 39: EM simulation results illustrating the degeneration of the first resonant mode to improve performance." width="500" >}}

The basic geometry in figure 38 illustrates the addition of a elliptic lobe that is placed protruding from the ground plane towards the elliptic patch which was found to give the antenna the desired in-plane directivity of 3dB and improved wide band matching. The ground plane extension generally reduced the Q-factor of the first mode such that its resonance overlaps more continuously with the second mode as may be observed in figure 39 by the gradual improvement in the reflection coefficient as the lobe is extended towards the antenna.

{{< figure src="/images/msc-thesis/A1.eps" title="Figure 40: EM simulation of the \\(S_{11}\\) reflection coefficient for the finalized UWB antenna geometry." width="500" >}}

{{< figure src="/images/msc-thesis/TRNSM.eps" title="Figure 41: Preliminary side-by-side \\(S_{21}\\) transmission characteristic." width="500" >}}

The preliminary EM simulation results in figure 40 show adequate performance over the 3-7 GHz band in terms of a reflection coefficient below -10dB with a constant group delay that only varies by several tens of degrees. Figure 41 illustrates a more insightful  the transmission characteristic of the near field coupling that the two antennas would experience placed side by side 1cm apart. The designated bandwidth of interest, 3GHz to 7GHz, has an insertion loss of 20dB and exhibits near negligible fluctuation in the group delay, that is less than 50 ps. The corresponding finalized parameters describing the antenna geometry are listed in table 6.

Table 6: UWB antenna parameters
|Parameter | Length $(\mu m)$|
|----|----|
|R | 5000|
|(R_g) | 400|
|(R_t) | 800|
|G | 290|
|W | 440|
|C | 260|

{{< figure src="/images/msc-thesis/MA.eps" title="Figure 42: (top) Comparison of the measured and simulated \\(S_{11}\\) characteristic. (bot) PSD generated by the UWB pulse shaper for reference." width="500" >}}

The first set of prototype UWB antennas were developed through manual photo chemical etching whose reflection characteristics are shown in figure 43. The sub 5GHz band appears to match the simulation results relatively well while there are some hints of over etching. The band above 5GHz however is characteristically very different from simulations. The author believes this to be the result of edge roughness introduced by uneven distribution of spray-on photo resist that was used in the development stage as a number of other antenna samples had miniature holes in the ground plane indicating a non-homogeneous etch. There is still a level of adequacy for the measured antenna as the UWB pulse PSD covers the entire band that exhibits the ability to radiate. The high Q notch at 5.5GHz however may significantly distort UWB pulses due the corresponding fluctuation in group delay. The prototype antenna does present a respectable 2GHz bandwidth.

{{< figure src="/images/msc-thesis/chmbr.png" title="Figure 43: Photograph of the UWB antenna under test in the Imperial College anechoic chamber." width="500" >}}


# 20 Reciever

The receiver presented in this section is primarily aimed at system completeness and the testability of the power optimized UWB transmitter system as many of the strict constraints that concern the implanted system no longer apply to the external system. UWB receiver architectures generally consist of almost completely digital architectures including RF ADCs with the exception of front end tunable low noise amplifiers for pre-acquisition gain. Pulse detection methods are very much translated into the DSP domain where channel approximation algorithms have proven to be very successful at filtering and detective UWB pulses mainly because of critical and overly complex filtering requirement that needs to adapt to both the channel and the effectively unknown input spectrum of the pulse that highly distorted after transmission [^44].

{{< figure src="/images/msc-thesis/rec.png" title="Figure 44: System level abstraction of the reciever architechture." width="500" >}}

Since both the most basic coherent and non-coherent UWB receiver architectures are beyond the scope of this project a very simple energy detection system has been derived that assumes no strong interferer is transmitting in the UWB spectrum such that the UWB pulse can easily be detected by energy thresholding.

Based on this detection, a set of trigger pulses are generated ideally identical to those generated at the output of the delay modulator. Using the same DCO, the delay between these triggers can be counted by a set of registers such that the encoded information is extracted from trigger circuit recovering all data sent from the transmitter.

{{< figure src="/images/msc-thesis/dly.png" title="Figure 45: (left) Schematic of the implemented delay-locked loop. (right) Analog tuned delay element." width="500" >}}

To synchronize the two systems a delay locked loop is introduced at the receiver that uses analog delay elements in combination with a charge pump phase detector[^45]. The control loop illustrated in figure 45 synchronizes the output of the delay line \\(V_{sync}\\) with the reference clock \\(V_{ref}\\) by continuously integrating the phase difference of the two signals. As charge accumulates onto \\(C_p\\), the resulting voltage biases four cascaded delay elements that each can efficiently introduce delays up to 25ns. The actual mechanism of the analog delay element is based on around the current starving the inverter structure of M5 M4 such that the time it takes to reach the switching point of the output inverter M12 M13 is controlled. Note that once the switching point is achieved the state rapidly regenerates itself due to M8 M9 assuring a fast transition. More importantly the structure negates short circuit currents that may be introduced by the slow switching of the first stage through the transistors M14 and M11.

# 21 UWB System Summary

Transient simulations of the UWB transmitter, illustrated in figure 46, have confirmed the general operation of the delay modulator and extracted simulation of the whole system have indicated a power consumption of $68.9\mu W$ for a PRF of 10MHz. Since the transmitter is encoding the pulses with an effective data rate of 77.5 Mb/s these results correspond to a energy per bit FOM of 890fJ per bit. By extrapolating these results to find the power consumption of the system excluding the UWB pulse shaper, it can be stated that the modulator consumes 470fJ per DCO oscillation and corresponds to 34% of the over power consumption.

{{< figure src="/images/msc-thesis/POWER.eps" title="Figure 46: System level simulation results of the DCO, Modulator, and pulse shaper outputs as well as the accumulated power consumption." width="500" >}}

Although the total phase noise expected at the output of the delay modulator still needs to be characterized, the complete UWB system presents respectable performance in terms of power consumption. And from figure 42 it can be observed that there is an expected -20dB rejection in the sub 2GHz band with reference to the 3-6GHz pass band which implies that the radiated spectrum should meet the FCC requirements accordingly. It can be observed from figure 46 that for closely spaced pulses the pulse amplitude is slightly degraded due to ISI at the transmitter. This type of hysteresis is generally unwanted but can be improved by either shortening the pulse or by reducing the DCO oscillation frequency, both of which degrade the over all system power performance.

Table 7: Performance overview of recent UWB transmitters
|Reference | [^16] | [^46] | [^47] | [^25] | [^48] | [^38] | This Work |
|----|----|----|----|----|----|----|----|
|Technology (nm) | 65 | 90 | 90 | 65 | 65 | 65 | 180 |
|Modulation | Delay | PPM | BPSK | PPM | OOK | PPM |  Delay  |
|Avg. Power (W) | 660n | 718u | 3.3m | 600u | 217u | 4.36m | 68.9u |
|PRF (Hz) | 1.3M | 16.7M | 100M | 50M | 24M | 15.6M |  10M |
|Energy per bit (J/bit) | 300f | 37p | 33p | 12p | 8.5p | 17p | 890f|
|FCC compliant | No | Yes | Yes | Yes | Yes | Yes | Yes |

With reference to table 7 it can be noted that the delay modulation generally achieves respectable energy per bit FOMs in comparison to other modulation schemes as the highly energetic pulses are encoded with multiple bits. Note that even though our design was based on a less aggressive \\(180nm\\) process the UWB pulse generator allowed us to achieve comparable performance to designs that were implemented in \\(65nm\\) technologies for which the transistors achieve a transition frequency (\\(F_T\\)) that extends far beyond the UWB bandwidth which is essentially a prerequisite for employing the piece-wise reconstruction of analytically optimal wavelets.

The two figures 47 & 48 show the full custom layout that was designed for the proposed UWB transceiver. The actual transistor level layout of transmitter and receiver combined occupy approximately $100\mu m$ by $200\mu m$ with a separate self calibrated DCO for each section. The overall area is increased by 300% due to the on-chip inductor that was integrated for the UWB pulse generator. The figure  48 also shows a large array of decoupling capacitors (in yellow) that remove noise from the supply pads that may influence the DCO operation and introduce additional phase noise.

{{< figure src="/images/msc-thesis/die1.png" title="Figure 47: Detail of the Full custom Digital layout of UWB, counter clockwise, TX [DCO(red), Delay Modulator(l. blue), UWB Pulse Generator(orange)] & UWB RX [DCO(purple), Demodulator(green), DLL(yellow), RF Energy detector(d. blue)]" width="500" >}}

{{< figure src="/images/msc-thesis/die2.png" title="Figure 48: Layout sent for tape out illustrating the guard-ring (blue), RF pads (red), Integrated Inductor (green), and UWB TX/RX (green)." width="500" >}}

# 22 Conclusion

This thesis has addressed the design considerations of an implantable biotelemetry system with respect system level optimizations and presented the circuit level innovation that focused on optimizing power requirements.

During the development of the forward link in particular the modulation techniques of contemporary literature were evaluated and, with respect to the projected system requirements, BPSK modulation was found to be the most promising. This was illustrated by the fact that BPSK modulation minimizes the off-chip components and by employing the proposed modulation scheme relatively high bit rates were achieved without degrading the overall power transfer efficiency of the forward link. Moreover, the efficiency achieved illustrates that the class-E amplifier operation shows a good synergy with the BPSK modulation mechanism without the need to supply modulation techniques or additional filtering components.

Since UWB application for biomedical implants is a relatively new and emerging field a significant amount of effort was put toward developing a scalable delay encoding system that could give way for systems that maximize efficiency FOMs like sub 100fJ energy dissipation per bit transferred. The presented work allows numerous bits to reliably be encoded into a single energetic pulse with a good control over how robust the encoding scheme is towards phase noise as only one element is required to be tuned. The delay modulator presented here is for that reason integrated with a self-calibration frequency locked loop that keeps chip area to a minimum. A conservative estimate bit error rates due to channel induced AWG noise was also presented to given insight to how higher order delay encoding effects the transmission of data. With the theoretical basis covered, circuit specific elements were developed such as a widely tunable digital oscillator and a particularly energy efficient UWB pulse generator based off the impulse response of a LC resonator. In extension to the transmitter, an UWB antenna was designed where a significant improvement in the low-frequency group-delay and reflection co-efficient was found if the first resonant mode was degenerated by an asymmetric extension of the ground plane. The antenna was fabricated but fine tuning of the etching process was still required for the EM simulation results to match the measured response at the frequencies above 5GHz. Finally a simple energy detection receiver is developed that will allow testing of the full custom digital layout that was designed for fully integrated the UWB transceiver system.

# 23 Future Work

Due to the broad scope telemetry systems there are a wide range of possible future developments that can be considered in extension to what has been presented here. First and foremost it would be important to develop a more standardized receiver that is based on GHz sample acquisition through FPGA and uses a channel estimation adaptive filter to detect the delay encoded words sent by the implanted device. Secondly the UWB antenna needs to go through several process development cycles under a automated fabrication process until the antenna is well characterized. In addition the antenna need to be tuned to match the impedance of the human body right under the skin for maximum radiation efficiency which may even allow for the system to be placed deeper within the body and may be of interest for future work in association to RF powered implants. The final aspect that should be a worthwhile investment lies with developing an integrated rectifier and regulator for the forward transmission link.

# Refernces:

[^1]: D.D. Wentzloff, ''Pulse-based ultra-wideband transmitters for digital  communication,'' PhD in Electrical Engineering and Computer Science,  Massachusetts Institute of Technology, Aug. 2007.
[^2]: K.Wise, D.Anderson, J.Hetke, D.Kipke, and K.Najafi, ''Wireless implantable  microsystems: high-density electronic interfaces to the nervous system,''  Proceedings of the IEEE, vol.92, no.1, pp. 76 -- 97, jan 2004.
[^3]: A.Eftekhar, S.Paraskevopoulou, and T.Constandinou, ''Towards a next  generation neural interface: Optimizing power, bandwidth and data quality,''  in Biomedical Circuits and Systems Conference (BioCAS), 2010 IEEE,  nov. 2010, pp. 122 --125.
[^4]: S.D. M.G. Olivo, J.;Carrara, ''Optimal frequencies for inductive powering of  fully implantable biosensors for chronic and elderly patients,'' in  Sensors, 2010 IEEE, nov. 2010, pp. 99 --103.
[^5]: P.C. Y.Luo, C.Winstead, ''125mbps ultra-wideband system evaluation for  cortical implant devices,'' in Engineering in Medicine and Biology  Society,EMBC, 2012 Annual International Conference of the IEEE, Sept. 2012,  pp. 779--782.
[^6]: S.M.T. Poon, A.S.Y.;O'Driscoll, ''Optimal operating frequency in wireless  power transmission for implantable devices,'' in Engineering in  Medicine and Biology Society, 2007. EMBS 2007. 29th Annual International  Conference of the IEEE, aug. 2007, pp. 5673 --5678.
[^7]: D.Laqua, T.Just, and P.Husar, ''Measuring the attenuation characteristics of  biological tissues enabling for low power in vivo rf transmission,'' in  Engineering in Medicine and Biology Society (EMBC), 2010 Annual  International Conference of the IEEE, 31 2010-sept. 4 2010, pp. 1437 --1440.
[^8]: J.C. Schuder, J.H. Gold, and H.E. Stephenson, ''An inductively coupled rf  system for the transmission of 1 kw of power through the skin,''  Biomedical Engineering, IEEE Transactions on, vol. BME-18, no.4, pp.  265 --273, july 1971.
[^9]: M.Ghovanloo and K.Najafi, ''A wideband frequency-shift keying wireless link  for inductively powered biomedical implants,'' Circuits and Systems I:  Regular Papers, IEEE Transactions on, vol.51, no.12, pp. 2374 -- 2383,  dec. 2004.
[^10]: K.Finkenzeller, RFID Handbook: Fundamentals and Applications in  Contactless Smart Cards and Identification, 2nded.\hskip 1em plus 0.5em  minus 0.4emelax New York, NY, USA: John Wiley & Sons, Inc., 2003.
[^11]: G.Marconi, Transatlantic Wireless Telegraphy, ser. Pamphlets on  electricity.\hskip 1em plus 0.5em minus 0.4emelax New York, NY, USA: E.  Eastwood, editor, Wiley, march 1908.
[^12]: ''Federal communications commission (fcc), first report and order in the matter  of revision of part 15 of the commission's rules regarding ultra wideband  transmission systems, et-docket 98-153, fcc 02-48, released 22 april 2002.''
[^13]: T.M. Cover and J.A. Thomas, Elements of Information Theory (Wiley  Series in Telecommunications and Signal Processing).\hskip 1em plus 0.5em  minus 0.4emelax Wiley-Interscience, 2006.
[^14]: H.Kim, D.Park, and Y.Joo, ''All-digital low-power cmos pulse generator for  uwb system,'' Electronics Letters, vol.40, no.24, pp. 1534 -- 1535,  nov. 2004.
[^15]: T.-A. Phan, V.Krizhanovskii, S.-K. Han, S.-G. Lee, H.seo Oh, and N.-S. Kim,  ''4.7pj/pulse 7th derivative gaussian pulse generator for impulse radio  uwb,'' in Circuits and Systems, 2007. ISCAS 2007. IEEE International  Symposium on, may 2007, pp. 3043 --3046.
[^16]: M.Mark, Y.Chen, C.Sutardja, C.Tang, S.Gowda, M.Wagner, D.Werthimer, and  J.Rabaey, ''A 1mm3 2mbps 330fj/b transponder for implanted neural sensors,''  in VLSI Circuits (VLSIC), 2011 Symposium on, june 2011, pp. 168 --169.
[^17]: J.Proakis, Digital Communications, 4thed.\hskip 1em plus 0.5em minus  0.4emelax McGraw-Hill, Aug. 2000.
[^18]: J.Agbinya and H.Truong, ''A comparison of ultra wideband signal functions for  wireless ad hoc networks,'' in Information Technology and Applications,  2005. ICITA 2005. Third International Conference on, vol.2, july 2005, pp.  677 -- 682 vol.2.
[^19]: M.Abtahi, M.Mirshafiei, J.Magne, L.Rusch, and S.LaRochelle,  ''Ultra-wideband waveform generator based on optical pulse-shaping and fbg  tuning,'' Photonics Technology Letters, IEEE, vol.20, no.2, pp. 135  --137, jan.15, 2008.
[^20]: J.Moll and S.Hamilton, ''Physical modeling of the step recovery diode for  pulse and harmonic generation circuits,'' Proceedings of the IEEE,  vol.57, no.7, pp. 1250 -- 1259, july 1969.
[^21]: I.Immoreev and P.Fedotov, ''Ultra wideband radar systems: advantages and  disadvantages,'' in Ultra Wideband Systems and Technologies, 2002.  Digest of Papers. 2002 IEEE Conference on, 2002, pp. 201 -- 205.
[^22]: A.T. Phan, J.Lee, V.Krizhanovskii, Q.Le, S.-K. Han, and S.-G. Lee,  ''Energy-efficient low-complexity cmos pulse generator for multiband uwb  impulse radio,'' Circuits and Systems I: Regular Papers, IEEE  Transactions on, vol.55, no.11, pp. 3552 --3563, dec. 2008.
[^23]: M.Mirshafiei, M.Abtahi, P.Larochelle, and L.Rusch, ''Pulse shapes that  outperform traditional uwb antenna/waveform combinations,'' in Global  Telecommunications Conference (GLOBECOM 2010), 2010 IEEE, dec. 2010, pp. 1  --5.
[^24]: K.Li, ''Uwb bandpass filter: structure, performance and application to uwb  pulse generation,'' in Microwave Conference Proceedings, 2005. APMC  2005. Asia-Pacific Conference Proceedings, vol.1, dec. 2005, p. 4 pp.
[^25]: Y.Park and D.Wentzloff, ''An all-digital 12pj/pulse 3.1 - 6.0ghz ir-uwb  transmitter in 65nm cmos,'' in Ultra-Wideband (ICUWB), 2010 IEEE  International Conference on, vol.1, sept. 2010, pp. 1 --4.
[^26]: H.S. Ian and P.K. Konrad, ''How advances in neural recording affect data  analysis,'' pp. 139 -- 142, Feb. 2011.
[^27]: X.Xu, X.Zou, L.Yao, and Y.Lian, ''A 1-v 450-nw fully integrated biomedical  sensor interface system,'' in VLSI Circuits, 2008 IEEE Symposium on,  june 2008, pp. 78 --79.
[^28]: M.S. Chae, Z.Yang, M.Yuce, L.Hoang, and W.Liu, ''A 128-channel 6 mw  wireless neural recording ic with spike feature extraction and uwb  transmitter,'' Neural Systems and Rehabilitation Engineering, IEEE  Transactions on, vol.17, no.4, pp. 312 --321, aug. 2009.
[^29]: F.Shahrokhi, K.Abdelhalim, D.Serletis, P.Carlen, and R.Genov, ''The  128-channel fully differential digital integrated neural recording and  stimulation interface,'' Biomedical Circuits and Systems, IEEE  Transactions on, vol.4, no.3, pp. 149 --161, june 2010.
[^30]: S.Rai, J.Holleman, J.Pandey, F.Zhang, and B.Otis, ''A 500 $\mu$ w neural  tag with 2 $\mu$ vrms afe and frequency-multiplying mics/ism fsk  transmitter,'' in Solid-State Circuits Conference - Digest of Technical  Papers, 2009. ISSCC 2009. IEEE International, feb. 2009, pp. 212 --213,213a.
[^31]: W.Wattanapanitch and R.Sarpeshkar, ''A low-power 32-channel digitally  programmable neural recording integrated circuit,'' Biomedical Circuits  and Systems, IEEE Transactions on, vol.5, no.6, pp. 592 --602, dec. 2011.
[^32]: R.Walker, H.Gao, P.Nuyujukian, K.Makinwa, K.Shenoy, T.Meng, and  B.Murmann, ''A 96-channel full data rate direct neural interface in 0.13  $\mu$ m cmos,'' in VLSI Circuits (VLSIC), 2011 Symposium on, june  2011, pp. 144 --145.
[^33]: \BIBentryALTinterwordspacingR.Sarpeshkar, Ultra Low Power Bioelectronics: Fundamentals, Biomedical  Applications, and Bio-Inspired Systems, ser. Ultra Low Power Bioelectronics:  Fundamentals, Biomedical Applications, and Bio-inspired Systems.\hskip 1em  plus 0.5em minus 0.4emelax Cambridge University Press, 2010. [Online].  Available: \urlhttp://books.google.co.uk/books?id=eYPBAyDRjOUC\BIBentrySTDinterwordspacing
[^34]: U.-M. Jow and M.Ghovanloo, ''Design and optimization of printed spiral coils  for efficient transcutaneous inductive power transmission,'' Biomedical  Circuits and Systems, IEEE Transactions on, vol.1, no.3, pp. 193 --202,  sept. 2007.
[^35]: C.Zierhofer and E.Hochmair, ''Geometric approach for coupling enhancement of  magnetically coupled coils,'' Biomedical Engineering, IEEE Transactions  on, vol.43, no.7, pp. 708 --714, july 1996.
[^36]: A guide to measurement technology and techniques, 4thed.\hskip 1em plus  0.5em minus 0.4emelax Agilent Technologies, Ltd., 2009.
[^37]: M.Welborn, ''System considerations for ultra-wideband wireless networks,'' in  Radio and Wireless Conference, 2001. RAWCON 2001. IEEE, 2001, pp. 5  --8.
[^38]: P.Mercier, D.Daly, and A.Chandrakasan, ''An energy-efficient all-digital uwb  transmitter employing dual capacitively-coupled pulse-shaping drivers,''  Solid-State Circuits, IEEE Journal of, vol.44, no.6, pp. 1679  --1688, june 2009.
[^39]: L.Moreira, W.van Noije, D.Silveira, S.Kofuji, and C.Sassaki, ''A small  area 2.8pj/pulse 7th derivative gaussian pulse generator for ir-uwb,'' in  Microwave Conference Proceedings (CJMW), 2011 China-Japan Joint, april  2011, pp. 1 --4.
[^40]: S.Bourdel, Y.Bachelet, J.Gaubert, M.Battista, M.Egels, and N.Dehaese,  ''Low-cost cmos pulse generator for uwb systems,'' Electronics  Letters, vol.43, no.25, pp. 1425 --1427, 6 2007.
[^41]: T.-A. Phan, J.Lee, V.Krizhanovskii, S.-K. Han, and S.-G. Lee, ''A 18-pj/pulse  ook cmos transmitter for multiband uwb impulse radio,'' Microwave and  Wireless Components Letters, IEEE, vol.17, no.9, pp. 688 --690, sept.  2007.
[^42]: W.Geyi, ''Physical limitations of antenna,'' Antennas and Propagation,  IEEE Transactions on, vol.51, no.8, pp. 2116 -- 2123, aug. 2003.
[^43]: C.-Y. Huang and W.-C. Hsia, ''Planar elliptical antenna for ultra-wideband  communications,'' Electronics Letters, vol.41, no.6, pp. 296 -- 297,  march 2005.
[^44]: C.Carbonelli and U.Mengali, ''Synchronization algorithms for uwb signals,''  Communications, IEEE Transactions on, vol.54, no.2, pp. 329 -- 338,  feb. 2006.
[^45]: M.Kurchuk and Y.Tsividis, ''Energy-efficient asynchronous delay element with  wide controllability,'' in Circuits and Systems (ISCAS), Proceedings of  2010 IEEE International Symposium on, 30 2010-june 2 2010, pp. 3837 --3840.
[^46]: D.Wentzloff and A.Chandrakasan, ''A 47pj/pulse 3.1-to-5ghz all-digital uwb  transmitter in 90nm cmos,'' in Solid-State Circuits Conference, 2007.  ISSCC 2007. Digest of Technical Papers. IEEE International, feb. 2007, pp.  118 --591.
[^47]: B.Qin, H.Chen, X.Wang, A.Wang, Y.Hao, L.Yang, and B.Zhao, ''A  single-chip 33pj/pulse 5th-derivative gaussian based ir-uwb transmitter in  0.13 $\mu$m cmos,'' in Circuits and Systems, 2009. ISCAS 2009. IEEE  International Symposium on, may 2009, pp. 401 --404.
[^48]: H.Miranda and T.Meng, ''A programmable pulse uwb transmitter with 34% energy  efficiency for multichannel neuro-recording systems,'' in Custom  Integrated Circuits Conference (CICC), 2010 IEEE, sept. 2010, pp. 1 --4.
