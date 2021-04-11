import sys
import PyPDF2

inputs = sys.argv[1:]
print(inputs)

def combine(lst):
    merger = PyPDF2.PdfFileMerger()
    for pdf in lst:
        print(pdf)
        merger.append(pdf)

    merger.write("Super.pdf")
    







combine(inputs)

