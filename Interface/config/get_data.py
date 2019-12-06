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

    #获取cookie(目前将header栏改为cookie)
    def get_cookies(self,row):
        col  = get_header()
        is_cookie = self.table_data.get_cell_value(row,col)
        return is_cookie


    #获取请求时的数据
    def get_method_data_depend(self,row):
        col = get_method_request_data()
        method_data = self.table_data.get_cell_value(row,col)
        data = OperationJson().get_login_data(method_data)
        return data

    #获取请求发送的数据依赖
    def get_method_data(self,row):
        col = request_data()
        method_data = self.table_data.get_cell_value(row,col)
        return method_data

    #获取期望结果
    def expact_result(self,row):
        col = get_expact_result()
        expact = self.table_data.get_cell_value(row,col)
        return expact


    #写入excel表格
    def write_data(self,row,value):
        col = get_result()
        self.table_data.write_excel(row,col,value)


    #得到case依赖的数据
    def get_case_depend_data(self,row):
        col = get_case_depend()
        case_depend_data = self.table_data.get_cell_value(row,col)
        return case_depend_data

    #得到依赖返回值数据
    def get_response_depend_data(self,row):
        col = get_data_depand()
        response_depend = self.table_data.get_cell_value(row,col)
        return response_depend

    #获取case_id列的值
    def get_case_id(self,col=None):
        case_id_data = self.table_data.get_col_data(col)
        return case_id_data



