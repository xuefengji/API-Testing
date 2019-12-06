import requests
import json

class RunMethod:
    #封装post请求
    def post_main(self,url,data,cookie):
        #verify=false 关闭验证，允许https的请求
        res = requests.post(url,data,cookies=cookie,verify=False)
        return res.json()
    #封装get请求
    def get_main(self,url,data=None):
        # res = None
        # if header != None:
        #     res = requests.get(url=url, data=data, headers=header)
        # else:
        res = requests.get(url, data,verify=False)
        return res.json()
    #使用主函数控制请求的发送
    def run_main(self,method,url,data,cookie=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,cookie)
        else:
            res = self.get_main(url,data)
        return res