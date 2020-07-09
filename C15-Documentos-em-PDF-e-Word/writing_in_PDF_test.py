import PyPDF2

pdf_file_1 = open('meetingminutes.pdf', 'rb')
pdf_file_2 = open('meetingminutes2.pdf', 'rb')
pdf_1_reader = PyPDF2.PdfFileReader(pdf_file_1)
pdf_2_reader = PyPDF2.PdfFileReader(pdf_file_2)
pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(pdf_1_reader.numPages):
    page_object = pdf_1_reader.getPage(pageNum)
    pdf_writer.addPage(page_object)
for pageNum in range(pdf_2_reader.numPages):
    page_object = pdf_2_reader.getPage(pageNum)
    pdf_writer.addPage(page_object)

pdf_output_file = open('combinedminutes.pdf', 'wb')
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
pdf_file_1.close()
pdf_file_2.close()
