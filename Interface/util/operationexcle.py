import xlrd
from xlutils.copy import copy

class OperationExcel:

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            #设置默认路径
            self.file_name = '../datas/excel_data.xlsx'
            self.sheet_id = 0
        self.tables_data = self.get_data()

    def get_data(self):
        exlce_data = xlrd.open_workbook(self.file_name)
        tables = exlce_data.sheet_by_index(self.sheet_id)
        return tables

    #得到表格行数
    def get_rows(self):
        rows = self.tables_data.nrows
        return rows

    #得到具体单元格数据
    def get_cell_value(self,row,col):
        data = self.tables_data.cell_value(row,col)
        return data

    #向excel中写入数据
    def write_excel(self,row,col,value):
        table = xlrd.open_workbook(self.file_name)
        write_data = copy(table)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)


if __name__=='__main__':
    tables = OperationExcel()

    print(tables)

