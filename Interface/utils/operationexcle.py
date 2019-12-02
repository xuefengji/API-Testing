import xlrd

exlce_data = xlrd.open_workbook('../datas/excel_data.xlsx')

sheet = exlce_data.sheet_by_index(0)

print(sheet.cell(1,3))
print(sheet.nrows)
