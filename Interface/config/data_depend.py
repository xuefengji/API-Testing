from config.get_data import GetData
from base.run_method import RunMethod
from jsonpath_rw import parse,jsonpath
class DataDepend:
    def __init__(self):
        self.data = GetData()
        self.run_method = RunMethod()
    #根据case_id获取行号
    def get_row_count(self,case_id,col):
        row_count = 0
        case_datas = self.data.get_case_id(col)
        for id in case_datas:
            if case_id in id:
                return row_count
            row_count += 1

    #获取返回值
    def get_response_data(self,case_id,col):
        row_count = self.get_row_count(case_id,col)
        url = self.data.request_url(row_count)
        is_run = self.data.is_run(row_count)
        request_way = self.data.get_method_way(row_count)
        request_data = self.data.get_method_data_depend(row_count)
        if is_run:
           res =  self.run_method.run_main(request_way,url,request_data)
        return res

    #获取依赖的数据值
    def get_depend_data(self,row,case_id,col):
        depend_data = self.data.get_response_depend_data(row)
        response = self.get_response_data(case_id,col)
        jsonpath_expr = parse(depend_data)
        res_data = jsonpath_expr.find(response)
        return [match.value for match in res_data]

