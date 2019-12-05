import xlrd
from xlutils.copy import copy

class OperationExcel:

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            #设置默认路径
            self.file_name = '../datas/data_excel.xls'
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

    #得到某一列的值
    def get_col_data(self,col=None):
        if col:
            col_data = self.tables_data.col_values(col)
        else:
            col_data = self.tables_data.col_values(0)
        return col_data


    #向excel中写入数据
    def write_excel(self,row,col,value):
        #打开要写入的excel
        table = xlrd.open_workbook(self.file_name)
        #copy一份新的
        write_data = copy(table)
        #获取sheet表格
        sheet_data = write_data.get_sheet(0)
        #写入数据
        sheet_data.write(row,col,value)
        #表格保存
        write_data.save(self.file_name)


if __name__=='__main__':
    tables = OperationExcel()

    print(tables)

