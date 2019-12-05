import smtplib
from email.mime.text import MIMEText
from util.operation_json import OperationJson
class SendMail:
    def __init__(self):
        self.email_json = OperationJson().email_json

    #发送邮件设置
    def send_mail(self,to_user_list,sub,content):
        #设置收发件人、主题、内容
        from_user = "xuefeng.ji"+'<'+self.email_json['email_name']+'>'
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['From'] = self.email_json['email_name']
        message['To'] = ';'.join(to_user_list)
        message['Subject'] = sub
        #连接SMTP服务器
        host = self.email_json['email_server']
        username = self.email_json['email_name']
        password = self.email_json['email_password']
        server = smtplib.SMTP()
        server.connect(host,25)
        server.login(username,password)
        server.sendmail(from_user,to_user_list,message.as_string())


    #统计结果发送
    def send_main(self,pass_count,fail_count):
        all_count = pass_count + fail_count
        pass_result = "%.2f%%" %(pass_count / all_count * 100)
        fail_result = "%.2f%%" % (fail_count / all_count * 100)
        user_list = self.email_json['user_list']
        # print(user_list)
        sub = '接口自动化测试报告'
        content = '本次测试接口总数为%s个,通过接口个数为%s个,失败接口数为%s个,通过率为%s,失败率为%s' %(all_count,pass_count,fail_count,pass_result,fail_result)
        self.send_mail(user_list,sub,content)

if __name__=='__main__':
    send_mail = SendMail()
    user_list = ['1369589832@qq.com']
    sub = '自动化接口测试'
    content = '第一封测试报告'
    send_mail.send_mail(user_list,sub,content)



