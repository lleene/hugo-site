---
title: "Calibre Physical Verification Hacks"
date: 2021-09-14T11:30:11+02:00
draft: false
toc: true
tags:
  - calibre
  - config
  - verification
---

This is a list of 'modifications' to the standard Calibre verification flow I
have used in the past to either modify the checks performed by Calibre or input
data bases.

# DRC

## Extended Device Checks

```tvf
NVA0.VAR_OVLP { @ Varactors / Tiles should not overlap
    VARi AND > 1
}
```

```tvf
NVA1.Cu_PPI.TEAR { @  Shape of Cu_PP I pad (under PM2 area): tear shape required
  X0 = EXT Cu_PPIi <1 ABUT <125 INTERSECTING ONLY REGION
  X1 = EXT Cu_PPIi <1 ABUT <180 INTERSECTING ONLY REGION
  X2 = INT Cu_PPIi <1 ABUT <180 INTERSECTING ONLY REGION
  X3 = EXPAND EDGE (X1 NOT TOUCH INSIDE EDGE X0) BY 1 EXTEND BY 50
  X4 = EXPAND EDGE (X2 NOT TOUCH INSIDE EDGE X0) BY 1 EXTEND BY 50
  (X3 AND X0) OR (X4 AND X0)
}
```


## Layer / Device Aliasing

```tvf
LAYER MAP 107 DATATYPE 0 746
```

# LVS

## Adding New Device Primitives

```tvf
LAYER RESLYR          450
LAYER MAP 215 DATATYPE 21 450 //  layer to form memresistor
XTERM = RESLYR AND M4
XCDTR = RESLYR NOT M4
CONNECT metal4 MEMRESLYRT
DEVICE XDEVICE XCDTR XTERM(PORT1) XTERM(PORT2) netlist model xdevice
```

```spice
.SUBCKT xdevice PORT1 PORT2
.ENDS
```

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

## Extending Connectivity Layers

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

```tvf
LVS SPICE CULL PRIMITIVE SUBCIRCUITS YES
VIRTUAL CONNECT NAME "POWER"
TEXT "POWER" LOCX LOCY DATATYPE
LAYOUT RENAME TEXT "/DATA\\[(.*)\\]/DATA<-1>/M-"
```



# SPICE

## Port Order Reshuffling

```bash
function getSortedOrder() {
  local SOURCE=""
  local SORTED=""
  read -a SOURCE <<< "$1"
  SORTED="${SOURCE[@]}"
  if [ -z "${SORTED//*\[*}" ] ; then
    SORTED=($(echo "${SOURCE[@]:2}" | tr " " "\n" | sed -r "s/\[([0-9]+)\]/ \1 /g" \
            | sort -k 1,1 -k2,2nr | sed -r "s/ ([0-9]+) /\[\1\]/g" ))
  else
    SORTED=($(echo "${SOURCE[@]:2}" | tr " " "\n" | sed -r "s/<([0-9]+)>/ \1 /g" \
            | sort -k 1,1 -k2,2nr | sed -r "s/ ([0-9]+) /<\1>/g" ))
  fi
  echo "${SOURCE[@]:0:2} ${SORTED[@]}"
}
function updatePortOrder() {
  local TARGET="$1"
  local CDL_FILE="$2"
  local PORTORDER="$(awk -v target="subckt ${TARGET} " -f "catch.awk" "$CDL_FILE")"
  local PORTREF=$(getSortedOrder "$PORTORDER")
  local SWPDELIMITER=""
  echo $TARGET
  if [ -z "${PORTREF//*\[*}" ] ; then SWPDELIMITER="TRUE" ; fi
  awk -v target="subckt ${TARGET} " -v release="$PORTREF" -v swpdelim="$SWPDELIMITER" \
      -f "release.awk" "$CDL_FILE" > "${TARGET}.cdl"
  [ ! -z "$(grep -m 1 "\[" "${TARGET}.cdl")" ] && [ ! -z "$(grep -m 1 "<" "${TARGET}.cdl")" ] \
      && echo "Error $CDL_FILE uses mixed delimiters"
}
```

```awk
BEGIN{ hold = ""; IGNORECASE = 1 }
NF {
    if( $1 == "+" && hold != "")
      { for(i=2;i<=NF;i++) hold=hold " " $i }
    else if( hold != "") { print hold; hold=""; exit }
  };
$0 ~ target { hold = $0 };
```

```awk
BEGIN{output="";hold="";IGNORECASE=1};
NF{if($1!="+")hold=""}
$0~target{
  hold=$0
  n=split(release,ports," ")
  for(i=n;i>0;i--){
    if(swpdelim!=""){
      gsub("<","[",ports[i])
      gsub(">","]",ports[i])}
    output=ports[i]" "output}
  print output}
NF{if(hold=="")print $0}
```
