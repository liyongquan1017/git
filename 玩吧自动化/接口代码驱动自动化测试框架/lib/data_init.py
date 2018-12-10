from lib.tools import my_request
import json

class data(object):
    def __init__(self):
        self.msurl = 'http://testapitest.wb-intra.com/ms/test'
        self.apiurl='http://testapitest.wb-intra.com/api/test'
        self.headers={'content-type': "application/x-www-form-urlencoded"}

    ###添加金币
    def add_money(self,uid,count):
        uid=str(uid)
        count=str(count)
        data={"url":"user.addMoney","host":"user.wb-ms.com",'params':'{"uid":"34853781","count":"4","reason":"2","misc":"2"}'}
        params=eval(data.get('params'))
        params['uid']=uid
        params['count']=count
        data['params']=json.dumps(params)
        response=my_request('post',self.msurl,data=data,headers=self.headers)
        print(response)


    ####添加钻石
    def add_diamond(self,uid,count):
        uid=str(uid)
        count=str(count)
        data={"url":"currency.addUserDiamond","host":"currency.wb-ms.com",'params':'{"uid":"34853781","count":"4","add_reason":"1","payType":"apple","add_type":"sandbox"}'}
        params=eval(data.get('params'))
        params['uid']=uid
        params['count']=count
        data['params']=json.dumps(params)
        response=my_request('post',self.msurl,data=data,headers=self.headers)
        print(response)


    ####获取用户钻石，金币,身价(可根据需求扩展)
    def get_price(self,uid):
        uid=str(uid)
        data={"url":"/v3/home/userInfo",'params':'{"__t_":"71117757"}'}
        params=eval(data.get('params'))
        params['__t_']=uid
        data['params']=json.dumps(params)
        res=my_request('post',self.apiurl,data=data,headers=self.headers)
        money=res.get('data').get('data').get('money')
        diamond=res.get('data').get('data').get('diamond')
        price=res.get('data').get('data').get('price')
        return [money,diamond,price]


    #####重置用户钻石为0
    def reset_diamond(self, uid):
        uid = str(uid)
        url = 'http://testapitest.wb-intra.com/ms/test'
        value = self.get_price(uid)[0]
        data = {"url": "currency.reduceUserDiamond", "host": "currency.wb-ms.com", 'params': '{"uid":"77338973"}'}
        params = eval(data.get('params'))
        params['uid'] = uid
        params['count'] = value
        params['orderId'] = 'yangjianbo'
        params['remark'] = '备注'
        params['pay_type'] = 'ali'
        params['reduce_reason'] = '1'
        params['app_id'] = '10002'
        params['app_version'] = '90000'
        params['misc'] = 'slave-compensate'
        params['needReset'] = 'true'
        data['params'] = json.dumps(params)
        response = my_request('post', url, data=data, headers=self.headers)
        print(response)

    ####重置个人用户金币为0
    def reset_money(self, uid):
        uid = str(uid)
        value = self.get_price(uid)[0]
        data = {"url": "user.deductMoney", "host": "user.wb-ms.com",'params': '{"uid":"77338973","count":"37","reason":"slave-compensate","misc":"slave-compensate","needReset":"true"}'}
        params = eval(data.get('params'))
        params['uid'] = uid
        params['count'] = value
        params['reason'] = 'slave-compensate'
        params['misc'] = 'slave-compensate'
        params['needReset'] = 'true'
        data['params'] = json.dumps(params)
        response = my_request('post',self.msurl,data=data, headers=self.headers)
        print(response)

    #####添加道具
    def add_prop(self, uid, propId,count):
        uid = str(uid)
        propId = str(propId)
        count=str(count)
        url = 'http://testapitest.wb-intra.com/ms/test'
        data = {"url": "prop.addUserProp", "host": "prop.wb-ms.com",'params': '{"uid": "84348841","location": "staff_added","propId": "1","propCount": "2"}'}
        params = eval(data.get('params'))
        params['uid'] = uid
        params['propId'] = propId
        params['propCount'] = count
        data['params'] = json.dumps(params)
        response = my_request('post', url, data=data, headers=self.headers)
        print(response)





