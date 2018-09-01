# unittest是python提供的一个自带的单元测试模块
# parameterized是一个参数化模块
import unittest
import requests
from lib.tools import my_request

from lib.tools import read_mysql2
from nose_parameterized import parameterized
# unittest.TestCase 把类下面的所有def视为测试用例
class userext(unittest.TestCase):
    # 测试开始前，初始化方法
    def setUp(self):
        print("444")

    #装饰器
    @classmethod
    #执行所有测试用力前
    def setUpClass(cls):
        print("ssss1111111111111113333333333333")

    #所有测试用例已执行完毕
    def tearDown(self):
        print('aaa')

    @classmethod
    def tearDownClass(cls):
        print('sss')
    def test_001(self):
        http_url = 'http://testapitest.wb-intra.com/api/test'
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        data = {'params':'{"uid":"68047730","key":"饭量","value":"一碗米饭"}','url':'/api/user/customInfo/add'}
        respose = my_request('post',http_url,data=data,headers=headers)
        sql = "select app_custom_info.key from app_custom_info where uid = '68047730' order by id desc limit 1"
        res = read_mysql2(sql)
        self.assertEqual(res[0][0],'饭量')  # 对比

       # self.assertIn("yang",ress)

        print(res)



import BeautifulReport
if __name__ == '__main__':
    unittest.main()

