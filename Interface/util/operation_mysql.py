import pymysql

class OperationMysql:
    #初始化时连接数据库
    def __init__(self):
        self.db = pymysql.connect(
        host="localhost",
        port=3306,
        db='test',
        user='root',
        password='123456',
        charset='utf8')
        self.cur = self.db.cursor()

    #获取数据
    def get_sql_one_data(self,sql):
        try:
            self.cur.execute(sql)
            #获取字段信息
            index =  self.cur.description
            data = self.cur.fetchone()
            # print(len(data))
            #将字段与数据关联，形成字典
            result = {}
            for i in range(len(data)):
                result[index[i][0]] = data[i]
            # self.cur.close()
            # print(type(result))
            return result
        except Exception as e:
            print(e)


if __name__=='__main__':
    mysql = OperationMysql()
    data = mysql.get_sql_one_data("select * from user where username='dasss'")
    print(data)