---
title: "Spice Monkey 💻🐒"
date: 2021-10-29T18:54:32+02:00
draft: false
toc: false
images:
tags:
    - spice
    - code
    - verification
---

Netlisting issues can be some of the more frustrating aspects of circuit design
tool chains primarily because its it all text based and very old fashioned.
The Cadence tools for example have various command-line utilities but
documentation is underwhelming to say the least. Quite often though they are
inevitable when combining different tools, design flows, or handling someone
else's IP. In order to cope with the usual inconsistencies I rely on the
scripts below to pre and post process SPICE netlists.

### Port Order Reshuffling

The default netlister and spice simulators usually connects sub component
terminals in terms of the order in which they are defined in the spice `.SUBCKT`
definition. Conflict arises however since IP vendors on the other hand tend
to sort the port order in someway in the spice netlist but the Cadence
symbol/schematic definition will usually disregard this order causing
connectivity issues later.

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
```

Cadence tools will prefer alphabetical ordering. The bash script above will
replicate this sorting behaviour if you pass it a `.SUBCKT` definition string.
The purpose here is that when you are given a netlist from a vendor you can
prepare an internal version that already sorts the ports alphabetically.

In order to do this in terms of editing a file however you can use the script
below which is called as: `updatePortOrder $CKT_NAME $FILE_NAME`. This will
look for the definition given a `CKT_NAME` in the spice file and create a
new file `CKT_NAME.cdl` in the current directory.

```bash
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

The second script however relies on some awk-based spice parsing calls to
properly find and replace the relevant sections in the netlist. `catch.awk`
simple finds the `SUBCKT` statement relevant and prints it to stdout.

```awk
BEGIN{ hold = ""; IGNORECASE = 1 }
NF {
    if( $1 == "+" && hold != "")
      { for(i=2;i<=NF;i++) hold=hold " " $i }
    else if( hold != "") { print hold; hold=""; exit }
  };
$0 ~ target { hold = $0 };
```

Then `release.awk` helps to insert the definition back into the netlist with
the option to swap out any delimiters in the port names.

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

### Netlisting Environment:

```skill
;; spice.env
simStopList = '("auCdl")
simViewList = '("auCdl" "schematic")
auCdlDefNetlistProc = "ansCdlSubcktCall"
globalGndSig = ""
globalPowerSig = ""
shrinkFACTOR = 0
checkScale = "meter"
preserveDIO = 'nil
checkDIOAREA = 'nil
checkDIOPERI = 'nil
preserveCAP = 'nil
checkCAPVAL = 'nil
checkCAPAREA = 'nil
checkCAPPERI = 'nil
preserveRES = 'nil
checkRESVAL = 'nil
checkRESSIZE ='nil
resistorModel = ""
shortRES = 2000
simNetlistHier = 't
pinMAP = 'nil
displayPININFO = 't
checkLDD = 'nil
connects = ""
setEQUIV = ""
cdlSimViewList = '("auCdl" "schematic")
cdlSimStopList = '("auCdl")
simSimulator = "auCdl"
simRunDir = "$RUN_DIR"
hnlNetlistFileName = "$CELL.src.net"
simViewName = "$SCH_VIEW"
simCellName = "$CELL"
simLibName = "$LIBRARY"
incFILE = "$RUN_DIR/source.added"
auCdlNoForwardSlash = t
```

```skill
;; simrc
hnlSetBusDirectionDescending = 't
simVerilogGenerateSingleNetlistFile = 't
hnlVerilogPrintSpecparam = nil
simVerilogNetlistExplicit = 't
simPrintInhConnAttributes = t
hnlInhConnUseDefSigName = t
```

```skill
;; verilog.env
simLibName = "$LIBRARY"
simCellName = "$CELL"
simViewName = "$SCH_VIEW"
simSimulator = "verilog"
simNotIncremental = nil
simReNetlistAll = 't
simNetlistHier = t
simVerilogLaiLmsiNetlisting = 'nil
verilogSimViewList = '("behavioral" "functional" "system" "verilog" "schematic" "symbol")
simVerilogAutoNetlisting = 't
simVerilogTestFixtureFlag = 't
simVerilogTestFixtureTemplate = "All"
simVerilogNetlistExplicit = 't
hnlVerilogTermSyncUp = "mergeAll"
simVerilogFlattenBuses = 'nil
vtoolsUseUpperCaseFlag = 'nil
hnlVerilogCreatePM = 'nil
simVerilogTopLevelModuleName = "verilog_$CELL.top"
simHierarchyPrefix = "verilog_$CELL.top"
simNCVerilogHierPrefix = "verilog_$CELL:top"
verilogSimStopList = '("verilog" "symbol")
simVerilogPwrNetList = '("$PWRLIST")
simVerilogGndNetList = '("$GNDLIST")
vtoolsifForceReNetlisting = 'nil
simVerilogLibNames = '("$LIBLIST")
vlogifInternalTestFixtureFlag = 'nil
simVerilogBusJustificationStr = "U"
simVerilogTestFixtureTemplate = "All"
simVerilogDropPortRange = 't
simVerilogHandleUseLib = 'nil
simVerilogHandleAliasPort = 't
simVerilogPrintStimulusNameMappingTable = 'nil
simVerilogProcessNullPorts = 'nil
simVerilogIncrementalNetlistConfigList = 'nil
hnlVerilogNetlistStopCellImplicit = 'nil
simVerilogOverWriteSchTimeScale = 'nil
vlogifCompatibilityMode = "4.2"
simVerilogHandleSwitchRCData = 'nil
vlogifUseAssignsForAlias = 't
vlogifDeclareGlobalNetLocal = 'nil
vlogifSkipTimingInfo = 'nil
simVerilogEnableEscapeNameMapping = 'nil
simVerilogStopAfterCompilation = 't
simVerilogVhdlImport = 'nil
simVerilogTopCellCounter = 0
hnlSupportIterInst = 't
hnlNetlistFileName = "$CELL.v"
hnlSetBusDirectionDescending = 't
simVerilogGenerateSingleNetlistFile = 't
hnlVerilogPrintSpecparam = 'nil
simPrintInhConnAttributes = 't
hnlInhConnUseDefSigName = 't
```

### Property Based Removal

```
hnlHonorLxRemoveDevice = 't
hnlUserShortCVList = list( list("analogLib" "res") list("tsmcN40" "rnpolywo")  )
```
