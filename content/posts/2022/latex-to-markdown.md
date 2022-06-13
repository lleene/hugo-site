---
title: "Latex to Markdown"
date: 2022-04-28T13:42:40+02:00
draft: false
tags:
  - markdown
  - latex
  - code
  - python
  - hugo
---

Recently I started porting some of my latex articles to markdown as they would
make a fine contribution to this website in simpler format. Making a simple
parser python isn't that bad and I could have used [Pandoc](https://pandoc.org/index.html)
but I wanted a particular format for rendering a hugo markdown page. So I
prepared several regex-based functions in python to dereference and construct
a hugo-compatible markdown file.

``` python3
class LatexFile:
    def __init__(self, src_file: Path):
        sys_path = path.abspath(src_file)
        src_dir = path.dirname(sys_path)
        src_file = path.basename(sys_path)
        self.tex_src = self.flatten_input("\\input{" + src_file + "}", src_dir)
        self.filter_tex(sys_path.replace(".tex", ".bbl"))

    def filter_tex(self, bbl_file: Path) -> None:
        """Default TEX filterting proceedure."""
        self.strip_tex()
        self.preprocess()
        self.replace_references(bbl_file)
        self.replace_figures()
        self.replace_tables()
        self.replace_equations()
        self.replace_sections()
        self.postprocess()
```

The general process for converting a Latex document is outlined above. The
principle here is to create a flat text source which we then incrementally
format such that Latex components are translated correctly.


## Latex Components

In order to structure the python code I created several named-tuples for
self-contained Latex contexts such as figures, tables, equations, etc. then
by adding a `markdown` property we can replace these sections with hugo
friendly syntax using short-codes where appropriate.

``` python3
class Figure(NamedTuple):
    """Structured Figure Item."""

    span: Tuple[int, int]
    index: int
    files: List[str]
    caption: str
    label: str

    @property
    def markdown(self) -> str:
        """Markdown string for this figure."""
        fig_str = ""
        for file in self.files[:-1]:
            fig_str += "{{" + f'< figure src="{file}" width="500" >' + "}}\n"
        fig_str += (
            "{{"
            + f'< figure src="{self.files[-1] if self.files else ""}" title="Figure {self.index}: {self.caption}" width="500" >'
            + "}}\n"
        )
        return fig_str
```
