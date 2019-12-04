from util.operationexcle import OperationExcel
from util.operation_json import OperationJson
from config.data_config import *


#获取表格中各单元格中的数据
class GetData:
    #实例化时得到表格数据
    def __init__(self):
        self.table_data = OperationExcel()

    #获取是否运行
    def is_run(self,row):
        flag = None
        col = get_is_run()
        isrun = self.table_data.get_cell_value(row,col)
        if isrun == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #获取URL
    def request_url(self,row):
        col = get_url()
        url = self.table_data.get_cell_value(row,col)
        return url

    #获取请求方式
    def get_method_way(self,row):
        col = get_request_way()
        method_way = self.table_data.get_cell_value(row,col)
        return method_way

    #获取是否添加header
    def get_is_header(self,row):
        col = get_header()
        is_header = self.table_data.get_cell_value(row,col)
        if is_header == '':
            return None
        else:
            return is_header

    #获取请求发送的数据
    def get_method_data(self,row):
        col = request_data()
        method_data = self.table_data.get_cell_value(row,col)
        data = OperationJson().get_login_data(method_data)
        return data

    #获取期望结果
    def expact_result(self,row):
        col = get_expact_result()
        expact = self.table_data.get_cell_value(row,col)
        return expact
