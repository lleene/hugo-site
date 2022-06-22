---
title: "About"
date: 2022-05-21T19:52:54+02:00
draft: false
tags:
  - personal
  - introduction
  - about
---

This site shares a bit of informal documentation and blog-based record keeping
reflecting my day to day activities. Hopefully it's a good mix of technical and
just-for-fun discussion. Professionally I am a mixed-signal circuit designer
which means I compose integrated circuits mostly for sensors whose signals are
then processed for interesting features. Besides my day-to-day job that I enjoy
a bit of casual programming as a hobby which is now predominantly based on
python which makes it easy to adapt or share code.

Currently my casualy programming projects are mainly oriented towards image
processing for object recognition and vectorization techniques. Basically
I am trying to approximate a rasterized images using absolute geometries and
polynomial color contours such that they have infinite or vector-based precision.
Surprisingly the hardest part here has been detecting and extracting the
underlying line-art and resolving contours.

Besides that I try to self-host the web-services I used as much as possible
both as an educational oppertunity with the added benifit that I can enjoy more
privacy than the average person. While it is a bit of effort, I feel that this
is an important part of software freedom and lets me avoid malicious services
that I would otherwise be subject to.

# Research Interests

I have a strong appreciation for sensing systems and exploring the
More-Than-More scaling for CMOS technology. The idea here is to augment
traditional fabrication techniques for sensing bio-markers, particles, light
and all kinds signals using electronics. More generally however I study analogue
signal processing techniques in the context of all-digital systems. My main
research interests currently are time-domain processing and asynchronous custom
digital logic for high performance applications such as ultra-low-power medical
devices and ultra-wide-band radio transceivers. In these systems we can encode
information using the relative timing of clock edges e.g. pulse-width-modulation
to do analogue processing using digital logic which leads to a new approach to
realizing certain functions and implementations.

### Time-Domain-Processing

There are always some suprising consistencies when re-imagining the
representation of information. For example in time-domain systems we can realize
resolve units of time with almost arbirtary precision, very often down to a
KT/C equivilent limit. Howver some-how similar to traditional analog systems,
where the maximum dynamic range is limited by the voltage-supply, in
time-domain systems this limit comes from rate at which we can make
observations. For example say we have a 1 MHz pulse-width-encoded signal then
we can only resolve relative timing information at 1 MHz. We could increase
our dynamic range by reducing the pulse-repetition-rate but our information
rate stays constant since we only double the information-per-pulse but half
its rate. Comparing this again to traditional analog with a simple RC circuit
where our maximum dynamic is set by the supply voltage to KT/C ratio and this
is fixed irrespective of the resistor or bandwidth of the circuit. Again we can
show that this is a fundamental consequence of the
[equi-partition-theorum](https://www.wikipedia.org/equipartition-theorum)
irrespective of how we represent/encode information.

The main advantage of time-domain processing is that we can exhaustively use
digital logic. This is not only highly-adventagious when designing in a
deep sub-nanometer technology since they are geared towards these kind of
circuits but also we dont suffer from performance losses due to device parameter
degredation in the same way a tranditional op-amp might. In fact you can show
that time-domain circuits can realize almost ideal operators for summation,
integration, multiplication, and thier inverses through closed-loop operation.

### Over-Sampling Techniques

Another facinating topic for embedded sensing circuits is the application of
over-sampling techniques. 
