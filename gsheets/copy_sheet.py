import ezsheets

ss = ezsheets.Spreadsheet('14eRPcDwS4qfK_byc7TkJdXBT2qHb2bHdeSFPFgzDXW4')
sheet = ss[0]
empty_ss = ezsheets.Spreadsheet('1dxvFnkUlM4cam0Es_5Tn3pgdgG3bcxKWC8HULr_fuNg')
column_one = sheet.getColumn(1)
sheet.copyTo(empty_ss) # Copy the sheet to empty_ss
print(empty_ss.sheetTitles) # empty_ss now contains ss' first sheet
