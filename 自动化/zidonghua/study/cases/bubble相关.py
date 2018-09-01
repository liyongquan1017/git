import unittest
from lib.tools import my_request
from nose_parameterized import parameterized
import json

class bubble_test(unittest.TestCase):
    def setUp(self):
        self.url = 'http://testapitest.wb-intra.com/api/test'
    @classmethod
    def tearDownClass(cls):
        print("执行完成bubble微服务相关接口测试用例")
    @parameterized.expand(
        [
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730"}'},
                0
            ]
        ]
    )
    def test_001(self,headers,data,hope1):
        '''正常获取气泡列表信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)


    @parameterized.expand(
        [#用户UID参数为空获取气泡列表信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":""}'},
                3
            ]
        ]
    )
    def test_002(self,headers,data,hope1):
        '''用户UID参数为空获取气泡列表信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)

    @parameterized.expand(
        [#指定气泡ID正常获取气泡信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730","batchBubbleId":"1"}'},
                0
            ]
        ]
    )
    def test_003(self,headers,data,hope1):
        '''指定气泡ID正常获取气泡信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)

    @parameterized.expand(
        [#指定气泡ID正常获取气泡信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730","batchBubbleId":"1"}'},
                0
            ]
        ]
    )
    def test_004(self,headers,data,hope1):
        '''指定气泡ID正常获取气泡信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)


    @parameterized.expand(
        [#指定气泡ID，入参非法获取气泡信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730","batchBubbleId":"xfsfsdf"}'},
                30101
            ]
        ]
    )
    def test_005(self,headers,data,hope1):
        '''指定气泡ID，入参非法获取气泡信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)


    @parameterized.expand(
        [#指定气泡ID，入参为空获取气泡信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730","batchBubbleId":""}'},
                0
            ]
        ]
    )
    def test_006(self,headers,data,hope1):
        '''指定气泡ID，入参为空获取气泡信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)


    @parameterized.expand(
        [#指定气泡ID，入参信息不存在获取气泡信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730","batchBubbleId":"66666"}'},
                {}
            ]
        ]
    )
    def test_007(self,headers,data,hope1):
        '''指定气泡ID，入参信息不存在获取气泡信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        self.assertEqual(response.get('data'),hope1)



    @parameterized.expand(
        [#指定气泡ID，入参信息格式不正确获取气泡信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getBubbleInfo','params': '{"uid":"68047730","batchBubbleId":"1，2，3"}'},
                30101
            ]
        ]
    )
    def test_008(self,headers,data,hope1):
        '''指定气泡ID，入参格式不正确获取气泡信息'''
        response=my_request("post",self.url,data=data,headers=headers)
        code=response.get('code')
        self.assertEqual(code,hope1)


    ####获取用户当前的气泡使用信息######
    @parameterized.expand(
        [  # 正常获取用户当前的气泡使用信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getUserBubbleInfo', 'params': '{"uid":"68047730"}'},
                0
            ]
        ]
    )
    def test_009(self, headers, data, hope1):
        '''正常获取用户当前的气泡使用信息'''
        response = my_request("post", self.url, data=data, headers=headers)
        code = response.get('code')
        self.assertEqual(code, hope1)



    ####获取用户当前的气泡使用信息######
    @parameterized.expand(
        [  # 用户UID参数为空获取用户当前的气泡使用信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getUserBubbleInfo', 'params': '{"uid":""}'},
                3
            ]
        ]
    )
    def test_010(self, headers, data, hope1):
        '''用户UID参数为空获取用户当前的气泡使用信息'''
        response = my_request("post", self.url, data=data, headers=headers)
        code = response.get('code')
        self.assertEqual(code, hope1)


    @parameterized.expand(
        [  # 用户UID参数为空格取用户当前的气泡使用信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getUserBubbleInfo', 'params': '{"uid":" "}'},
                3
            ]
        ]
    )
    def test_011(self, headers, data, hope1):
        '''用户UID参数为空格获取用户当前的气泡使用信息'''
        response = my_request("post", self.url, data=data, headers=headers)
        code = response.get('code')
        self.assertEqual(code, hope1)


    @parameterized.expand(
        [  # 用户UID参数非法格取用户当前的气泡使用信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getUserBubbleInfo', 'params': '{"uid":"sdfsdfer"}'},
                3
            ]
        ]
    )
    def test_012(self, headers, data, hope1):
        '''用户UID参数非法获取用户当前的气泡使用信息'''
        response = my_request("post", self.url, data=data, headers=headers)
        code = response.get('code')
        self.assertEqual(code, hope1)


    @parameterized.expand(
        [  # 用户UID参数不存在格取用户当前的气泡使用信息
            [
                {'content-type': "application/x-www-form-urlencoded"},
                {'url': '/api/v2/bubble/getUserBubbleInfo', 'params': '{"uid":"11111111111111111"}'},
                3
            ]
        ]
    )
    def test_013(self, headers, data, hope1):
        '''用户UID参数不存在获取用户当前的气泡使用信息'''
        response = my_request("post", self.url, data=data, headers=headers)
        code = response.get('code')
        self.assertEqual(code, hope1)

if __name__ == '__main__':
    unittest.main()

