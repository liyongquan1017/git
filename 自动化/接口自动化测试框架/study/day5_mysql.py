# 1:写入型接口（insert delte upedate）
# 2：获取型接口 (get)
# pymysql(第三方模块是需要进行安装的，在cmd通过pip install pymysl命令进行安装)
# host是数据库IP地址
# user是数据库用户名
# password是数据库密码
# port是连接端口
# charset是数据库字符集
# db是你要连接的数据库
# fetchone是获取一条数据
# fetchall是获取所有的数据
def chaxun(sql):
    import pymysql
    #创建连接mysql数据库通道
    connect=pymysql.connect(host='127.0.0.1',user='root',password='Yjbtest123',port=3307,charset='utf8',db='wanba')
    #建立游标（设置数据库仓库管理员）
    cur=connect.cursor()
    #执行sql语句
    cur.execute(sql)
    #获取回传数据
    res=cur.fetchall()
    #关闭连接
    connect.close()
    #解放仓库管理员
    cur.close()
    return res

def xieru():
    import pymysql
    connect=pymysql.connect(host='127.0.0.1',user='root',password='Yjbtest123',port=3307,charset='utf8',db='wanba')
    cur=connect.cursor()
    sql='insert into test (username,age,height) values ("chenxin","16","175CM")'
    cur.execute(sql)
    #提交数据至数据库
    connect.commit()
    connect.close()
    cur.close()

def caozuo_mysql(sql):
    import pymysql
    #创建连接数据库通道
    connect=pymysql.connect(host='127.0.0.1',user='root',password='Yjbtest123',port=3307,charset='utf8',db='wanba')
    #设置仓库管理员
    curor=connect.cursor()
    if 'select' in sql:
        curor.execute(sql)
        res=curor.fetchall()
        connect.close()
        curor.close()
        return res
    else:
        curor.execute(sql)
        connect.commit()
        connect.close()
        curor.close()
# caozuo_mysql("update test set age='28' where username='chenxin'")
# res=caozuo_mysql("select age from test where username='chenxin'")
for i in range(10):
    import random
    import string
    username=''.join(random.sample(string.ascii_lowercase,5))
    age=''.join(random.sample(string.digits,2))
    height=''.join(random.sample(string.digits,3))+'CM'
    caozuo_mysql("insert into test (username,age,height) values('%s','%s','%s')"%(username,age,height))




