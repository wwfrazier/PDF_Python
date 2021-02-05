# Project Goal: Import a readable sales agreement and then scan it for keywords.
# Highlight keywords in PDF and create a text document with a list of the keywords and the words surrounding them.

import PyPDF2
import tkinter
import os
import sys

original_stdout = sys.stdout # Save a reference to the original standard output
sys.stdout = open('TestPDF.txt', 'w+')

from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

filename = filedialog.askopenfilename(parent=root,title='Choose File Path') #Credit: https://stackoverflow.com/questions/3643418/storing-file-path-using-windows-explorer-browser-in-python

with open(filename, mode='rb') as f: #rb = read only binary, 'f' is a custom file object. Credit: https://www.soudegesu.com/en/post/python/extract-text-from-pdf-with-pypdf2/
    reader = PyPDF2.PdfFileReader(f)
    #(1)sys.stdout = f  # Change the standard output to the file we created
    for page in reader.pages:
        pass
    print(page.extractText())
    #(1)sys.stdout = original_stdout  # Reset the standard output to its original value



#t = open("TestPDF.txt", "w+") #(Replaced with os.system command for now)

#os.system('notepad.exe ' + 'TestPDF.txt')




