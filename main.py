# Project Goal: Import a readable sales agreement and then scan it for keywords.
# Highlight keywords in PDF and create a text document with a list of the keywords and the words surrounding them.

import PyPDF2
import tkinter

from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

filename = filedialog.askopenfilename(parent=root,title='Choose File Path') #Credit: https://stackoverflow.com/questions/3643418/storing-file-path-using-windows-explorer-browser-in-python

with open(filename, mode='rb') as f: #rb = read only binary, 'f' is a custom file object.
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())





