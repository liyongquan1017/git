import random
import unittest
from lib.tools import my_request
import json
from nose_parameterized import parameterized
from lib.tools import read_mysql,read_mysql2
import string

class ChatGroup_test(unittest.TestCase):
    def setUp(self):
        self.url='http://testapitest.wb-intra.com/api/test'
        self.headers={'content-type': "application/x-www-form-urlencoded"}
    @classmethod
    def tearDownClass(cls):
        print('执行完成ChatGroup相关接口测试用例')

    def remove_chatgroup(self,id):
        #删除解散群组
        headers={'content-type': 'application/x-www-form-urlencoded'}
        data = {"url": "/api/groupChat/removeGroup"}
        params = {"uid": "68047730"}
        params['groupId'] = id
        params=json.dumps(params)
        data['params']=params
        response=my_request("post",self.url,data=data,headers=headers)


    def add_chatgroup(self,chatname):
        headers={'content-type': "application/x-www-form-urlencoded"}
        data={'url': '/api/groupChat/createGroup', 'params': '{"uid":"68047730","groupName":"chatname"}'}
        params=eval(data.get('params'))
        params['groupName']=chatname
        params=json.dumps(params)
        data['params']=params
        response=my_request("post",self.url,data=data,headers=headers)
        id=response.get('data').get('chatGroupInfo').get('id')
        return id



    ##组相关接口测试用例#####
    ##创建群组############
    @parameterized.expand(
        [#正确创建群组
            [
                {'url': '/api/groupChat/createGroup', 'params': '{"uid":"68047730","groupName":"QA杨建波"}'}
            ]
        ]
    )
    def test_001(self,data):
        '''正常创建群组'''
        res_all=read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all=[]
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response=my_request("post",self.url,data=data,headers=self.headers)
        data=read_mysql('select name,owner_id from chat_group_info where owner_id=68047730 ')
        self.assertEqual(data[0],'QA杨建波')
        self.assertEqual(data[1],'68047730')




    @parameterized.expand(
        [
            [
                {'url': '/api/groupChat/createGroup', 'params': '{"uid":"68047730","groupName":"QA杨建波"}'}
            ]
        ]
    )
    def test_002(self,data):
        '''用户创建2个聊天组以上'''
        res_all=read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all=[]
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        for i in range(5):
            response=my_request("post",self.url,data=data,headers=self.headers)
        data=read_mysql('select count(*) from chat_group_info where owner_id=68047730 ')[0]
        self.assertEqual(data,2)





    @parameterized.expand(
        [
            [
                {'url': '/api/groupChat/createGroup', 'params': '{"uid":"","groupName":"QA杨建波"}'}
            ]
        ]
    )
    def test_003(self,data):
        '''用户UID为空创建聊天组'''
        res_all=read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all=[]
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response=my_request("post",self.url,data=data,headers=self.headers)
        data=read_mysql('select * from chat_group_info where name="QA杨建波"')
        self.assertEqual(data,None)

    @parameterized.expand(
        [
            [
                {'url': '/api/groupChat/createGroup', 'params': '{"uid":"111111111","groupName":"QA杨建波"}'}
            ]
        ]
    )
    def test_004(self,data):
        '''用户UID非法无效创建聊天组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response = my_request("post", self.url, data=data, headers=self.headers)
        data = read_mysql('select * from chat_group_info where name="QA杨建波" and owner_id=68047730')
        self.assertEqual(data, None)




    @parameterized.expand(
        [
            [
               {'url': '/api/groupChat/createGroup', 'params': '{"uid":"68047730","groupName":""}'}
            ]
        ]
    )
    def test_005(self,data):
        '''聊天组名称为空创建聊天组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response = my_request("post", self.url, data=data, headers=self.headers)
        data = read_mysql('select * from chat_group_info where owner_id=68047730 and name=""')
        self.assertEqual(data, None)




    @parameterized.expand(
        [
            [
                {'url': '/api/groupChat/createGroup', 'params': '{"uid":"68047730","groupName":"yangjianbowanbatesttesttest"}'}
            ]
        ]
    )
    def test_006(self,data):
        '''聊天组名称长度为超长字符创建聊天组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response = my_request("post", self.url, data=data, headers=self.headers)
        data = read_mysql('select * from chat_group_info where owner_id=68047730 and name="yangjianbowanbatesttesttest"')
        self.assertEqual(data, None)



    @parameterized.expand(
        [
            [
                {'url': '/api/groupChat/createGroup','params': '{"uid":"68047730","groupName":" "}'}
            ]
        ]
    )
    def test_007(self,data):
        '''聊天组名称长度为空格创建聊天组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response = my_request("post", self.url, data=data, headers=self.headers)
        data = read_mysql(
            'select * from chat_group_info where owner_id=68047730 and name=" "')
        self.assertEqual(data, None)




    @parameterized.expand(
        [
            [
                {'url': '/api/groupChat/createGroup', 'params': '{"uid":"68047730","groupName":"@$#%^_^\n\s\"}'}
            ]
        ]
    )
    def test_008(self, data):
        '''聊天组名称为特殊字符创建聊天组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        response = my_request("post", self.url, data=data, headers=self.headers)
        data = read_mysql('select * from chat_group_info where owner_id=68047730 and name="@$#%^_^\n\s\"')
        self.assertEqual(data, None)



    ####删除聊天组######
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/removeGroup",'params':'{"uid":"68047730","groupId":"ID"}'}
            ]
        ]
    )
    def test_009(self,data):
            '''用户正常删除聊天组'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('QA玩吧')
            params=eval(data.get('params'))
            params['groupId']=id
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql('select * from chat_group_info where owner_id=68047730 and name="QA玩吧"')
            self.assertEqual(res,None)




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/removeGroup",'params':'{"uid":"","groupId":"ID"}'}
            ]
        ]
    )
    def test_010(self,data):
            '''用户UID参数为空删除聊天组'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('8888')
            params=eval(data.get('params'))
            params['groupId']=id
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql('select * from chat_group_info where owner_id=68047730 and name="8888"')
            self.assertNotEqual(res,None)




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/removeGroup",'params':'{"uid":"77338973","groupId":"ID"}'}
            ]
        ]
    )
    def test_011(self,data):
            '''非群主删除聊天组'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('8888')
            params=eval(data.get('params'))
            params['groupId']=id
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql('select * from chat_group_info where owner_id=68047730 and name="8888"')
            self.assertNotEqual(res,None)



    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/removeGroup",'params':'{"uid":"77338973","groupId":"ID"}'}
            ]
        ]
    )
    def test_012(self,data):
            '''groupId为空删除聊天组'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('8888')
            params=eval(data.get('params'))
            params['groupId']=""
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql('select * from chat_group_info where owner_id=68047730 and name="8888"')
            self.assertNotEqual(res,None)




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/removeGroup",'params':'{"uid":"77338973","groupId":"ID"}'}
            ]
        ]
    )
    def test_013(self,data):
            '''groupId不存在删除聊天组'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('8888')
            params=eval(data.get('params'))
            params['groupId']=88888888
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql('select * from chat_group_info where owner_id=68047730 and name="8888"')
            self.assertNotEqual(res,None)




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/removeGroup",'params':'{"uid":"77338973","groupId":"ID"}'}
            ]
        ]
    )
    def test_014(self,data):
            '''groupId参数数据类型非法删除聊天组'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('8888')
            params=eval(data.get('params'))
            params['groupId']=-1
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            res=read_mysql('select * from chat_group_info where owner_id=68047730 and name="8888"')
            self.assertNotEqual(res,None)


        #####获取指定群组信息######

    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupInfo",'params':'{"uid":"68047730","groupId":"ID"}'}
            ]
        ]
    )
    def test_015(self,data):
            '''用户正常获取指定聊天组信息'''
            res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
            list_all = []
            for list in res_all:
                list_all.append(list[0])
            for list in list_all:
                self.remove_chatgroup(list)
            id=self.add_chatgroup('8888')
            params=eval(data.get('params'))
            params['groupId']=id
            params=json.dumps(params)
            data['params']=params
            response=my_request('post',self.url,data=data,headers=self.headers)
            self.assertIn('id',str(response))
            self.assertIn('uid',str(response))
            self.assertIn('ownerId',str(response))



    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupInfo", 'params': '{"uid":"","groupId":"ID"}'}
            ]
        ]
    )
    def test_016(self, data):
        '''用户UID参数为空获取指定聊天组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = id
        params = json.dumps(params)
        data['params'] = params
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id', str(response))
        self.assertNotIn('uid', str(response))
        self.assertNotIn('ownerId', str(response))





    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupInfo", 'params': '{"uid":"666666666666","groupId":"ID"}'}
            ]
        ]
    )
    def test_017(self, data):
        '''用户UID参数不存在获取指定聊天组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = id
        params = json.dumps(params)
        data['params'] = params
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id', str(response))
        self.assertNotIn('uid', str(response))
        self.assertNotIn('ownerId', str(response))





    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupInfo", 'params': '{"uid":"68047730","groupId":"ID"}'}
            ]
        ]
    )
    def test_018(self, data):
        '''groupId参数为空获取指定聊天组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = ""
        params = json.dumps(params)
        data['params'] = params
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id', str(response))
        self.assertNotIn('uid', str(response))
        self.assertNotIn('ownerId', str(response))




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupInfo", 'params': '{"uid":"68047730","groupId":"ID"}'}
            ]
        ]
    )
    def test_019(self, data):
        '''groupId参数不存在获取指定聊天组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = "55555"
        params = json.dumps(params)
        data['params'] = params
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id', str(response))
        self.assertNotIn('uid', str(response))
        self.assertNotIn('ownerId', str(response))




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupInfo", 'params': '{"uid":"68047730","groupId":"ID"}'}
            ]
        ]
    )
    def test_020(self, data):
        '''groupId参数为非法数值获取指定聊天组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = "-1"
        params = json.dumps(params)
        data['params'] = params
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id', str(response))
        self.assertNotIn('uid', str(response))
        self.assertNotIn('ownerId', str(response))




    ###批量获取群组信息########
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupList", 'params': '{"uid":"68047730"}'}
            ]
        ]
    )
    def test_021(self, data):
        '''用户正确批量获取群组信息'''
        res_all = read_mysql2('select group_id from chat_group_user where uid=68047730 ')
        groupid=[]
        groupId=[]
        for list in res_all:
            groupid.append(list[0])
        resopnse=my_request('psot',self.url,data=data,headers=self.headers)
        for list in resopnse.get('data'):
            groupId.append(list.get('id'))
        self.assertEqual(len(groupId),len(groupid))
        self.assertIn('name',str(resopnse))
        self.assertIn('ownerId',str(resopnse))










    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupList", 'params': '{"uid":""}'}
            ]
        ]
    )
    def test_023(self, data):
        '''用户UID参数为空批量获取群组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id1=self.add_chatgroup('8888')
        id2=self.add_chatgroup('9999')
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id',str(response))
        self.assertNotIn('name',str(response))




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/getGroupList", 'params': '{"uid":"26422161"}'}
            ]
        ]
    )
    def test_024(self, data):
        '''用户UID参数无效批量获取群组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id1=self.add_chatgroup('8888')
        id2=self.add_chatgroup('9999')
        response = my_request('post', self.url, data=data, headers=self.headers)
        self.assertNotIn('id',str(response))
        self.assertNotIn('name',str(response))



    #####修改群组信息#####
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup", 'params': '{"uid":"68047730","groupId":"chat_id","groupName":"666"}'}
            ]
        ]
    )
    def test_025(self, data):
        '''群主正常修改群组名称信息'''
        groupname=''.join(random.sample(string.digits,3))
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params['groupName']=groupname
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        name=read_mysql('select name from chat_group_info where owner_id=68047730')[0]
        self.assertEqual(name,groupname)




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup", 'params': '{"uid":"68047730","groupId":"chat_id","groupName":"666666666666666666666666666666666666666"}'}
            ]
        ]
    )
    def test_026(self, data):
        '''群主修改群组名称信息超过32位字符'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        name=read_mysql('select name from chat_group_info where owner_id=68047730')[0]
        self.assertNotEqual(name,'666666666666666666666666666666666666666')





    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup",
                 'params': '{"uid":"68047730","groupId":"chat_id","groupName":""}'}
            ]
        ]
    )
    def test_027(self, data):
        '''群主修改群组名称信息为空'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = id
        params = json.dumps(params)
        data['params'] = params
        response = my_request('post', self.url, data=data, headers=self.headers)
        name = read_mysql('select name from chat_group_info where owner_id=68047730')[0]
        self.assertNotEqual(name, '')




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup",
                 'params': '{"uid":"68047730","groupId":"chat_id","groupName":" "}'}
            ]
        ]
    )
    def test_028(self, data):
        '''群主修改群组名称信息为空格'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = id
        params = json.dumps(params)
        data['params'] = params
        print(data)
        response = my_request('post', self.url, data=data, headers=self.headers)
        name = read_mysql('select name from chat_group_info where owner_id=68047730')[0]
        self.assertNotEqual(name," ")





    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup",
                 'params': '{"uid":"26422161","groupId":"chat_id","groupName":"666"}'}
            ]
        ]
    )
    def test_029(self, data):
        '''非群主修改群组信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id = self.add_chatgroup('8888')
        params = eval(data.get('params'))
        params['groupId'] = id
        params = json.dumps(params)
        data['params'] = params
        print(data)
        response = my_request('post', self.url, data=data, headers=self.headers)
        name = read_mysql('select name from chat_group_info where owner_id=68047730')[0]
        self.assertNotEqual(name,"666")



    #####修改用户群组头像########
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup", 'params': '{"uid":"77338973","groupId":"chat_id","avatar":"666"}'}
            ]
        ]
    )
    def test_025(self, data):
        '''群主正常修改群组头像信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=77338973 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        name=read_mysql('select avatar from chat_group_info where owner_id=77338973')[0]
        self.assertEqual(name,'666')



    ###修改群组简介######
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup", 'params': '{"uid":"68047730","groupId":"chat_id","summary":"777"}'}
            ]
        ]
    )
    def test_026(self, data):
        '''群主正常修改群组简介信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        summary=read_mysql('select summary from chat_group_info where owner_id=68047730')[0]
        self.assertEqual(summary,'777')



    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/updateGroup", 'params': '{"uid":"68047730","groupId":"chat_id","summary":"rrrrrrtttttttttttttt55555555555555555555555555hhhhhhhhhhhhhhhhhhhhhhhhhhhhhfffffffffffffff66666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777778888888888888uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"}'}
            ]
        ]
    )
    def test_027(self, data):
        '''群组简介信息为超长字符群主修改群组简介信息'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        summary=read_mysql('select summary from chat_group_info where owner_id=68047730')[0]
        self.assertNotEqual(summary,'rrrrrrtttttttttttttt55555555555555555555555555hhhhhhhhhhhhhhhhhhhhhhhhhhhhhfffffffffffffff66666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777778888888888888uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')






    #####邀请用户加入群组########
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/inviteUser", 'params': '{"uid":"68047730","groupId":"","toUids":"toUids"}'}
            ]
        ]
    )
    def test_028(self, data):
        '''群主正常邀请好友加入群组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params['toUids']='["77338973"]'
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        code=response.get('code')
        data=response.get('data')
        self.assertEqual(code,0)
        self.assertEqual(data,{})




    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/inviteUser", 'params': '{"uid":"77338973","groupId":"","toUids":"toUids"}'}
            ]
        ]
    )
    def test_029(self, data):
        '''非群主邀请好友加入群组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params['toUids']='["54869969"]'
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        code=response.get('code')
        data=response.get('desc')
        self.assertEqual(code,-1)
        self.assertEqual(data,'此功能暂时只对房主开放~')





    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/inviteUser", 'params': '{"uid":"68047730","groupId":"","toUids":"toUids"}'}
            ]
        ]
    )
    def test_030(self, data):
        '''邀请非好友加入群组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params['toUids']='["89540643"]'
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        code=response.get('code')
        data=response.get('desc')
        self.assertEqual(code,-1)
        self.assertEqual(data,'对方不是你好友')





    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/inviteUser", 'params': '{"uid":"68047730","groupId":"","toUids":"toUids"}'}
            ]
        ]
    )
    def test_031(self, data):
        '''群组ID不存在邀请好友加入群组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']='8888888'
        params['toUids']='["64483773"]'
        params=json.dumps(params)
        data['params']=params
        response = my_request('post', self.url, data=data, headers=self.headers)
        code=response.get('code')
        data=response.get('desc')
        self.assertEqual(code,-1)
        self.assertEqual(data,'服务异常')
    #


    #####申请加入群组######
    @parameterized.expand(
        [
            [
                {"url": "/api/groupChat/applyJoin", 'params': '{"uid":"77338973","groupId":""}'}
            ]
        ]
    )
    def test_032(self, data):
        '''正常申请加入群组'''
        res_all = read_mysql2('select id from chat_group_info where owner_id=68047730 ')
        list_all = []
        for list in res_all:
            list_all.append(list[0])
        for list in list_all:
            self.remove_chatgroup(list)
        id=self.add_chatgroup('8888')
        params=eval(data.get('params'))
        params['groupId']=id
        params=json.dumps(params)
        data['params']=params
        response=my_request('post',self.url,data=data,headers=self.headers)
        code=response.get('code')
        data=response.get('data')
        self.assertEqual(code,0)
        self.assertEqual(data,{})




if __name__ == '__main__':
    unittest.main()