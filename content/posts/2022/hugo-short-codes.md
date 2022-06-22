---
title: "Hugo Short Codes"
date: 2022-06-14T19:36:18+02:00
draft: false
toc: false
tags: 
  - hugo
  - code
---



## Inserting columns

``` go
<div class="flex flex-wrap">
  <div style="width:10em; padding: 1em;">
    <img src="{{ .Get "src" }}"
         {{- if or (.Get "alt") (.Get "caption") }}
         alt="{{ with .Get "alt" }}{{ . }}{{ else }}{{ .Get "caption" | markdownify | plainify }}{{ end }}"
         {{- end -}}
         {{- with .Get "width" }} width="{{ . }}"{{ end -}}
         {{- with .Get "height" }} height="{{ . }}"{{ end -}}
    />
  </div>
  <div class="flex-even markdown-inner">
    {{ .Inner | markdownify }}
  </div>
</div>
```

## Inserting SVG Figures

``` go
<figure{{ with .Get "class" }} class="{{ . }}"{{ end }}>
    {{- if .Get "link" -}}
        <a href="{{ .Get "link" }}"{{ with .Get "target" }} target="{{ . }}"{{ end }}{{ with .Get "rel" }} rel="{{ . }}"{{ end }}>
    {{- end -}}
    {{- if false }} <!-- python src_code {{ .Inner }} --> {{ end -}}
    <img src="{{ .Get "dest" }}"
         {{- if or (.Get "alt") (.Get "caption") }}
         alt="{{ with .Get "alt" }}{{ . }}{{ else }}{{ .Get "caption" | markdownify | plainify }}{{ end }}"
         {{- end -}}
         {{- with .Get "width" }} width="{{ . }}"{{ end -}}
         {{- with .Get "height" }} height="{{ . }}"{{ end -}}
    /><!-- Closing img tag -->
    {{- if .Get "link" }}</a>{{ end -}}
    {{- if or (or (.Get "title") (.Get "caption")) (.Get "attr") -}}
        <figcaption>
            {{ with (.Get "title") -}}
                <h4>{{ . }}</h4>
            {{- end -}}
            {{- if or (.Get "caption") (.Get "attr") -}}<p>
                {{- .Get "caption" | markdownify -}}
                {{- with .Get "attrlink" }}
                    <a href="{{ . }}">
                {{- end -}}
                {{- .Get "attr" | markdownify -}}
                {{- if .Get "attrlink" }}</a>{{ end }}</p>
            {{- end }}
        </figcaption>
    {{- end }}
</figure>
```


``` go
{< python-svg dest="/images/posts/test.svg" title="This is a pyuthon-svg exmaple." >}
railroad.Diagram("foo", railroad.Choice(0, "bar", "baz"), css=style)
{< /python-svg >}
```

{{< python-svg dest="/images/posts/test.svg" title="This is a python-svg exmaple." >}}
railroad.Diagram("foo", railroad.Choice(0, "bar", "baz"), css=style)
{{< /python-svg >}}

