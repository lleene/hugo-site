#!/usr/bin/env python3

"""Command line utility for converting a tex source file into a markdown document."""

import sys
import re
from os import path
from pathlib import Path
from typing import List, Tuple, NamedTuple


class Section(NamedTuple):
    """Structured Figure Item."""

    span: Tuple[int, int]
    index: int
    level: int
    name: str
    label: str

    @property
    def markdown(self) -> str:
        """Markdown string for this section."""
        return "#" * self.level + f" {self.index} {self.name}\n\n"


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


class Equation(NamedTuple):
    """Structured Equation Item."""

    span: Tuple[int, int]
    index: int
    expression: str
    label: str

    @property
    def markdown(self) -> str:
        """Markdown string for this equation."""
        return f"$$ {self.expression} $$"


class Table(NamedTuple):
    """Structured Table Item."""

    span: Tuple[int, int]
    index: int
    caption: str
    content: List[List[str]]
    footer: str
    label: str

    @property
    def markdown(self) -> str:
        """Markdown string for this table."""
        tbl_str = f"Table {self.index}: {self.caption}\n"
        for index, line in enumerate(self.content):
            tbl_str += "|" + "|".join(line).replace("\\\\", "") + "|" + "\n"
            if index == 0:
                tbl_str += (
                    "|" + "|".join(["----" for elem in line]) + "|" + "\n"
                )
        tbl_str += self.footer
        return tbl_str


class Citation(NamedTuple):
    """Structured Citation Item."""

    index: int
    name: str
    label: str


class LatexFile:
    def __init__(self, src_file: Path):
        sys_path = path.abspath(src_file)
        src_dir = path.dirname(sys_path)
        src_file = path.basename(sys_path)
        self.tex_src = self.flatten_input("\\input{" + src_file + "}", src_dir)
        self.filter_tex(sys_path.replace(".tex", ".bbl"))

    @classmethod
    def first(cls, list: List[str]) -> str:
        """Fetch the first optional element else return empty string."""
        return list[0] if list else ""

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

    @property
    def sections(self) -> List[Section]:
        """Parse TEX contents for context refereces."""
        sec_list = []
        for index, match in enumerate(
            re.finditer(r"\\(sub)*(section|chapter)(.*)", self.tex_src)
        ):
            sub_string = self.tex_src[match.start() : match.end()]
            label = self.first(re.findall("\\\\label\{(.*)\}", sub_string))
            sub_string = re.sub(
                r"\\(sub)*(section|chapter)",
                "",
                sub_string.replace("\\label{" + label + "}", ""),
            ).strip()
            sec_list.append(
                Section(
                    span=(match.start(), match.end()),
                    index=index + 1,
                    level=len(match.groups()[0] or "") // 3 + 1,
                    name=sub_string[1:-1],
                    label=label,
                )
            )
        return sec_list

    @property
    def equations(self) -> List[Equation]:
        """Parse TEX contents for context refereces."""
        eq_list = []
        for index, (begin, stop) in enumerate(
            zip(
                re.finditer("\\\\begin\{equation\}", self.tex_src),
                re.finditer("\\\\end\{equation\}", self.tex_src),
            )
        ):
            sub_string = self.tex_src[begin.end() : stop.start()]
            label = self.first(re.findall("\\\\label\{(.*)\}", sub_string))
            eq_list.append(
                Equation(
                    span=(begin.start(), stop.end()),
                    index=index + 1,
                    expression=sub_string.replace(
                        "\\label{" + label + "}", ""
                    ).replace("\n", ""),
                    label=label,
                )
            )
        return eq_list

    @property
    def tables(self) -> List[Table]:
        """Parse TEX contents for context refereces."""
        tbl_list = []
        for index, (begin, stop) in enumerate(
            zip(
                re.finditer("\\\\begin\{table\*?\}", self.tex_src),
                re.finditer("\\\\end\{table\*?\}", self.tex_src),
            )
        ):
            sub_string = self.tex_src[begin.end() : stop.start()]
            label = self.first(re.findall("\\\\label\{(.*)\}", sub_string))
            caption = self.first(re.findall("\\\\caption\{(.*)\}", sub_string))
            footer = sub_string[
                re.search("\\\\end\{tabular\}", sub_string).end() :
            ].replace("\n", "")
            sub_string = sub_string[
                re.search("\\\\begin\{tabular\}", sub_string)
                .end() : re.search("\\\\end\{tabular\}", sub_string)
                .start()
            ]
            content = [line.split("&") for line in sub_string.split("\n")[1:]]
            [
                content.pop(row - 1)
                for row in range(len(content), 0, -1)
                if len(content[row - 1]) <= 1
            ]
            tbl_list.append(
                Table(
                    span=(begin.start(), stop.end()),
                    index=index + 1,
                    caption=caption,
                    content=content,
                    footer=footer,
                    label=label,
                )
            )
        return tbl_list

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

    def replace_tables(self) -> None:
        """Dereference and replace all tables with markdown formatting."""
        tbl_list = self.tables
        tbl_list.reverse()
        for table in tbl_list:
            self.tex_src = (
                self.tex_src[: table.span[0]]
                + table.markdown
                + self.tex_src[table.span[1] :]
            )
        for table in tbl_list:
            self.tex_src = re.sub(
                "\\\\ref\{" + table.label + "\}",
                str(table.index),
                self.tex_src,
            )

    def replace_equations(self) -> None:
        """Dereference and replace all equations with markdown formatting."""
        eq_list = self.equations
        eq_list.reverse()
        for equation in eq_list:
            self.tex_src = (
                self.tex_src[: equation.span[0]]
                + equation.markdown
                + self.tex_src[equation.span[1] :]
            )
        for equation in eq_list:
            self.tex_src = re.sub(
                "\\\\ref\{" + equation.label + "\}",
                str(equation.index),
                self.tex_src,
            )

    @classmethod
    def parse_bbl(cls, lines: List[str]) -> List[Citation]:
        """Parse BBL contents for bibtec refereces."""
        return [
            Citation(
                label=re.match("\\\\bibitem{([0-z\.\-_]*)}", entry).groups()[
                    0
                ],
                index=index + 1,
                name=re.sub(
                    "\\\\emph|\\\\BIBentry[A-z]*wordspacing|\\\\bibitem\{([0-z]*)\}|[\{\}\n~]|\\\\url",
                    "",
                    entry,
                ),
            )
            for index, entry in enumerate("".join(lines).split("\n\n")[1:-1])
        ]

    @classmethod
    def md_bbl(cls, src_bbl: List[Citation]) -> str:
        bbl_str = "# References:\n\n"
        src_bbl.sort(key=lambda x: x.index)
        for citation in src_bbl:
            bbl_str += f"[^{citation.index}]: {citation.name}\n"
        return bbl_str

    def replace_sections(self) -> None:
        """Dereference and replace all sections with markdown formatting."""
        sc_list = self.sections
        sc_list.reverse()
        for section in sc_list:
            self.tex_src = (
                self.tex_src[: section.span[0]]
                + section.markdown
                + self.tex_src[section.span[1] :]
            )
        for sc in sc_list:
            self.tex_src = re.sub(
                "\\\\ref\{" + sc.label + "\}", str(sc.index), self.tex_src
            )

    def preprocess(self) -> None:
        """Prep proceedure for customized formatting."""
        custom_rules = [
            (r"\n(\w)*%.*", ""),
            (r"}(\n)*\\label", r"}\\label"),
            (r" %.*", ""),
            (r"\\usection", r"\\section"),
            (r"\\usubsection", r"\\subsection"),
            (r"\\begin{abstract}", r"\\section{Abstract}"),
            (r"\\end{abstract}", r""),
            (r"\\maketitle", r""),
            (r"\\IEEEpeerreviewmaketitle", r""),
            (r"\\bstctlcite{[0-z:]*}", r""),
            (r"\\clearpage", r""),
            (r"\\pagebreak", r""),
            (r"\\\\[ ]*", r""),
            (r"\$\\,\$", r" "),
            (r"\$([0-z\\\.\-\+_,{}%\(\)\/]*)\$", r"\\\\(\g<1>\\\\)"),
            (r"\\flushleft", r""),
            (r"\\begin{flushleft}", r""),
            (r"\\end{flushleft}", r""),
            (r"\\begin{center}", r""),
            (r"\\end{center}", r""),
        ]
        for rule, result in custom_rules:
            self.tex_src = re.sub(rule, result, self.tex_src)

    def postprocess(self) -> None:
        """Clean up proceedure for customized formatting."""
        custom_rules = [
            (r"\\,", r" "),
            (r"~", r" "),
            (r"\\tsqrd", r"²"),
            (r"\\rpi", r"π"),
            (r"\\rmu", r"μ"),
            (r"\\rbeta", r"β"),
            (r"\\ralpha", r"α"),
            (r"\\rDelta", r"Δ"),
            (r"\\rdelta", r"δ"),
            (r"\\rsigma", r"σ"),
            (r"\\rSigma", r"Σ"),
            (r"\\rtau", r"τ"),
            (r"\\reta", r"η"),
            (r"\\rphi", r"φ"),
            (r"\\rPhi", r"Φ"),
            (r"\\romeg", r"ω"),
            (r"\\rOmeg", r"Ω"),
            (r"\\vspace\{[0-z \.\-\+]*\}", r""),
            (r"\\hspace\{[0-z \.\-\+]*\}", r""),
            (r"\\vfill", r""),
            (r"\\hfill", r""),
            (r" \\& ", r" & "),
            (r"\$\\pm\$", "±"),
            (r"\\tss\{([0-z,_\. ]*)\}", r"<sub>\g<1><sub>"),
            (r"\\tps\{([0-z,_\. ]*)\}", r"<sup>\g<1><sup>"),
            (r"\\textbf\{([0-z\.,_ ]*)\}", r"**\g<1>**"),
            (r"\\sqrt", r"√"),
            (r"\\%", "%"),
        ]
        for rule, result in custom_rules:
            self.tex_src = re.sub(rule, result, self.tex_src)

    @classmethod
    def flatten_input(cls, tex_src: str, basedir: Path = Path(".")) -> str:
        """Recusive method for generating a flattened latex source."""
        for source_file in re.findall("input\{([0-z\/\.\_\-]*)\}", tex_src):
            tex_input = list()
            with open(
                path.join(basedir, source_file), "r", encoding="utf8"
            ) as input:
                for line in input.readlines():
                    tex_input.append(
                        line
                        if not re.findall("input\{([0-z\/\.\_\-]*)\}", line)
                        else cls.flatten_input(line, basedir=basedir)
                    )
            tex_src = tex_src.replace(
                "\\input{" + source_file + "}", "".join(tex_input)
            )
        return tex_src

    def replace_references(self, bbl_file: Path) -> None:
        with open(bbl_file, "r") as file:
            bbl_list = self.parse_bbl(file.readlines())
            bbl_list.sort(key=lambda x: x.label)
            bbl_list.reverse()
            for bbl in bbl_list:
                self.tex_src = re.sub(
                    "\\\\cite{([0-z,\.\-_]*)("
                    + bbl.label
                    + ")([0-z,\.\-_]*)}",
                    f"[^{bbl.index}]" + "\\\\cite{\g<1>\g<3>}",
                    self.tex_src,
                )
            self.tex_src = re.sub(
                r"\\bibliographystyle\{[0-z,\-_\/\.]*\}", "", self.tex_src
            )
            self.tex_src = re.sub(
                r"\\bibliography\{[0-z,\-_\.\/]*\}",
                self.md_bbl(bbl_list),
                self.tex_src,
            )
            self.tex_src = re.sub(r"\\cite{[,]*}", "", self.tex_src)

    def strip_tex(self) -> None:
        """Clear default TEX preable - postamble."""
        begin = re.search(r"\\begin\{document\}", self.tex_src).end()
        end = re.search(r"\\end\{document\}", self.tex_src).start()
        self.tex_src = self.tex_src[begin:end]

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


for file in sys.argv[1:]:
    print(LatexFile(file).tex_src)

# eof
