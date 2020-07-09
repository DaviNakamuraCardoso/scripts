import PyPDF2

pdf_file = open('meetingminutes2.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
page = pdf_reader.getPage(0)
page.rotateClockwise(90)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)
result_file = open('rotatepage.pdf', 'wb')
pdf_writer.write(result_file)
result_file.close()
pdf_file.close()

