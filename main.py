# todo Project Goal: Import a readable sales agreement and then scan it for keywords.
# todo Highlight keywords in PDF and create a text document with a list of the keywords and the words surrounding them.
# todo recognize tax schedule, identify fields, copy field to income analysis form.

import PyPDF2
import tkinter

from tkinter import filedialog

root = tkinter.Tk()
root.withdraw()

test_sheet = 'C:\Users\wwfra\Desktop\Frazier_Python_Test.csv'

def key_search():
    filename = filedialog.askopenfilename(parent=root, title='Choose File Path')  # Credit: https://stackoverflow.com/questions/3643418/storing-file-path-using-windows-explorer-browser-in-python
    with open(filename, mode='rb') as f: #rb = read only binary, 'f' is a custom file object. Credit: https://www.soudegesu.com/en/post/python/extract-text-from-pdf-with-pypdf2/
        reader = PyPDF2.PdfFileReader(f)
        results = []
        for page in reader.pages:
            results.append(page.extractText())
        return results

def xl_write():
    with open(test_sheet, 'w') as g:
        csvwt = csv.writer(g)
        for x in key_search():
            csvwt.writerow(x)

pages = key_search()
for page in pages:
    print(page)

