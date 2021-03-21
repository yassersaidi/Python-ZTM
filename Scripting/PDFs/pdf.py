from os import write
import PyPDF2 as pdf

with open("dummy.pdf" , 'rb') as file:
    reader = pdf.PdfFileReader(file)
    print(reader.documentInfo)
    print(reader.getNumPages())
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = pdf.PdfFileWriter()
    writer.addPage(page)
    with open("rotate.pdf" , "wb") as new_file:
        writer.write(new_file)
