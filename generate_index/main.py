#!/usr/bin/env python3

from publications import publications

publications_src = (
    "<table>"
    + "\n".join(publication.to_html_table() for publication in publications)
    + "</table>"
)

publications_src = "\n".join(
    publication.to_html_simple(one_line=False, long_venue=False)
    for publication in publications
)


def probably_comment(line):
    s = line.strip()
    return s.startswith("<!--") and line.strip().endswith("-->")


with open("template.html") as f:
    doc = "".join([l for l in f.readlines() if not probably_comment(l)])
    doc = doc.replace("PUBLICATIONS", publications_src)
    print(doc)
