import ezsheets

ezsheets.upload('../C13-Planilhas-Excel/produceSales.xlsx')
old_ss = ezsheets.Spreadsheet('14eRPcDwS4qfK_byc7TkJdXBT2qHb2bHdeSFPFgzDXW4')
old_sheet = old_ss['Sheet']
old_sheet.getRow(1)
old_sheet.getRow(2)
column_one = old_sheet.getColumn(1)
old_sheet.getRow(3)
old_sheet.updateRow(3, ['Pumpkin', 11.50, 20, 230])
for i, value in enumerate(column_one):
    column_one[i] = value.upper()
old_sheet.updateColumn(1, column_one)
rows = old_sheet.getRows() # Get every row in the sheet
rows[0] # Examine the value in the first row
print(rows[2][0])
rows[1][0] = 'PUMPKIN'
print(rows[10])
rows[10][2] = 400 # Change the pounds sold
rows[10][3] = 904 # Change the total
print(rows[10])
old_sheet.updateRows(rows) # Update the online spreadsheet
print(old_sheet.rowCount) # You can get the number of rows by passing the argument rowCount
print(old_sheet.columnCount) # You can also get the number of columns with columnCount
old_sheet.columnCount = 4 # Change the number of columns to 5
print(old_sheet.column.Count)

