from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()
direct = os.curdir
base = os.path.curdir

base_path = os.path.join(base, 'PDFs-to-merge')
out_path = os.path.join(base, "Output")

for file in os.listdir(base_path):
    file = base_path + '/' + file
    if file.endswith(".pdf"):
        merger.append(file)
        print("Combined !!", file)
    out = out_path + '/' + "New-Combined.pdf"
    merger.write(out)
