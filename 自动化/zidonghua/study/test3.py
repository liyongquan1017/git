import time
from lib.tools import read_mysql2,my_request
import json
import random
import string
def add_feed():
    users = ['46223077', '70622779', '25377759', '31144713', '37043283', '13598133', '52862935', '31901030', '71846024','48988137', '81366631', '74967153', '67473865', '46223077', '70622779', '12983276', '37342558','47381356','21879444','59391617','54869969','14596652']
    users=set(users)
    url = 'http://testapitest.wb-intra.com/api/test'
    headers = {'content-type': "application/x-www-form-urlencoded"}
    data = {"url": "/api/v2/feed/publishImage",'params': '{"uid":"68047730","url":"http://qiniu.wodidashi.com/picture/fyOqvTogDZbJX?imageView/2/w/300/h/300","message":"玩吧QA测试啦!!","topicId":"235","urlLarge":"http://qiniu.wodidashi.com/picture/fyOqvTogDZbJX"}'}
    value = 1
    for i in range(10):
        for list in users:
            params=eval(data.get('params'))
            params['uid']=list
            params['message']=value
            params=json.dumps(params)
            data['params']=params
            value+=1
            time.sleep(10)
            print(data)
            my_request('post',url,data=data,headers=headers)


b=''.join(random.sample(string.ascii_lowercase,25))
print(b)
print(type(b))