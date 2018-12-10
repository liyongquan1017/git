import unittest  ####导入unittest单元 测试模块
from lib.tools import read_mysql2,through_sql,read_mysql###导入mysql操作方法，mysql2是去记录里所有的（二维数据），mysql是取一维数据，through_sql是穿透数据库函数
from nose_parameterized import parameterized ###parameterized是参数化模块
from lib.tools import my_request###接口请求处理函数
import random###随机模块
import json####这个是把字符串和可以进行逻辑运算的数据类型进行转换

class friend_api(unittest.TestCase):####就是把这个类里面的def函数test开头的都视为测试用例
    def setUp(self):
        self.url='http://testapitest.wb-intra.com/api/test'
        self.headers={'Content-Type': "application/x-www-form-urlencoded"}

    @classmethod
    def setUpClass(cls):
        print()

    @classmethod
    def tearDownClass(cls):
        print('执行完成friend相关的接口测试用例')

    ###删除好友
    def remove_friend(self,uid):
        data={"url":"/api/removeFriend",'params':'{"uid":"68047730","friendUid":""}'}
        params=eval(data.get('params'))
        params['friendUid']=uid
        data['params']=json.dumps(params)
        res=my_request('post',self.url,data=data,headers=self.headers)
        print(res)

    def get_price(self,uid):
        data={"url":"/v3/home/userInfo",'params':'{"uid":"71117757"}'}
        params=eval(data.get('params'))
        params['uid']=uid
        data['params']=json.dumps(params)
        res=my_request('post',self.url,data=data,headers=self.headers)
        price=res.get('data').get('data').get('price')
        return price


    ####获取用户金钱
    def get_value(self,uid):
        data = {"url": "/api/getScoreAndMoney", "params": '{"uid":"uid"}'}
        params=eval(data.get('params'))
        params['uid']=uid
        data['params']=json.dumps(params)
        res=my_request('post',self.url,data=data,headers=self.headers)
        money=res.get('money')
        return int(money)

    @parameterized.expand(
        [
            [
                {"url":"/api/v2/addFriend",'params':'{"uid":"68047730","toUid":""}'},
            ]
        ]
    )
    def test_001(self,data):
        '''正常添加好友'''
        hongxing=self.get_price(71117757)
        num=self.get_value(68047730)
        self.remove_friend(71117757)
        params=data.get('params')
        params=eval(params)
        params['toUid']='71117757'
        data['params']=json.dumps(params)
        res=my_request('post',self.url,data=data,headers=self.headers)
        num1=self.get_value(68047730)
        value=read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b=71117757')
        self.assertEqual(res.get('code'),0)
        self.assertEqual(res.get('msg'),'加上好友啦！一起玩吧')
        self.assertEqual(res.get('data'),None)
        self.assertNotEqual(value,())
        self.assertEqual(num-num1,hongxing)


if __name__ == '__main__':
    unittest.main()

