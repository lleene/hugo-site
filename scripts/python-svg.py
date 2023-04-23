#!/usr/bin/env python3

import sys
import re
import railroad

style = (
    "\tsvg.railroad-diagram {\n\t\tbackground-color:none;\n\t}\n"
    + "\tsvg.railroad-diagram path {\n\t\tstroke-width:1.5;\n\t\tstroke:white;\n\t\tfill:rgba(0,0,0,0);\n\t}\n"
    + "\tsvg.railroad-diagram text {\n\t\tfont:bold 14px monospace;\n\t\tfill: white;\n\t\ttext-anchor:middle;\n\t}\n"
    + "\tsvg.railroad-diagram text.label{\n\t\ttext-anchor:start;\n\t}\n"
    + "\tsvg.railroad-diagram text.comment{\n\t\tfont:italic 12px monospace;\n\t}\n"
    + "\tsvg.railroad-diagram rect{\n\t\tstroke-width:1.5;\n\t\tstroke:white;\n\t\tfill:none;\n\t}\n"
    + "\tsvg.railroad-diagram rect.group-box {\n\t\tstroke: gray;\n\t\tstroke-dasharray: 10 5;\n\t\tfill: none;\n\t}\n"
)

for md_src in sys.argv[1:]:
    with open(md_src, "r") as file:
        md_src = file.read()
        for start, end in zip(
            re.finditer(r"{{< python-svg ", md_src),
            re.finditer(r"{{< /python-svg ", md_src),
        ):
            sub_str = md_src[start.start() : end.start()].split("\n")
            [
                print(elem)
                for elem in re.findall(
                    r"([0-z]+=\"[0-z\.\/\-\_\s]+\")+", sub_str[0]
                )
            ]
            print(sub_str[0])
            print(sub_str[1:-1])

# eof
