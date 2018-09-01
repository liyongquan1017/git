import time
coding='utf8'
from lib.tools import my_request,read_mysql2
import json
import pymysql
import sys
import os
import random,string
from nose_parameterized import parameterized
import threading

def delete_personal_information():
    # id = self.get_personal_information_id()
    id=675
    params = {"uid": "68047730"}
    params['id'] = id
    params=json.dumps(params)
    data={'url': '/api/user/customInfo/delete'}
    data['params']=params
    url='http://testapitest.wb-intra.com/api/test'
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response=my_request("post",url,data=data,headers=headers)
    print(response)

def get_personal_information_id():
    data={'url':'/api/user/customInfo/add',"params":'{"uid":"68047730","key":"杨建波测试","value":"杨建波测试"}'}
    url = 'http://testapitest.wb-intra.com/api/test'
    headers = {'content-type': "application/x-www-form-urlencoded"}
    response = my_request("post", url, data=data, headers=headers)
    id=response.get('id')
    return id


# def delete_personal_information():
#     id=get_personal_information_id()
#     params={"uid":"68047730"}
#     params['id']=id
#     params=json.dumps(params)
#     url = 'http://testapitest.wb-intra.com/api/test'
#     headers = {'content-type': "application/x-www-form-urlencoded"}
#     data={'url':'/api/user/customInfo/delete'}
#     data['params']=params
#     response = my_request("post", url, data=data, headers=headers)
# # delete_personal_information()
# c=get_personal_information_id()
# print(c)
# id=get_personal_information_id()
# print(id)
# c=''.join(random.sample(string.ascii_letters,12))
# print(c)

# data=''.join(string.punctuation)
# print(data)

# def remove_chatgroup(id):
#     # 删除解散群组
#     url='http://testapitest.wb-intra.com/api/test'
#     headers = "{'content-type': 'application/x-www-form-urlencoded'}"
#     data = {"url": "/api/groupChat/removeGroup"}
#     params = {"uid": "68047730"}
#     params['groupId'] = id
#     params=json.dumps(params)
#     data['params']=params
#     print(data)
#     response=my_request("post",url,data=data,headers=headers)
#     print(response)
# remove_chatgroup(5)
# y={
#     "code": 0,
#     "msg": "success",
#     "data": {
#         "bannerList": {
#             "showType": 1,
#             "showMap": {
#                 "banner": {
#                     "bannerList": [
#                         {
#                             "imgUrl": "https://qiniustatic.wodidashi.com/newdraw11.png",
#                             "jumpUrl": "wanba://webview/inner?_info=eyJ1cmwiOiJodHRwOi8vd3d3Lm1vcWl3YW5iYS5jb20vIn0="
#                         },
#                         {
#                             "imgUrl": "https://qiniustatic.wodidashi.com/newdraw11.png",
#                             "jumpUrl": "wanba://webview/inner?_info=eyJ1cmwiOiJodHRwOi8vd3d3Lm1vcWl3YW5iYS5jb20vIn0="
#                         }
#                     ],
#                     "duration": 3
#                 }
#             }
#         },
#         "hasMore": "1",
#         "list": [
#             {
#                 "showType": 2,
#                 "showMap": {
#                     "roomId": "3776",
#                     "roomUid": "69586444",
#                     "gameTypeId": 2000,
#                     "subTypeId": 0,
#                     "title": "hehe",
#                     "coverImageSmall": "http://qiniu.wodidashi.com/head/lmWz0xCIwmGqg?imageView/2/w/200/h/200",
#                     "coverImageLarge": "http://qiniu.wodidashi.com/head/lmWz0xCIwmGqg",
#                     "followerCount": 0,
#                     "passwordEnable": 0,
#                     "password": "",
#                     "background": "",
#                     "state": 1,
#                     "accessState": 0,
#                     "tagId": 0,
#                     "subject": "来玩吧",
#                     "liveType": 0,
#                     "recordId": 0,
#                     "startTime": 1525950686000,
#                     "endTime": 1525948491000,
#                     "pushFriend": 0,
#                     "pushFollower": 0,
#                     "createTime": 1525948491000,
#                     "username": "黄雄",
#                     "gender": "m",
#                     "iconImg": "http://qiniu.wodidashi.com/head/lmWz0xCIwmGqg?imageView/2/w/200/h/200"
#                 }
#             }
#         ]
#     }
# }
# rommID=y.get('data').get('list')[0].get('showMap').get('roomId')
# roomUid=y.get('data').get('list')[0].get('showMap').get('roomUid')
#
# print(rommID)
# print(roomUid)
# def get_slave():
#     url = 'http://testapitest.wb-intra.com/api/test'
#     headers = {'content-type': "application/x-www-form-urlencoded"}
#     data={'url':'/api/v2/slave/collectBonus','params':'{"uid":"68047730","ownerUid":"68047730","slaveUid":"26422161"}'}
#     response = my_request("post",url,data=data, headers=headers)
#     print(response)
# get_slave()

def get_ShopHome():
    url='http://testapitest.wb-intra.com/api/test'
    headers = {'content-type': "application/x-www-form-urlencoded"}
    data={'url':" /api/v2/shop/getShopHome",'params':'{"uid":"68047730","source":0}'}
    response=my_request("post",url,data=data,headers=headers)
    print(response)
def follow_room():
    url = 'http://testapitest.wb-intra.com/api/test'
    headers={'content-type': "application/x-www-form-urlencoded"}
    data={"url":"/v3/liveroom/follow/setUserFollowRoom","params":'{"uid":"77338973","roomUid":"68047730","roomId":"307185"}'}
    response=my_request('post',url,data=data,headers=headers)
    print(response)


def submit_report():
    url = 'http://testapitest.wb-intra.com/api/test'
    headers={'content-type': "application/x-www-form-urlencoded"}
    data={"url":"/v3/liveroom/report/submit","params":'{"uid": "24664041","roomUid":"68047730","roomId":"307185","option":"ZKAFL-live"}'}
    response=my_request('post',url,data=data,headers=headers)
# submit_report()
# def report():
#     for list in range(100):
#         submit_report()
#
# t=threading.Thread(target=report())
# t.start()





def read_mysql(sql):
    try:
        connect = pymysql.connect(host='127.0.0.1', port=3306, user='spy', passwd='hexenn',charset='utf8', db='spy')
        cur=connect.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            print('执行数据库语句失败，错误是%s' %e)
        res=cur.fetchall()[0][0]
        return res
    except Exception as e:
        # print('连接数据库出错了，错误是%s' %e)
        cur.close()
        connect.close()


def get_musicId():
    url='http://testapitest.wb-intra.com/api/test'
    headers={'content-type': "application/x-www-form-urlencoded"}
    data={"url": "/api/getMusicList","params": '{"uid":"68047730"}'}
    response=my_request('post',url,data=data,headers=headers)
    for list in response:
        ID=list['id']
        if ID=='128':
            print(list['price'])


def get_price(uid):
    url = 'http://testapitest.wb-intra.com/api/test'
    data = {"url": "/api/getScoreAndMoney", "params": '{"uid":"uid"}'}
    headers = {'content-type': "application/x-www-form-urlencoded"}
    params = eval(data.get('params'))
    params['uid'] = uid
    params = json.dumps(params)
    data['params'] = params
    response = my_request('post', url, data=data, headers=headers)
    print(response)
    diamond = response.get('diamondCount')
    money = response.get('money')
    return [int(money), int(diamond)]
# url='http://testapitest.wb-intra.com/api/test'
# headers = {'content-type': "application/x-www-form-urlencoded"}
# data={"url":"/api/v2/vipRoom/getRoomInfo",'params':'{ "uid": "68047730","roomId":"308346"}'}
# response=my_request('post',url,data=data,headers=headers)
# if 'puzzle_type_name' in str(response):
#     print('yyy')
# else:print('cccc')

def delete_feed(uid):
    uid=str(uid)
    url = 'http://testapitest.wb-intra.com/api/test'
    headers = {'content-type': "application/x-www-form-urlencoded"}
    res=read_mysql2('select * from feed_source where source_owner_id=%s'%uid)
    all_feed=[]
    for list in res:
        feedid=str(list[1])
        sourceType=str(list[2])
        sourceId=str(list[4])
        all_feed.append([feedid,sourceType,sourceId])
    for list in all_feed:
        data = {"url": "/api/v2/feed/deleteFeed",'params': '{"uid":"40846498","feedOwnerId":"40846498","feedId":"21697","sourceId":"6787","sourceType":1}'}
        params = eval(data.get('params'))
        params['uid']=uid
        params['feedOwnerId']=uid
        params['feedId']=list[0]
        params['sourceType']=list[1]
        params['sourceId']=list[2]
        params=json.dumps(params)
        data['params']=params
        response=my_request('post',url,data=data,headers=headers)
    print('删除完该用户所有的feed')

if __name__ == '__main__':
    users = ['46223077', '70622779', '25377759', '31144713', '37043283', '13598133', '52862935', '31901030', '71846024','48988137', '81366631', '74967153', '67473865', '46223077', '70622779', '12983276', '37342558', '47381356','21879444', '59391617', '54869969', '14596652','37043284']
    users=set(users)
    for list in users:
        delete_feed(list)

