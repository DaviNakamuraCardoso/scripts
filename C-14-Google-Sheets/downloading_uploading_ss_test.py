import ezsheets

# You can download a Google Spreadsheet in a lot of formats: Excel, OpenOffice, PDF, ZIP, CSV, TSV
ss = ezsheets.Spreadsheet('1dxvFnkUlM4cam0Es_5Tn3pgdgG3bcxKWC8HULr_fuNg')
print(ss.title)
#ss.downloadAsExcel() # Downloads as Excel file
#ss.downloadAsCSV() # Downloads as CSV file
#ss.downloadAsPDF() # Downloas as PDF file
#ss.downloadAsODS() # Downloads as ODS file
ss.downloadAsHTML() # Dowloads as a ZIP of HTML files

ss_trash = ezsheets.createSpreadsheet('Delete Me')
print(ezsheets.listSpreadsheets())
ss_trash.delete(permanent=True)

print(ezsheets.listSpreadsheets())
