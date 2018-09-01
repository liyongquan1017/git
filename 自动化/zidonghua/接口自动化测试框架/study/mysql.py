


# pymysql(第三方的方法)
# 安装方法：pip install pymysql
def select_mysql(sql):
    import pymysql
    # 1:建立与数据库的连接
    connect=pymysql.connect(host='127.0.0.1',user='root',password='Yjbtest123',charset='utf8',port=3307,db='wanba')
    # 2:设置仓库管理员（建立游标）
    cur=connect.cursor()
    # 3:执行sql命令（仓库管理员帮你干活）
    cur.execute(sql)
    #获取你从数据库查询的数据
    res=cur.fetcall()
    print(res)
    #关闭连接
    connect.close()
    #解放管理员
    cur.close()

def write_mysql(sql):
    import pymysql
    '''写入型数据库操作'''
    connect=pymysql.connect(host='127.0.0.1',user='root',port=3307,password='Yjbtest123',charset='utf8',db='wanba')
    cur=connect.cursor()
    cur.execute(sql)
    #提交数据至数据库
    connect.commit()



def caozuo_mysql(sql):
    import pymysql
    try:
        connect=pymysql.connect(host='127.0.0.1',user='root',port=3307,password='Yjbtest123',charset='utf8',db='wanba')
    except Exception as e:
        print('连接数据库出错，错误是%s'%e)
    else:
        cur=connect.cursor()
        if 'select' in sql:
            try:
                cur.execute(sql)
            except Exception as e:
                print('执行mysql语句错误,错误是%s'%e)
            else:
                res=cur.fetchall()
                connect.close()
                cur.close()
                return res
        else:
            try:
                cur.execute(sql)
            except Exception as e:
                print('执行mysql语句错误，错误是%s'%e)
            else:
                connect.commit()
                connect.close()
                cur.close()


 # for i in range(1,5):
#     # print('这是第%s次循环,循环的元素是%s'%(i,i))
#     value=[]
#     for j in range(1,5):
#         if i!=j:(先去除相同元素的数字)
#             num='%s%s'%(i,j)
#             print(num)
#     if num not in value:
#         value.append(num)


# 接口测试：有两种类型接口 一种是get型接口，一种是写入型接口
# res=caozuo_mysql("select into test1(username,age,height) values('hongxing','10','169CM')")

