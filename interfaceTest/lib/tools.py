import pymysql
import requests
from conf.setting_info import mysql_info


#mysql操作
class mySql(object):
    # 初始化
    def __int__(self,host,port,user,passward,db,chaeset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passward = passward
        self.db = db
        self.charset = chaeset
        self.__myCur__()    #获取游标（创建操作数据库的管理员）

    # 创建游标
    def __myCur__(self):
        try:
            self.myCoon = pymysql.connect(
                host=self.host, port=self.port,
                user=self.user, passward=self.passward,
                db=self.db, charset=self.charset
            )
        except Exception as e:
            print("连接数据库出错了，错误是【%s】"%e)
        else:
            self.cur = self.myCoon.cursor()
    def select_sql(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()
    def other_sql(self,sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            print("sql操作失败，错误为【%s】"%e)
            self.myCoon.rollback()
    def close_sql(self):
        self.cur.close()
        self.myCoon.close()

class myinterFace_request(object):
    def __init__(self,url,headers,data):
        self.url = url
        self.headers = headers
        self.data = data
    def mfGet(self):
        try:
            mtGet = requests.get(self.url,self.data).json()
        except Exception as e:
            print("发生错误，错误为：【%s】"%e)
        else:
            return mtGet

    def mfPost(self):
        try:
            mtPost = requests.post(self.url,self.headers,self.data).json()
        except Exception as e:
            print("post请求出错，错误为：【%s】"%e)
        else:
            return mtPost


def sql_conn():
    host = mysql_info.get('host')
    port = mysql_info.get('port')
    user = mysql_info.get('user')
    passwd = mysql_info.get('passwd')
    db = mysql_info.get('db')
    charset = mysql_info.get('charset')
    try:
        connect = pymysql.connect(host=host,port = port,user = user,passwd = passwd,db = db,charset=charset)

    except Exception as e:

        print("连接数据库出错,错误为：【%s】"%e)
    else:
        return connect

def select_sql(sql):
        conn = sql_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            cur.close()
            conn.close()
            print("sql执行出错，错误为：【%s】" % e)
        else:
            allData = cur.fetchall()
            cur.close()
            conn.close()
            return allData

def other_sql(sql):
    try:
        conn = sql_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()

        except Exception as e:
            conn.rollback()
            cur.close()
            conn.close()
            print("sql执行错误，错误为：【%s】" % e)
        else:
            cur.close()
            conn.close()
    except Exception as e:
        print("数据库操作失败，错误为：【%s】"%e)







