import ezsheets

ss = ezsheets.Spreadsheet('1D5hlMzP8-vX7cIf1yvzhOZidKOqpMRe1NLJtuDhn_Bk')
#ss = ezsheets.createSpreadsheet('My First Edited Sheet')
sheet = ss[0]
sheet.title = 'Random Stuff'
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'
print(sheet['A1'])
print(sheet['A2'])
print(sheet[2, 1])
sheet['A2'] = 'Alice'
sheet['B2'] = 23
sheet['C2'] = 'Robocop'
print(ezsheets.convertAddress('A2')) # Converts adresses
print(ezsheets.convertAddress((1, 2)))
print(ezsheets.getColumnLetterOf(40))
print(ezsheets.getColumnNumberOf('GG'))
print(ezsheets.getColumnLetterOf(999))
print(ezsheets.getColumnNumberOf('ZZZ'))
# Creating and deleting sheets
print(ss.sheetTitles)
#new_sheet = ss.createSheet('Spam') # Create a sheet at the end of the ss
#new_eggs_sheet = ss.createSheet('Eggs') # More sheets
print(ss.sheetTitles)
bacon_sheet = ss['Bacon']
bacon_sheet.delete()
ss.createSheet('Bacon', index=0)
print(ss.sheetTitles)
ss[0].delete() # Delete the Bacon sheet
ss['Eggs'].delete() # Delete the Eggs sheet
new_sheet = ss['Spam']
new_sheet.delete() # Delete the Spam sheet
print(ss.sheetTitles)
