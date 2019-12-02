import xlrd

class OperationExcel:

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            #设置默认路径
            self.file_name = '../datas/excel_data.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    def get_data(self):
        exlce_data = xlrd.open_workbook(self.file_name)
        tables = exlce_data.sheet_by_index(self.sheet_id)
        return tables

    #得到表格行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    #得到具体单元格数据
    def get_cell_value(self,row,col):
        data = self.data.cell(row,col)
        return data

if __name__=='__main__':
    tables = OperationExcel()

    print(tables.get_cell_value(1,3))

