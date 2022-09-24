---
title: "Home Automation with LED Lighting"
date: 2022-09-23T10:58:11+02:00
draft: false
toc: false
images:
tags:
  - electronics
  - lighting
  - DIY
---

As a small side project I am installing LED lighting in on of the rooms at my
place. There are quite a few interesting details that is worth taking note on.

## Hardware Preparation

Before buying the bulk of my hardware I ordered a smaller quantity to
assess build quality and see how it all fits together. All components discussed
below are ordered from aliexpress while the AC-DC power-supply will be purchased
locally for safety and certification reasons.

### 12 V and 24 V LED Strips

LED strips are advertised at different voltages but generally all operate the
same way by stringing sets of LEDs in series and then having multiple sections
in parallel. The voltage specification will limit the number of LED you can
put in series due to the voltage requirement on each device which means that
12 V strips will use smaller groupings and yield 10 to 20 cm cuts. Strictly
speaking device or power density will be independent of the operating voltage.

The efficiency for either voltage is comparable but the 24V configuration will
do slightly better by sharing the current limiting resistor over more LEDs.

``` goat
                 12V / 24V SUPPLY                                                 
                 -------*------*------*------*------*---->                        
                        |      |      |      |      |                             
                      +-+-+  +-+-+  +-+-+  +-+-+  +-+-+                           
                 LED   \ /    \ /    \ /    \ /    \ /   3V Drop                  
                      --+--  --+--  --+--  --+--  --+--                           
                        |      |      |      |      |                             
                        |      |      |      |      |                             
                      +-+-+  +-+-+  +-+-+  +-+-+  +-+-+                           
                 LED   \ /    \ /    \ /    \ /    \ /   3V Drop                  
                      --+--  --+--  --+--  --+--  --+--                           
                        |      |      |      |      |                             
                        |      |      |      |      |                             
                      +-+-+  +-+-+  +-+-+  +-+-+  +-+-+                           
                 LED   \ /    \ /    \ /    \ /    \ /   3V Drop                  
                      --+--  --+--  --+--  --+--  --+--                           
                        |      |      |      |      |                             
                      +-+    +-+    +-+    +-+    +-+                             
                       \      \      \      \      \                              
            LIMITING  +-+    +-+    +-+    +-+    +-+    0V to 3V                 
            RESISTOR   \      \      \      \      \     Drop                     
                      +-+    +-+    +-+    +-+    +-+                             
                       \      \      \      \      \                              
                        +      +      +      +      +                             
                        |      |      |      |      |                             
                <-------*------*------*------*------*-----                        
                 Lighting Control Signal                                          
```

### Individually Addressable LED Strips

Some of the advertised LED strips come with integrated controllers where
brightness levels can be adjusted for each section. The advantage is that
this allows you to animate the lighting or create intricate patterns along
the LED strip. Note that the failure of a single controller
will cause the entire strip to fail rather than just one section of LED lights.
Another detail is different integrated don't all provide equivalent lighting.
A RGB LED for example emits with a luminosity of 600, 1250, and 300 mcd
while a dedicated white-channel LED emits around 4000 mcd or around 12 lumens.
Specification wise SK6812 RGBW does seem like a good choice here especially
since the estimated power requirement is 9 Watt per meter.

The main caveat however is that controllers can require a quite a bit more
effort to operate with the added functionality. Given the Chinese quality
standards a home-brew ESP32-H2 solution would be preferred. Besides that
the efficiency/performance seems very similar to that of non-individually
addressable solutions looking mostly at Watt per meter figures.

### Prototyping hardware

The LED controller from GLEDOPTO cost me $19.99 USD and provides
6 channel (RGB+CW) lighting with maximum capacity of 270 W. The 6 channel
LED strip similarly cost me $22.00 USD for 5 meter of lighting.
This strip uses 21 Watt per meter which means the controller could drive 11
meter of lighting. Here are some more details for the LED strip:

|LED Strip     |Specification           |
|--------------|------------------------|
|Model Number  | MF350Z090A80           |
|LED Type      | 5050 RGB               |
|CCT Colour    | 622 nm, 522 nm, 465 nm |
|Beam Angle    | 120 °                  |
|Voltage       | DC 24 V                |
|Current       | 0.83 A/m               |
|Power         | 20.2 W/m               |
|LED Density   | 30 Units/m or 12/cut   |
|Brightness    | 1457 Lumen/m           |    
|PCB Width     | 12 mm                  |
|Cost          | $4.4 USD/m           |

Note that the density here is with respect the density for a single LED channel.
Originally it is quoted at 90 Units/m since there are 3 devices for the 6 channels.
Similarly the brightness is optimistically the sum of each channel together.
The controller is specified below:

|Zigbee controller |Specification         |
|------------------|----------------------|
|Model Number      | GL-C-008             |
|Input Power       | 270 W Max            |
|Input Voltage     | DC 12-24 V           |
|Output Current    | 15 A or 6 A/channel  |
|Dimensions LWH    | 8.0 x 4.8 x 2.4 cm   |
|Recommended Load  | 10 m                 |
|Cost              | $1.99 USD / m        |

The key detail here is that we should match certain lengths with designated
controllers. For example the room I intend to illuminate has a 11 meter
perimeter and I would prefer to use just one controller which implies
I should keep in mind that I can probably only illuminate part of the ceiling.

For preliminary testing I also ordered 10 meter of diffuser that is compatible
with the 6 channel LEDs.

|LED Diffuser     |Specification         |
|-----------------|----------------------|
|Model Number     | T0515                |
|Type             | Minimal enclosure    |
|Dimensions WH    | 1.5 x 0.5 cm         |
|PCB Width        | 12 mm                |
|Cost             | $2.66 USD / m        |

While we have not included the price here for a 24V 10A AC-DC converter required
to power this setup, it is interesting to note the majority of the cost comes
from the LED strip is self. As explained below I probably wouldn't purchase
this particular diffuser again since at least for my application other
lighting configurations seem more useful. I also ordered a bunch of LED utility
items that is compatible with the 6 channel strip including some T-junctions
and L-junctions. These are mainly just for wiring and don't contribute to
lighting but could make the general configuration look a bit more integrated.   

### LED Placement

One issue with LED lighting is that generally we would prefer a contiguous
strip of lighting even around corners but depending on the orientation and
diffusion this may not be possible. It is generally better
to orient the strip facing the corner which means that side-illuminating
diffusions are generally more aesthetically useful. For example when we
want to illuminate the perimeter of the ceiling it is not possible the to
make right-angle turns with contiguous lighting when the LEDs are facing the
floor.

Instead having the strip face this inside of the room with a
downward/sideways diffusing shroud avoids this issue where we need to break up
or fold the lighting which cannot be done readily.

``` goat
      3.6 meters
  .-----------------.
  |   11m OFFICE    | 1.9        
  |   220W / 110W   | meters      
  |   330 units     |          
  +-----------------+---------------+-----------------------.
  |           15m HALL WAY          |                       |
  | 1.5       300W / 150W           |    19m LIVING ROOM    |
  | meters    450 units             |    380W / 190W        |
  |           5.8 meters            |    570 units          | 3.8
  +-----------------+---------------+                       | meters
  |   10m BED ROOM  |               |                       |
  |   200W / 100W   | 2.0           |                       |
  |   300 units     | meters        |                       |
  '-----------------+               '-----------------------'
      3.1 meters                         5.4 meters

  Total Perimeter 55 meters. Power Estimates for 20/10 Watt per meter.
```

The diagram above roughly illustrates some of the rooms I was considering to
light using this LED setup. It is worthwhile to estimate the maximum power
requirement for the mains transformer that is supplying the 24 V DC supply.
I found that I can readily get a good quality 150 Watt AC-DC transformer
for about $50 USD which means for most rooms a lower power configuration would
be preferred.
