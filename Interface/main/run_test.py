from config.get_data import GetData
from util.operationexcle import OperationExcel
from base.run_method import RunMethod
from util.commutil import CommUtil
import json

class RunMain:
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()
        self.comm_util = CommUtil()
    def go_on_run(self):
        rows_count = self.opera_excel.get_rows()
        for i in range(1,rows_count):
            url = self.data.request_url(i)
            request_data = self.data.get_method_data(i)
            header = self.data.get_is_header(i)
            request_way = self.data.get_method_way(i)
            is_run = self.data.is_run(i)
            expact_result = self.data.expact_result(i)
            # print(expact_result)
            if is_run:
                flag = None
                res = self.run_method.run_main(request_way,url,request_data)
                # print(res)
                # print(type(res['password']))
                result = self.comm_util.comm_util(res['password'],expact_result)
                if result:
                    flag = 'Pass'
                else:
                    flag = 'Fail'
                return flag




if __name__=='__main__':
    run = RunMain()
    print(run.go_on_run())






