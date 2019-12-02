from utils.operationexcle import OperationExcel
from utils.operation_json import OperationJson
from data.data_config import *

class GetData:
    def __int__(self):
        self.data = OperationExcel().get_data()
    def is_run(self,row):
        flag = None
        col = get_is_run()
        isrun = self.data.cell_value(row,col)
        if isrun == 'yes':
            flag = True
        else:
            flag = False
        return flag
    def request_url(self,row):
        col = get_url()
        url = self.data.cell_value(row,col)
        return url
    def get_method_way(self,row):
        col = get_request_way()
        method_way = self.data.cell_value(row,col)
        return method_way
    def get_is_header(self,row):
        col = get_header()
        is_header = self.data.cell_value(row,col)
        if is_header == '':
            return None
        else:
            return is_header
    def get_method_data(self,row):
        col = get_data()
        method_data = self.data.cell_value(row,col)
        data = OperationJson().get_login_data(method_data)
        return data