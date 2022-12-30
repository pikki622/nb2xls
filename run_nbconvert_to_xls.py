## Run an example nbconvert through Python directly
# This is to make debugging easier

import nbformat

fn = "./Examples/ExcelTest.ipynb"

with open(fn, "rt") as f:
    jsontext = f.read()

json_nb = nbformat.reads(jsontext, as_version=4)

from nb2xls import XLSExporter

xlsexporter = XLSExporter()

xlsexporter.ignore_markdown_errors = False

body,resources = xlsexporter.from_notebook_node(json_nb)


with open(f'{fn}.xlsx', "wb") as f:
    f.write(body)
