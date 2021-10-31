---
title: "Unified Modelling Language 🐬"
date: 2021-10-30T15:42:47+02:00
draft: false
toc: false
images:
tags:
  - svg
  - uml
  - code
---

## Mermaid CLI

[Mermaid](https://mermaid-js.github.io/mermaid) is a JS based diagram and
charting tool which aspires to generate diagrams in a markdown fashion. The
main advantage here is that Mermaid is well integrated into quite a few
editing and content management
[packages](https://mermaid-js.github.io/mermaid/#/./integrations).
There is command-line node-package that installs on both linux and WSL
environments. You do need NPM version 10+ so installing in
[Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)
takes a few extra steps in order to get the latest version.

```bash
npm install @mermaid-js/mermaid-cli
```

Additionally this
package will sandbox a instance of chromium which doesn't operate correctly
with WLS version 1. Upgrading to WLS version 2 will allow you to run the
following example using `mmdc -i input.mmd -o output.svg -c config.json`.

```text
graph LR
    S[fa:fa-dot] --> A
    A{foo}
    A --> B(bar)
    A --> C(baz)
    style S fill:none, stroke:none
```

This example generates the diagram show below.

![example_mermaid.svg](/images/example_mermaid.svg)

There are four base themes: dark, default, forest, neutral. Additional
[customization](https://mermaid-js.github.io/mermaid/#/theming) is possible.
The `config.json` is shown below which sets similar styling as
[before]({{< relref "building-svg.md" >}} "building svg") using the other
command-line tools.

```json
{
  "theme": "neutral",
  "themeVariables": {
      "fontFamily":"monospace",
      "fontSize":"14px",
      "classText" : "white",
      "nodeBorder" : "white",
      "nodeTextColor" : "white",
      "lineColor" : "white",
      "arrowheadColor" : "white",
      "mainBkg" : "none"
  }
}
```

## UML diagrams

Mermaid is quite a bit more versatile and is geared towards making structured
diagrams of classes and inter-related structures. For example the UML diagram below presents the overall composition of
[pyviewer]({{< relref "pyside.md" >}} "pyside") which is image simple
browsing utility for compressed archives.

![example_pyviewer.svg](/images/example_pyviewer.svg)

This does quite well at illustrating how classes are composed and which methods
are available at various scopes. It also helps organizing and structuring a
code-base when there means to reason in a visual way. The source code for this
diagram is shown below for reference.

```text
classDiagram
     class ApplicationWindow{
          int[2] layout
          int max_count
          navigate(keyPress)
          update()
      }
      class PyViewer{
        signal image_changed
        load_file_map(str path)
        load_archive(int index)
        set_max_count(int max_count)
      }
      class ArchiveLoader{
        generate_map(str path)
        extract_current_index()
        check_media()
      }
      class ArchiveManager{
          int max_count
          Qbyte[] images
          load_archive(str archive_path)
      }
      class TagManager{
          int index
          dict media_map
          dict tag_filter
          list tag_history
          update_filter(str tag, bool state)
          undo_last_filter()
          adjust_index(int change)
          tag_at(int index)
          set_index(str tag_name)
      }
      ArchiveLoader <|-- TagManager
      ArchiveLoader <|-- ArchiveManager
      PyViewer <-- ArchiveLoader
      PyViewer <-- ApplicationWindow
```
