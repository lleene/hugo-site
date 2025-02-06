---
title: "Single-Bit Heuristics"
date: 2025-01-13T12:31:02+01:00
draft: true 
toc: false
images:
tags: 
  - signal-processing
  - digital-circuits
  - python
---





``` goat
                                   
              .                                 
        .-.   |\                 .-.      
Vin -->| Σ +--+⨍+------*------->| Σ +-->  Digitized Sequence
        '-'   |/       |         '-'  
         ^-   '        v          ^   
         |         .--------.     |   
         |         |  H(z)  |     |   
         |         '---+----'     |   
         |             |          |   
          '------------*---------'    
                   
```