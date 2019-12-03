from config.get_data import GetData
from util.operationexcle import OperationExcel
from base.run_method import RunMethod

class RunMain:
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()

    def go_on_run(self):
        rows_count = self.opera_excel.get_rows()
        for i in range(1,rows_count):
            url = self.data.request_url(i)
            request_data = self.data.get_method_data(i)
            header = self.data.get_is_header(i)
            request_way = self.data.get_method_way(i)
            is_run = self.data.is_run(i)
            if is_run:
                res = self.run_method.run_main(request_way,url,request_data,header)
            return res




if __name__=='__main__':
    run = RunMain()
    print(run.run_test())






