import ezsheets

ss = ezsheets.Spreadsheet('1dxvFnkUlM4cam0Es_5Tn3pgdgG3bcxKWC8HULr_fuNg')
print(ss.title)
# Generating new Spreadsheets
# new_ss = ezsheets.createSpreadsheet('My First Real Google Spreadsheet')
new_ss = ezsheets.Spreadsheet('15v89_xtRYGSSEGY6wxyr9Qldv09KMou_1sG9N0d-wwU')
print(new_ss.title)
# Uplaading Spreadsheets
#uploaded_ss = ezsheets.upload('../C13-Planilhas-Excel/redefined_file.xlsx')
#print(uploaded_ss.title)
# Attributes
ss.title = 'My First Test'
print(ss.title)
# The ID
print(ss.spreadsheetId)
# The url
print(ss.url)
# The sheet titles
print(ss.sheetTitles)
# The sheets, in order
print(ss.sheets)
# The first sheet object in the spreadsheet
print(ss[0])
# Sheets can also be accessed by it's title
print(ss['Class'])
# Delete the Teachers sheet
del ss['Teachers']
print(ss.sheetTitles)
# Your script can also refresh the API conection
ss.refresh()

# Spreadsheet Objects
