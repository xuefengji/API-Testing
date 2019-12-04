from config.get_data import GetData
from util.operationexcle import OperationExcel
from base.run_method import RunMethod
from util.commutil import CommUtil
from config.data_depend import DataDepend

class RunMain:
    #实例化一些基本的工具个data
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()
        self.comm_util = CommUtil()

    #主函数运行入口
    def go_on_run(self):
        #获取数据行数
        rows_count = self.opera_excel.get_rows()
        #循环数据，并取值进行post或get请求，并获取结果
        for i in range(1,rows_count):
            url = self.data.request_url(i)
            request_data = self.data.get_method_data(i)
            header = self.data.get_is_header(i)
            request_way = self.data.get_method_way(i)
            is_run = self.data.is_run(i)
            case_depend = self.data.get_case_depend_data(i)
            expact_result = self.data.expact_result(i)
            request_data_depend = self.data.get_method_data(i)
            # print(expact_result)
            if is_run:
                #查看是否有数据依赖
                if case_depend != '':
                    data_depend = DataDepend()
                    response_depend = data_depend.get_depend_data(i,case_depend,0)
                    request_data[request_data_depend] = response_depend
                res = self.run_method.run_main(request_way,url,request_data)
                result = self.comm_util.comm_util(res['password'],expact_result)
                if result:
                    self.data.write_data(i,'Pass')
                else:
                    self.data.write_data(i,'Fail')

if __name__=='__main__':
    run = RunMain()
    run.go_on_run()






