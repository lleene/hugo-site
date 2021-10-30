---
title: "Calibre Physical Verification Hacks 🐛🐛"
date: 2021-09-14T11:30:11+02:00
draft: false
toc: true
tags:
  - calibre
  - config
  - verification
---

This page details a variety of 'modifications' to the standard Calibre
verification flow I have used in the past to either modify the checks performed
tools in the physical verification flow. None of which are particularly clean
since they depart from what is usually an approved rule deck / verification
flow. Designs do need to pass the verification process in a meaningful way at
the end of the day so your mileage may vary.

## Extended Device Checks

It is generally good practice to be able to check for internal design
conventions when it comes to layout. Making a custom set of rules that does
exactly this is highly advised to yield better quality designs. For example
it could be required that varactor or mosfet primitives should never have
overlapping shapes with other devices of the same type. The rule below
will check for exactly this and report it as a "NVA0.VAR_OVLP" violation.

```tvf
NVA0.VAR_OVLP { @ Varactors / Tiles should not overlap
    VARi AND > 1
}
```

There are other rules that are required or suggested by the DRM that simply
don't have a good DRC rule. For example requiring tear-shaped geometries on
the RDL layer near flip-chip balls. Getting an approximate rule check that
catches the more obvious issues is worthwhile including.

```tvf
NVA0.RDL.TEAR { @  Shape of RDL near pad: tear shape required
  X0 = EXT RDL <1 ABUT <125 INTERSECTING ONLY REGION
  X1 = EXT RDL <1 ABUT <180 INTERSECTING ONLY REGION
  X2 = INT RDL <1 ABUT <180 INTERSECTING ONLY REGION
  X3 = EXPAND EDGE (X1 NOT TOUCH INSIDE EDGE X0) BY 1 EXTEND BY 50
  X4 = EXPAND EDGE (X2 NOT TOUCH INSIDE EDGE X0) BY 1 EXTEND BY 50
  (X3 AND X0) OR (X4 AND X0)
}
```

The above rule finds regions with acute angles (internal and external)
near regions with obtuse angles where the latter is generally the rounded
RDL landing pad for the ball.

## Layer / Device Aliasing

Layer aliasing or remapping is another way to add indirection to the DRC rule
deck that will allow you to both run your own checks and device recognition
without interfering with the standard flow.

```tvf
LAYER MAP 107 DATATYPE 0 746
```

In the above scenario we allocated an additional layer in the Cadence design
to designate inductor recognition beside the standard inductors. This was
required since the standard inductors also implied metallization free regions
which is not always be acceptable. By adding this layer and mapping it to
the same inductor recognition data type during LVS these inductors would still
be recognized but did not trigger the associated metallization rules during DRC.

## Adding New Device Primitives

Another good know how is the process behind device recognition when you run
the Calibre LVS process. The code snippets below take us through a process of
defining a new device for LVS recognition that is bound together with a spice
definition to produce the extracted netlist. This should allow you to define
custom layers and define custom devices on those layers while still getting
LVS clean at the end of the day. This example will define a custom resistor.

```tvf
LAYER RESLYR          450
LAYER MAP 215 DATATYPE 21 450 //  layer to form memresistor
XTERM = RESLYR AND M4
XCDTR = RESLYR NOT M4
CONNECT metal4 MEMRESLYRT
DEVICE XDEVICE XCDTR XTERM(PORT1) XTERM(PORT2) netlist model xdevice
```

The section of code above are LVS rule statements that first define a named
layer `RESLYR` and then map a data type onto that layer. The data type should
correspond to what ever you new layer you used to define the device in the
layout editor. Then we define the terminals of this device when ever this layer
overlaps and connects with metal 4 otherwise it is the resistive section.
Finally you specify a device in terms of the relevant layers and how they map
to the actual model.

Notice the device maps to a netlist model called `xdevice` with named ports.
This model is defined below. Note that we haven´t extracted any parameters
but this could be done in the rule deck definition. Also note that here
we also specify the mapping of this `xdevice` to a cell in the design library.

```lisp
(xdevice
  (DEVICE_LIB DEVICE_CELL DEVICE_VIEW)
  (
    (PORT1 PIN1)
    (PORT2 PIN2)
  )
  (
    (nil multi 1)
    (nil m 1)
  )
)
```

Finally a spice definition must also be included in order to run the netlist
comparison. Assuming the cell in the design library correctly netlists with a
auCDL view. The spice definition below presumes both the layout and schematic
perform black-boxed comparison of this new resistor.

```spice
.SUBCKT xdevice PORT1 PORT2
.ENDS
```

## Extending Connectivity Layers

In some occasions it could be that certain extra layers are defined in the DRC
deck but not in the LVS deck. For example there are optional metallization
layers for your process. Adding connectivity is rather strait forward.
The main challenge here is to choose the correct data type mappings as to
avoid conflicts with the original rule statements.

```tvf
LAYER PM1i 5001
LAYER MAP 5 DATATYPE 1 5001
LAYER Cu_PPIi 7410
LAYER MAP 74 DATATYPE 10 7410
LAYER UBM 170
LAYER MAP 170 DATATYPE 0 170
LAYER PM2i 5002
LAYER MAP 5 DATATYPE 2 5002
VIA8 = COPY CB2
metal9 = COPY Cu_PPIi
VIA9 = COPY PM2i
metal10 = COPY UBM
```

Once these layers are defined we can go ahead and specify the order of
connectivity. Notice that we can´t directly operate / manipulate layer
definitions so simply running a `COPY` statement resolves this. Below we
see also that adding ports and text labels connectivity for the relevant
layers is also needed for your pins to connect.

``` tvf
CONNECT metal9 metal8 BY VIA8
CONNECT metal10 metal9 BY VIA9
TEXT LAYER 140 ATTACH 140 metal9
PORT LAYER TEXT 140
TEXT LAYER 141 ATTACH 141 metal10
PORT LAYER TEXT 141
TEXT LAYER 125 ATTACH 125 metal10
PORT LAYER TEXT 125
```

## Hot fixing LVS comparison

Finally the rule statements below are global deck adjustments. They are
for the most part self explanatory except for `CULL` which actually
removes empty spice sub-circuits that are identified by a hierarchical LVS run
but does not actually contain active devices (i.e. a dummy digital filler cell).

```tvf
LVS SPICE CULL PRIMITIVE SUBCIRCUITS YES
VIRTUAL CONNECT NAME "POWER"
TEXT "NET_NAME" LOCX LOCY DATATYPE
LAYOUT RENAME TEXT "/DATA\\[(.*)\\]/DATA<-1>/M-"
```
