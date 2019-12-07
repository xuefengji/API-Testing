import pymysql

class OperationMysql:
    #初始化时连接数据库
    def __init__(self):
        self.db = pymysql.connect(
        host="localhost",
        port=3306,
        db='api_test',
        user='root',
        password='',
        charset='utf8')
        self.cur = self.db.cursor()

    #获取数据
    def get_sql_one_data(self,sql):
        try:
            self.cur.execute(sql)
            data = self.cur.fetchone()
            return data
        except Exception as e:
            print(e)



