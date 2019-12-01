import requests
import json

class Run_Main():
    #初始化
    # def __init__(self,url,data,method):
    #    self.res = self.run(url,data,'POST')

    def send_post(self,url,data):
        res = requests.post(url,data)
        return res.json()

    def send_get(self,url,data):
        res = requests.get(url,data)
        return res.json()

    def run_main(self,url,data,method):
        res = None
        if method == 'POST':
            res = self.send_post(url,data)
        if method == 'GET':
            res = self.send_get(url,data)
        return res

if __name__=='__main__':
    url = 'http://127.0.0.1:8000/login/'
    data = {'username': 'dddddd', 'password': 11111111}
    # res = Run_Main(url,data,'POST')
    run = Run_Main()
    res = run.run_main(url,data,'POST')
    print(res)