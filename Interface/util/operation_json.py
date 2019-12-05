import json

class OperationJson:
    def __init__(self,json_name=None,emil_json = None):
        if json_name:
            self.json_name = json_name
            self.email_json = emil_json
        else:
            self.json_name = '../datas/login.json'
            self.email_json = '../datas/email_count.json'
        self.data = self.get_data()
        self.email_json = self.get_email_data()

    #打开json文件
    def get_data(self):
        try:
            with open(self.json_name)as fp:
                data = json.load(fp)
                return data
        except Exception:
            print('读取文件异常')

    #获取login数据
    def get_login_data(self,id):
        data = self.data[id]
        return data

    #获取邮箱信息
    def get_email_data(self):
        try:
            with open(self.email_json)as fp:
                data = json.load(fp)
                # print(data)
                return data
        except Exception:
            print('读取文件异常')



if __name__=="__main__":
    operajson = OperationJson()
    print(operajson.get_login_data())