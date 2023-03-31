# %% import necessary packages

# unstructured // open source package to manipulate files containing unstructured data
from unstructured.partition.auto import partition

# PyPDF2 // open source package to manipulate .pdf files
from PyPDF2 import PdfReader

# pdfplumber // utility to manipulate .pdf files
import pdfplumber

# essential packages
import os

# TODO: Overall, this needs to be converted to one or a few functions

# %% upload necessary .pdf file

# pdf 
lowenstern_pdf_path = "../../../data/yellowstone/Lowenstern_Origins_Geothermal_Gases_at_Yellowstone.pdf"

out_txt = "../../../data/yellowstone/Lowenstern_Orrigins_Geothermal_Gases_at_Yellowstone.txt"

# %% pdfplumber

with pdfplumber.open(lowenstern_pdf_path) as pdf:
    _page = pdf.pages[1]
    print(_page.extract_text())

# %% PyPDF2

fh = open(lowenstern_pdf_path, "rb")

py_pdfreader = PdfReader(fh)

pagehandle = py_pdfreader.getPage(1)

print(pagehandle.extractText())

# %% unstructured

elements = partition(lowenstern_pdf_path)

with open(out_txt, "w") as f:
    for elem in elements:
        f.write("{}\n\n".format(elem))


print("\n\n".join([str(el) for el in elements]))
# %%
