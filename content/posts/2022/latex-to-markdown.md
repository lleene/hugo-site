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
but I wanted to keep formatting as simple as possible when rendering a hugo
markdown page. So I prepared several regex-based functions in python to
dereference and construct a hugo-compatible markdown file.

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
principle here is to process a flat text source which we then incrementally
format such that Latex components are translated incrementally and replaced
by plain text with markdown syntax.


## Latex Components

In order to structure the python code I created several named-tuples for
self-contained Latex contexts such as figures, tables, equations, etc. Then
by adding a `markdown` property we can create a collection of objects
where we can simple replace the corresponding latex code in a predictable
manner.

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
            + f'< figure src="{self.files[-1] if self.files else ""}" '
            + f'title="Figure {self.index}: {self.caption}" width="500" >'
            + "}}\n"
        )
        return fig_str
```

Notice that here we use a hugo short-code for when representing the figure in
markdown. This lets us set with and other properties in a simpler and more
systematic way.

## Replacement Procedure

As mentioned before the replacement simply looks for sections in the source and
directly replaces them with appropriate markdown text. In order to do this it
is important to process the source code in reverse order such that the text
location references remain correct as the replacement occurs.

``` python3
def replace_figures(self) -> None:
    """Dereference and replace all figures with markdown formatting."""
    fig_list = self.figures
    fig_list.reverse()
    for figure in fig_list:
        self.tex_src = (
            self.tex_src[: figure.span[0]]
            + figure.markdown
            + self.tex_src[figure.span[1] :]
        )
    for figure in fig_list:
        self.tex_src = re.sub(
            "\\\\ref\{" + figure.label + "\}",
            str(figure.index),
            self.tex_src,
        )
```

Secondly we also replace the latex references with plain text references. This
means that instead of using labels that are translated during compilation into
numbers we directly reference the figure number.

``` python3
@property
def figures(self) -> List[Figure]:
    """Parse TEX contents for context eces."""
    return [
        Figure(
            span=(begin.start(), stop.end()),
            index=index + 1,
            files=[
                elem[1]
                for elem in re.findall(
                    "\\\\includegraphics(.*)\{(.*)\}",
                    self.tex_src[begin.start() : stop.end()],
                )
            ],
            caption=self.first(
                re.findall(
                    "\\\\caption\{(.*)\}",
                    self.tex_src[begin.start() : stop.end()],
                )
            ),
            label=self.first(
                re.findall(
                    "\\\\label\{(.*)\}",
                    self.tex_src[begin.start() : stop.end()],
                )
            ),
        )
        for index, (begin, stop) in enumerate(
            zip(
                re.finditer("\\\\begin\{figure\*?\}", self.tex_src),
                re.finditer("\\\\end\{figure\*?\}", self.tex_src),
            )
        )
    ]
```

The piece of python code above exemplifies how we capture all figures found in
the latex source code and aggregate them in a list of named-tuples. Naturally
this is dependent on the style used when writing latex but I generally try
to keep latex-code a simple and systematic as possible.
