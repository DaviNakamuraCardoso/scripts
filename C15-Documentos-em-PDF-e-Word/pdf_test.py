import PyPDF2

pdf_file_object = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_object)
print(pdf_reader.numPages)
page_object = pdf_reader.getPage(0)
print(page_object.extractText())