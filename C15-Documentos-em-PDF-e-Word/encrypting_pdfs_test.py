import PyPDF2

pdf_file = open('meetingminutes2.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()
for page_num in range(pdf_reader.numPages):
    page_object = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_object)

pdf_writer.encrypt('édavi')
result_pdf = open('pdf_criptografado.pdf', 'wb')
pdf_writer.write(result_pdf)
result_pdf.close()
pdf_file.close()
