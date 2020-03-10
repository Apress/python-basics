import openpyxl
buildings_spreadsheet = openpyxl.load_workbook('buildings.xlsx')
heights_sheet = buildings_spreadsheet['heights']
cell_A1 = heights_sheet['A1']
print(cell_A1)
print(cell_A1.value)
row_number = 2
# The following line has a deliberate error. See the video for details
# To get this script working, put a # in front of it to turn it into a comment
name = heights_sheet['A', row_number]
# The following line has a deliberate error. See the video for details
# To get this script working, put a # in front of it to turn it into a comment
'A' + row_number
'A' + str(row_number)
heights_sheet['A' + str(row_number)].value
f'A{row_number}'
f'Five times six is {5 * 6}'
heights_sheet['A' + str(row_number)].value
heights_sheet[f'A{row_number}'].value
for row_number in range(2, 6):
    name = heights_sheet[f'A{row_number}'].value
    country = heights_sheet[f'B{row_number}'].value
    height_meters = heights_sheet[f'C{row_number}'].value
    print(name, country, height_meters)
heights_sheet['D1'].value = 'Height (feet)'
for row in range(2, 6):
    height_meters = heights_sheet[f'C{row}'].value
    height_feet = height_meters * 3.3
    heights_sheet[f'D{row}'].value = height_feet
buildings_spreadsheet.save('buildings2.xlsx')
