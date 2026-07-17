#!/usr/bin/env python3

from pathlib import Path
import re


def convert_file(txt_file):

    lines = txt_file.read_text().splitlines()

    md = []

    md.append(f"# {txt_file.stem}")
    md.append("")

    in_code = False
    code_lines = []


    def flush_code():

        nonlocal code_lines

        if code_lines:

            md.append("")
            md.append("    ```code")

            for line in code_lines:
                md.append(f"    {line}")

            md.append("    ```")
            md.append("")

            code_lines = []



    for line in lines:

        line = line.rstrip()


        if line == "CODE:":

            in_code = True
            code_lines = []
            continue


        if line == "ENDCODE":

            flush_code()
            in_code = False
            continue



        if in_code:

            code_lines.append(line)
            continue



        if line.startswith("# ") and not line.startswith("##"):

            md.append(
                f'??? note "{line[2:]}"'
            )
            md.append("")



        elif line.startswith("## "):

            md.append(
                f"    **{line[3:]}**"
            )
            md.append("")



        elif line.startswith("### "):

            md.append(
                f"    **{line[4:]}**"
            )
            md.append("")



        elif re.match(r"https?://", line):

            md.append(
                f"    [{line}]({line})"
            )
            md.append("")



        elif line == "":

            md.append("")



        else:

            md.append(
                f"    {line}"
            )



    flush_code()


    output = txt_file.with_suffix(".md")

    output.write_text(
        "\n".join(md)
    )

    print(f"Created {output.name}")



for txt in Path(".").glob("*.txt"):

    convert_file(txt)
