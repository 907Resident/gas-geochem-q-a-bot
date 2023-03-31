# %% import necessary packages

# PyPDF2 // open source package to manipulate .pdf files
from PyPDF2 import PdfReader

# pdfplumber // utility to manipulate .pdf files
import pdfplumber

# essential packages
import os

# %% upload necessary .pdf file

# pdf 
lowenstern_pdf_path = "../../../data/yellowstone/Lowenstern_Origins_Geothermal_Gases_at_Yellowstone.pdf"

# %% pdfplumber

with pdfplumber.open(lowenstern_pdf_path) as pdf:
    _page = pdf.pages[1]
    print(_page.extract_text())

# %% PyPDF2

fh = open(lowenstern_pdf_path, "rb")

py_pdfreader = PdfReader(fh)

pagehandle = py_pdfreader.getPage(1)

print(pagehandle.extractText())

# %%
