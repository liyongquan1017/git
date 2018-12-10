import yagmail
###发送邮件
###user为发送邮件的邮箱名，passwd为邮箱授权码，host为邮箱服务器，port为端口号
###to为接受者的邮箱多个邮箱用list,subject为邮件标题，contnets为邮件正文，attachments为邮件带的附件
class Sendmail(object):
    def __init__(self,user,password,host,to,cc,subject,contents,attachments=None):
        self.to=to  ###接收者的邮箱地址
        self.cc=cc  ####抄送邮件
        self.subject=subject  ####邮件标题
        self.contents=contents  ####邮件正文
        self.attachments=attachments  ####附件
        self.user=user   ###发送者邮箱
        self.password=password  ####发送者邮箱密码
        self.host=host   ###邮箱服务器

    def send_mail(self):
        yag=yagmail.SMTP(user=self.user,password=self.password,host=self.host)
        try:
            yag.send(to=self.to,cc=self.cc,subject=self.subject,contents=self.contents,attachments=self.attachments)
            print('邮件发送成功！')
        except Exception as e:
            print('邮件发送出错，请检查!错误是%s'%e)

if __name__ == '__main__':
    user='liyongquan@moqipobing.com'
    password='Lyq18335446369'
    host='smtp.moqipobing.com'
    to='1061982257@qq.com'
    cc=["516902394@qq.com","yangjianbo@moqipobing.com"]
    subject='测试报告'
    contents='这是测试'
    attachments=r'D:\project\接口代码驱动自动化测试(服务端)\report\html\20180428120550_report.html'
    y=Sendmail(user,password,host,to,cc,subject,contents)
    y.send_mail()

