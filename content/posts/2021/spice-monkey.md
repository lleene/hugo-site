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
