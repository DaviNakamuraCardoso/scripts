#! /usr/bin/python3

# combining.py - Combina todos os PDFs do diretório de trabalho atual em um único PDF

import PyPDF2
import os

# Obtém os nomes de todos os arquivos PDF

pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)


pdf_files.sort(key=str.lower)
pdf_writer = PyPDF2.PdfFileWriter()
for pdf in pdf_files:
    pdf_file = open(pdf, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    for page_num in range(1, pdf_reader.numPages):
        page_object = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_object)


new_file = open('superpdf.pdf', 'wb')
pdf_writer.write(new_file)
new_file.close()
for pdf_file in pdf_files:
    filename = open(pdf_file, 'rb')
    filename.close()
    

