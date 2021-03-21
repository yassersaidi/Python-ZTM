import PyPDF2
import sys

super_file = sys.argv[1]
watermark_name  = sys.argv[2] #pdf file
output_name =sys.argv[3] 

template   = PyPDF2.PdfFileReader(open(super_file,'rb'))
watermark  = PyPDF2.PdfFileReader(open(watermark_name,'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open(output_name,'wb') as output_file:
        output.write(output_file)