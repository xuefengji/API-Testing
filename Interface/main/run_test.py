from config.get_data import GetData
from util.operationexcle import OperationExcel
from base.run_method import RunMethod
from util.commutil import CommUtil
from config.data_depend import DataDepend
from util.send_mail import SendMail
from util.operation_cookie import OperationCookie
from util.operation_json import OperationJson

class RunMain:
    #实例化一些基本的工具个data
    def __init__(self):
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.run_method = RunMethod()
        self.comm_util = CommUtil()
        self.send_mail = SendMail()

    #主函数运行入口
    def go_on_run(self):
        pass_count = 0
        fail_count = 0
        #获取数据行数
        rows_count = self.opera_excel.get_rows()
        #循环数据，并取值进行post或get请求，并获取结果
        for i in range(1,rows_count):
            is_run = self.data.is_run(i)
            # print(expact_result)
            if is_run:
                url = self.data.request_url(i)
                request_data = self.data.get_method_data_depend(i)
                # print(request_data)
                cookies = self.data.get_cookies(i)
                request_way = self.data.get_method_way(i)
                case_depend = self.data.get_case_depend_data(i)
                # print(case_depend)
                expact_result = self.data.expact_result(i)
                request_data_depend = self.data.get_method_data(i)
                #查看是否有数据依赖
                if case_depend != '':
                    data_depend = DataDepend()
                    response_depend = data_depend.get_depend_data(i,case_depend,0)
                    request_data[request_data_depend] = response_depend

                #判断是否需要写入或读取cookie
                if cookies == 'write':
                    cookie_data = OperationCookie().get_cookie(request_way,url,request_data)
                    OperationJson().write_json('../datas/cookie.json',cookie_data)
                elif cookies == 'yes':
                    cookie_data = OperationJson().get_cookie_data('../datas/cookies.json')

                res = self.run_method.run_main(request_way, url, request_data)
                result = self.comm_util.comm_util(str(res['code']),expact_result)
                if result:
                    self.data.write_data(i,'Pass')
                    pass_count += 1
                else:
                    self.data.write_data(i,'Fail')
                    fail_count += 1
        self.send_mail.send_main(pass_count,fail_count)

if __name__=='__main__':
    run = RunMain()
    run.go_on_run()






