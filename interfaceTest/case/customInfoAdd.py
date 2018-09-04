# -*- coding:utf-8 -*-
import unittest
from lib.tools import mySql
from lib.tools import myinterFace_request
class custominfo_add(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def test01(self):
        url = 'http://testapitest.wb-intra.com/api/test'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'params':'{"uid":"85637664","key":"饭量","value":"一碗米饭"}','url':'/api/user/customInfo/add'}
        myRe = myinterFace_request(url,data,headers)
        r = myRe.mfPost()
        print(r)


if __name__ == '__main__':
    unittest.main()