import requests

class RunMethod:
    #封装post请求
    def post_main(self,url,data):
        # res = None
        # if header != None:
        #     res = requests.post(url=url,data=data,headers=header)
        # else:
        res = requests.post(url,data)
        return res.json()
    #封装get请求
    def get_main(self,url,data=None):
        # res = None
        # if header != None:
        #     res = requests.get(url=url, data=data, headers=header)
        # else:
        res = requests.get(url, data)
        return res.json()
    #使用主函数控制请求的发送
    def run_main(self,method,url,data):
        res = None
        if method == 'post':
            res = self.post_main(url,data)
        else:
            res = self.get_main(url,data)
        return res
