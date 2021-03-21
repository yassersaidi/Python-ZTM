import PyPDF2 
import sys
#import the PDFs by enter the name of the files
pdf_list = sys.argv[1:]
#start the merger function
def merger(pdf_list):
    for pdf in pdf_list:
        merger = PyPDF2.PdfFileMerger()
        merger.append(pdf)
        print(merger)
    merger.write("super.pdf")
    return True
merger(pdf_list)