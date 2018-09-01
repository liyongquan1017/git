##redis数控配置信息
REDIS_INFO = {
	'host':'116.196.122.221',
	'port':6379,
	'password':'123456'
}

####mysql数据库配置信息
MYSQL_INFO  = {
	'host':'116.196.122.221',
	'port':3306,
	'user':'besttest',
	'password':'123456',
	'db':'main',
	'charset':'utf8'
}
HOST_INFO = 'http://api.nnzhp.cn'
#对应的环境信息
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT_Path= os.path.join(BASE_PATH,'report')
XML_path = os.path.join(REPORT_Path,'xml')
HTML_path = os.path.join(REPORT_Path,'html')
CASE_PATH = os.path.join(BASE_PATH,'cases')


EMAIL_INFO = {
	'username':'yangjianbo@moqipobing.com',#发件箱
	'passwd':'Yjbtest123',#邮箱授权码
	'recv':['1061982257@qq.com','yangjianbo@moqipobing.com','liuwenju@moqipobing.com','lishipeng@moqipobing.com','ronghuayang@moqipobing.com','xulei@moqipobing.com','zhangyimin@moqipobing.com','zhangchang@moqipobing.com'],#收件人
	'title':'测试环境接口自动化测试报告',#邮箱host
	'content':'语音房接口测试报告系统自动发送请勿回复！！有哪些需要用例需要补全覆盖请与我联系 谢谢！，\nEnvironmental Science：测试环境 \n具体测试报告详情请下载附件查看，所有测试测试用例请点击ALL查看！\nQA 杨建波\n北京默契破冰科技有限公司\n电话：13720094293\n邮箱：yangjianbo@moqipobing.com\n地址：北京市东城区东直门外大街46号天恒大厦B座23层'#端口号
}


