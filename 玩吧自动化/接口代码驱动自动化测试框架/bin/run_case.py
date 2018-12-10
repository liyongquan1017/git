import os,sys,time
BASE_PATH = os.path.dirname(
	os.path.dirname(os.path.abspath(__file__))
)#获取程序的入口总目录
sys.path.insert(0,BASE_PATH)#把目录加入到环境变量里

import unittest#导入HTMLTestRunner和xmlrunner模块
from conf.setting import CASE_PATH,HTML_path,XML_path
from lib.sendmail_new import Sendmail
from conf.setting import EMAIL_INFO
from BeautifulReport import BeautifulReport
from lib.tools import remove_report,get_newreport

user=EMAIL_INFO.get('user')#从配置文件中获取邮件用户名
password=EMAIL_INFO.get('password')#从配置文件中获取邮件密码
to=EMAIL_INFO.get('to')#从配置文件中获取邮件接收者
cc=EMAIL_INFO.get('cc')#从配置文件中获取抄送者
subject=EMAIL_INFO.get('subject')##从配置文件中获取邮件标题
contents=EMAIL_INFO.get('content')#从配置文件中获取邮件内容
host=EMAIL_INFO.get('host')##从配置文件中获取邮箱服务器地址

def html_run():
	suite = unittest.TestSuite()#建立测试集合
	all_cases = unittest.defaultTestLoader.discover(CASE_PATH,'*.py')#把case目录下的所有测试用例.py加入到一个list里
	for case in all_cases:#循环测试用例list
		suite.addTests(case)#把测试用例.py加入到测试集合里
	run = BeautifulReport(suite)
	run.report(filename="%s_report.html" % time.strftime('%Y%m%d%H%M%S'), description='玩吧服务端api自动化测试报告', log_path=HTML_path)
	# send = SendMail(username, passwd, recv, title, content, file_name)#实例化发邮件函数
	# send.send_mail()#发送邮件

# #####xml_run同上，运行测试用例生成xml格式的测试报告给jenkins
# def xml_run():
# 	suite = unittest.TestSuite()
# 	all_cases = unittest.defaultTestLoader.discover(CASE_PATH,'*.py')
# 	for case in all_cases:
# 		suite.addTests(case)
# 	runner = xmlrunner.XMLTestRunner(output=XML_path)
# 	runner.run(suite)
# 	send = SendMail(username, passwd, recv, title, content, file_name)
# 	send.send_mail()


# remove_report()#调用tools里的remove_report函数清空report/html目录下的文件
html_run()#运行程序，完成运行测试用例，校验结果，生成报告，发送邮件操作
file_name=get_newreport()#获取新生成的测试报告
send = Sendmail(user, password,host,to, cc, subject,contents,file_name)#实例化发邮件函数
send.send_mail()#发送邮件