import unittest   #第三方单元测试模块，可以用于自动化测试。
from lib.tools import through_sql,read_mysql,read_mysql2,my_request
from parameterized import parameterized  # 这个模块是参数化模块，主要对我们的测试用例进行参数化
import random
import json #主要用于数据类型的转换
from BeautifulReport import BeautifulReport

class friend_api(unittest.TestCase):  #该类下的所有test开头的都为测试用例
    def setUp(self): #执行每条测试用例前执行我
        self.url = 'http://testapitest.wb-intra.com/api/test'
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}
    def tearDown(self):   #执行每条结束后执行
        print()
    @classmethod
    def setUpClass(cls): #执行所有测试用例前执行
        print('开始执行测试用例')
    @classmethod
    def tearDownClass(cls): #执行所有测试用例结束后执行
        print('测试用例执行成功')
    @parameterized.expand(
        [
            [
                {"url":"/api/v2/addFriend","params":'{"__t_":"","toUid":""}'},
                '14596652',
                '55398833'

            ]
        ]
    )
    def test_001(self,data,myUid,friendUid):
        self.remove_friend(myUid, friendUid)
        params = eval(data.get('params'))
        params['__t_'] = myUid
        params['toUid'] = friendUid
        data['params'] = json.dumps(params)
        res = my_request('post',url = self.url,data = data,headers= self.headers)
        myFriendList = self.getFriendList(myUid)
        value = list(myFriendList.keys())
        code = res.get('code')
        resData = res.get('data')
        self.assertEqual(code,0)
        self.assertEqual(data,None)
        self.assertIn(friendUid,str(myFriendList))
        print(value)
        print(res)


    def remove_friend(self,myUid,friendUid):
        data = {"url":"/v3/friend/removeFriend","params":'{"__t_":"","friendUid":""}'}
        params = eval(data.get('params'))
        params['__t_'] = myUid
        params['friendUid'] = friendUid
        data['params'] = json.dumps(params)
        res = my_request('post',url = self.url,data = data,headers= self.headers)
        print(res)
    def getFriendList(self,myUid):
        data = {"url":"/api/getFriendsList","params":'{"__t_":""}'}
        params = eval(data.get('params'))
        params['__t_'] = myUid
        data['params'] = json.dumps(params)
        res = my_request('post',url = self.url,data = data,headers= self.headers)
        return res
    def test2(self):
        print()
if __name__ == '__main__':
    unittest.main()



