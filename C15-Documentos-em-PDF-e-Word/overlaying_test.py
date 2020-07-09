import PyPDF2

pdf_file_content = open('meetingminutes2.pdf', 'rb')
pdf_file_mark = open('watermark.pdf', 'rb')
pdf_reader_1 = PyPDF2.PdfFileReader(pdf_file_content)
pdf_reader_2 = PyPDF2.PdfFileReader(pdf_file_mark)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_file_content_first_page = pdf_reader_1.getPage(0)
pdf_file_mark_first_page = pdf_reader_2.getPage(0)
pdf_file_content_first_page.mergePage(pdf_file_mark_first_page)
pdf_writer.addPage(pdf_file_content_first_page)
for page_num in range(1, pdf_reader_1.numPages):
    page_object = pdf_reader_1.getPage(page_num)
    pdf_writer.addPage(page_object)

result_file = open('watermarkcover.pdf', 'wb')
pdf_writer.write(result_file)
pdf_file_content.close()
pdf_file_mark.close()
result_file.close()
