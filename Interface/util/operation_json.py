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
        except Exception as e:
            print(e)

    #获取login数据
    def get_login_data(self,id):
        data = self.data[id]
        return data

    #读取cookie文件：
    def get_cookie_data(self,filename):
        try:
            with open(filename)as fp:
                cookie_data = json.load(fp)
                return cookie_data
        except Exception as e:
            print(e)

    #获取邮箱信息
    def get_email_data(self):
        try:
            with open(self.email_json)as fp:
                data = json.load(fp)
                # print(data)
                return data
        except Exception as e:
            print(e)

    #将json文件写入
    def write_json(self,filename,result):
        try:
            with open(filename,'w')as f:
                f.write(json.dumps(result))
        except Exception as e:
            print(e)





if __name__=="__main__":
    operajson = OperationJson()
    print(operajson.get_login_data())