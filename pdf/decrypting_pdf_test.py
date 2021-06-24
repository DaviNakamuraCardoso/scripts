import PyPDF2

pdf_file = open('encrypted.pdf')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print(pdf_reader.isEncrypted) # The attribute isEncrypted is True when the PDF is Encrypted
#pdf_reader.getPage(0) # If we try to get the PDF's pages, a error will occur
pdf_reader.decrypt('rosebud')
page_object = pdf_reader.getPage(0)
print(page_object)
