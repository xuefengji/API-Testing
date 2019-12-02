import json

class OperationJson:
    def __init__(self,json_name=None):
        if json_name:
            self.json_name = json_name
        else:
            self.json_name = '../datas/login.json'
        self.data = self.get_data()

    #打开json文件
    def get_data(self):
        with open(self.json_name)as fp:
            data = json.load(fp)
            return data

    #获取login数据
    def get_login_data(self):
        data = self.data['login']
        return data



if __name__=="__main__":
    operajson = OperationJson()
    print(operajson.get_login_data())