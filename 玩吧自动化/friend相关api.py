
import  unittest #####unittest是一个单元测试模块，用于接口自动化，Ui自动化，APP自动化
from lib.tools import read_mysql2,read_mysql,my_request,through_sql
from nose_parameterized import parameterized###这个模块是参数化模块，主要对咱们的测试用例的请求数据进行参数化设置
import random ###随机模块
import json ###这个主要用于数据类型的转换
from lib.data_init import Data

class friend_api(unittest.TestCase):###这句的意思就是把这个类下面的所有test开头的函数（方法）都视为测试用例
        def setUp(self):###执行每条测试用例之前来执行我
            self.url='http://testapitest.wb-intra.com/api/test' ###每条测试用例都需要的域地址
            self.headers={'content-type': "application/x-www-form-urlencoded"}####每条请求头都一样
        @classmethod
        def setUpClass(cls):####执行所有的测试用颗粒之前都来执行我一次
            through_sql()

        @classmethod
        def tearDownClass(cls):###执行所有测试用例以后来执行我一次
            print('执行完成friend相关的api测试用例')


        ####删除好友
        def delete_friend(self,uid,friendUid):
            uid=str(uid)
            friendUid=str(friendUid)
            data={"url":"/api/removeFriend",'params':'{"__t_":"68047730","friendUid":""}'}
            params=eval(data.get('params'))
            params['__t_']=uid
            params['friendUid']=friendUid
            data['params']=json.dumps(params)
            my_request('post',self.url,data=data,headers=self.headers)


    ####获取好友列表
        def get_friend(self,uid):
            uid=str(uid)
            data={"url":"/api/getFriendsList","params":'{"__t_":""}'}
            params=eval(data.get('params'))
            params['__t_']=uid
            data['params']=json.dumps(params)
            response=my_request('post',self.url,data=data,headers=self.headers)
            friends=list(response.keys())
            return friends

    ####获取用户金币
        def get_price(self,uid):
            uid=str(uid)
            data={"url":"/v3/home/userInfo",'params':'{"__t_":""}'}
            params=eval(data.get('params'))
            params['__t_']=uid
            data['params']=json.dumps(params)
            response=my_request('post',self.url,data=data,headers=self.headers)
            money=response.get('data').get('data').get('money')
            price=response.get('data').get('data').get('price')
            return [int(money),int(price)]






        @parameterized.expand(
            [
                [
                    {"url":"/api/v2/addFriend",'params':'{"__t_":"","toUid":""}'},
                ]
            ]
        )
        def test_001(self,data):
            '''用户正常添加好友'''
            value1=self.get_price(68047730)[0]
            price=self.get_price(26422161)[1]
            self.delete_friend(68047730,26422161)
            params=data.get('params')
            params1=eval(params)
            params1['__t_']='68047730'
            params1['toUid']='26422161'
            data['params']=json.dumps(params1)
            response=my_request('post',self.url,data=data,headers=self.headers)
            value2=self.get_price(68047730)[0]
            res=self.get_friend(68047730)
            code=response.get('code')
            data1=response.get('data')
            self.assertEqual(code,0)
            self.assertEqual(data1,None)
            self.assertIn('26422161',str(res))
            self.assertEqual(value1-value2,price)


        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":"","toUid":""}'},

                ]
            ]
        )
        def test_002(self,data):
            '''Touid参数为空添加好友'''
            self.delete_friend(68047730,26422161)
            params=data.get('params')
            params1=eval(params)
            params1['__t_']='68047730'
            params1['toUid']=''
            data['params']=json.dumps(params1)
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b=""')
            code=response.get('code')
            data1=response.get('data')
            self.assertEqual(code,20007)
            self.assertEqual(res,())

        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_003(self,data):
            '''Touid参数缺参添加好友'''
            self.delete_friend(68047730,26422161)
            params=data.get('params')
            params1=eval(params)
            params1['__t_']='68047730'
            data['params']=json.dumps(params1)
            response=my_request('post',self.url,data=data,headers=self.headers)
            code=response.get('code')
            data1=response.get('data')
            self.assertEqual(code,20007)

        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_004(self,data):
            '''Touid参数为空格添加好友'''
            self.delete_friend(68047730,26422161)
            params=data.get('params')
            params1=eval(params)
            params1['__t_']='68047730'
            params1['toUid']=' '
            data['params']=json.dumps(params1)
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b=" "')
            code=response.get('code')
            data1=response.get('data')
            self.assertEqual(code,20007)
            self.assertEqual(res,())

        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_005(self,data):
            '''Touid参数为非数值类型添加好友'''
            self.delete_friend(68047730,26422161)
            params=data.get('params')
            params1=eval(params)
            params1['__t_']='68047730'
            params1['toUid']='26422161'
            data['params']=json.dumps(params1)
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b="26422161"')
            code=response.get('code')
            data1=response.get('data')
            self.assertEqual(code,20007)
            self.assertEqual(res,())


        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_006(self, data):
            '''Touid参数为非玩吧用户添加好友'''
            self.delete_friend(68047730, 26422161)
            params = data.get('params')
            params1 = eval(params)
            params1['__t_'] = '68047730'
            params1['toUid'] = '9999999999'
            data['params'] = json.dumps(params1)
            response = my_request('post', self.url, data=data, headers=self.headers)
            res = read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b=9999999999')
            code = response.get('code')
            data1 = response.get('data')
            self.assertEqual(code, 20007)
            self.assertEqual(res, ())

        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_007(self, data):
            '''用户自己把自己添加为好友'''
            value=self.get_price(68047730)[0]
            params = data.get('params')
            params1 = eval(params)
            params1['__t_'] = '68047730'
            params1['toUid'] = '68047730'
            data['params'] = json.dumps(params1)
            response = my_request('post', self.url, data=data, headers=self.headers)
            res = read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b=68047730')
            value2=self.get_price(68047730)[0]
            code = response.get('code')
            data1 = response.get('data')
            self.assertEqual(code, 20004)
            self.assertEqual(res, ())
            self.assertEqual(value,value2)

        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_008(self, data):
            '''用户重复添加某个用户为好友'''
            self.delete_friend(26422161)
            value = self.get_price(68047730)[0]
            price=self.get_price(26422161)[1]
            params = data.get('params')
            params1 = eval(params)
            params1['__t_'] = '68047730'
            params1['toUid'] = '26422161'
            data['params'] = json.dumps(params1)
            for i in range(5):
                response = my_request('post', self.url, data=data, headers=self.headers)
            res = read_mysql2('select * from app_friend_730 where uid_a=68047730 and uid_b=26422161')
            value2=self.get_price(68047730)[0]
            code = response.get('code')
            data1 = response.get('data')
            self.assertEqual(code, 20004)
            self.assertEqual(len(res),1)
            self.assertEqual(value-value2,price)

        @parameterized.expand(
            [
                [
                    {"url": "/api/v2/addFriend", 'params': '{"__t_":""}'},

                ]
            ]
        )
        def test_009(self, data):
            '''金币不够添加为好友'''
            y=Data()
            y.reset_money(60152919)
            params = data.get('params')
            params1 = eval(params)
            params1['__t_'] = '60152919'
            params1['toUid'] = '26422161'
            data['params'] = json.dumps(params1)
            response = my_request('post', self.url, data=data, headers=self.headers)
            res = read_mysql2('select * from app_friend_730 where uid_a=60152919 and uid_b=26422161')
            value2 = self.get_price(68047730)[0]
            code = response.get('code')
            data1 = response.get('data')
            self.assertEqual(code, 20006)
            self.assertEqual(res, ())

    # 5：好友上限（自己上限是否能添加好友，对方已经上限是否能添加好友）






if __name__ == '__main__':
    unittest.main()












