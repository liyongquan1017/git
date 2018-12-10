import pymysql
import redis
import requests
from conf.setting import MYSQL_INFO,REDIS_INFO,REPORT_Path
from hashlib import md5
import os
###mysql数据库操作
class MyConnect(object):
	def __init__(self, host, port, user, password, db, charset='utf8'):#初始化
		self.__host = host
		self.port = port
		self.user = user
		self.passwd = password
		self.db = db
		self.charset = charset
		self.__get_cur()  # 在类初始化的时候就去调用创建游标的函数

	def __get_cur(self):
		try:
			self.coon = pymysql.connect(
				host=self.__host, port=self.port, user=self.user, passwd=self.passwd,
				charset=self.charset, db=self.db
			)
		except Exception as e:
			print('这里出错了，错误信息是【%s】' % e)
		else:
			self.cur = self.coon.cursor()  # 建立游标

	def select_sql(self, sql):
		self.cur.execute(sql)
		return self.cur.fetchall()

	def other_sql(self, sql):
		try:
			self.cur.execute(sql)
		except Exception as e:
			print('sql执行失败%s' % e)
		else:
			self.coon.commit()

	def close(self):
		self.cur.close()
		self.coon.close()

###redis数据库操作
class MyRedis(object):
	def __init__(self,host='127.0.0.1',port='6379',password='wanbA89612234'):
		self.pool = redis.ConnectionPool(host=host, port=port, password=password)
		self.r = redis.Redis(connection_pool=self.pool)

	#根据key获取value值
	def get(self, k):
		return self.r.get(k)

	#添加键值对
	def set(self, k, v):
		self.r.set(k, v)

	#获取hash类型所有的key
	def get_hash_keys(self,name):
		data=self.r.hkeys(name)
		return data
	def get_keys(self,name):
		data=self.r.keys(name)
		return data

	def get_value(self,name):
		value=self.r.get(name)
		return value

	def is_exists(self,key):
		return self.r.exists(key)

	def get_value_num(self,name,start=0,stop=100,withscores=True):
		return self.r.zrevrange(name,start,stop,withscores)

	#删除KEY值
	def delete_key(self,k):
		tag = self.r.exists(k) #判断这个key是否存在
		if tag:
			self.r.delete(k)
			print('删除Key值(缓存)成功')
		else:
			print('这个key不存在')

	#将name对应的hash中指定key的键值对删除
	def hash_del(self,name,k):
		res = self.r.hdel(name,k)
		if res:
			print('删除成功')
			return 1
		else:
			print('删除失败，该key不存在')
			return 0
	def get_type(self,key):
		attribute=self.r.type(key)
		return attribute

###接口请求
def my_request(method,url,data,headers):
	try:
		if method.upper()=='GET':
			r = requests.get(url,data,headers=headers).json()
		else:
			r = requests.post(url,data,headers=headers).json()
	except Exception as e:
		return '出错了，错误是%s'%e
	return r

def myMd5(st):
	SECRET_KEY = '68@63fc1jkyu4m+wlvyc5(0gik12u9o90tm5q^l^_w^9^%7=zl'
	st = str(st)
	md = md5()
	st = SECRET_KEY+st
	md.update(st.encode())
	return md.hexdigest()

####清除测试报告目录文件
def remove_report():
	html_path=os.path.join(REPORT_Path,'html')
	all_report=os.listdir(html_path)
	for list in all_report:
		abs_path=os.path.join(html_path,list)
		os.remove(abs_path)

def get_newreport():
	html_path = os.path.join(REPORT_Path, 'html')
	all_report = os.listdir(html_path)
	file_name=all_report[0]
	abs_path=os.path.join(html_path,file_name)
	print(abs_path)
	return abs_path

def read_mysql(sql):
	# 建立数据库连接
	try:
		connect = pymysql.connect(host='127.0.0.1', port=3306, user='spy', passwd='hexenn', charset='utf8', db='spy')
	except Exception as e:
		print('连接数据库错误，错误是%s' % e)
	else:
		# 建立游标（设置仓库管理员）
		cur = connect.cursor()
		if 'select' in sql:
			# 执行sql语句
			try:
				cur.execute(sql)
			except Exception as e:
				print('执行sql语句失败，错误是%s' % e)
			else:
				# 获取查询数据
				res = cur.fetchall()
				# 关闭连接
				connect.close()
				# 释放管理员
				cur.close()
				return res[0]
		else:
			try:
				cur.execute(sql)
			except Exception as e:
				print('执行sql语句失败，错误是%s' % e)
			else:
				# 提交数据至数据库
				connect.commit()
				connect.close()
				cur.close()


def read_mysql2(sql):
	#建立数据库连接
	try:
		connect=pymysql.connect(host='127.0.0.1', port=3306, user='spy', passwd='hexenn', charset='utf8',db='spy')
	except Exception as e:
		print('连接数据库错误，错误是%s'%e)
	else:
		#建立游标（设置仓库管理员）
		cur=connect.cursor()
		if 'select' in sql:
			#执行sql语句
			try:
				cur.execute(sql)
			except Exception as e:
				print('执行sql语句失败，错误是%s'%e)
			else:
				#获取查询数据
				res=cur.fetchall()
				#关闭连接
				connect.close()
				#释放管理员
				cur.close()
				return res
		else:
			try:
				cur.execute(sql)
			except Exception as e:
				print('执行sql语句失败，错误是%s'%e)
			else:
				#提交数据至数据库
				connect.commit()
				connect.close()
				cur.close()


def through_sql():
	p_mysql=os.popen('nohup ssh -L 3306:10.173.53.20:3306 readonly@123.56.91.6 -N &')
	p_redis=os.popen('nohup ssh -L 6379:10.173.53.20:6379 readonly@123.56.91.6 -N &')
# my_mysql = MyConnect(**MYSQL_INFO)
# my_redis = MyRedis(**REDIS_INFO)
# get_newreport()
# y=MyRedis()
# y.delete_key('app:liveroom:follow:requency:77338973:68047730:307185')
# y.get('app:liveroom:follow:requency:77338973:68047730:307185')
# through_sql()