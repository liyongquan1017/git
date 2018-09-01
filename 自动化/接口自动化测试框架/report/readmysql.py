import pymysql
def read_mysql2(sql):
	try:
		connect = pymysql.connect(host='127.0.0.1', port=3306, user='spy', passwd='hexenn', charset='utf8',db='spy')
		cur = connect.cursor()
		try:
			cur.execute(sql)
		except Exception as e:
			print('执行数据库语句失败，错误是%s' % e)
		res = cur.fetchall()
		return res
	except Exception as e:
		print('链接数据库出错了，错误是%s' % e)
		cur.close()
		connect.close()

if __name__ == '__main__':
    sql='select * from app_liveroom_sound'
    res=read_mysql2(sql)
    print(res)