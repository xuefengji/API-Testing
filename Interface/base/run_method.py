import requests

class RunMethod:
    #封装post请求
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url,data,headers=header).json()
        else:
            res = requests.post(url,data).json()
        return res
    #封装get请求
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url, data=data, headers=header).json()
        else:
            res = requests.get(url, data=data).json()
        return res
    #使用主函数控制请求的发送
    def run_main(self,method,url,data,header):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res
