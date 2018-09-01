# # 作业1：
import string
# #使用in或者not in方法把下面列表中的重复的元素去重并返回结果，并且提取重复的元素返回结果
# a=[1,2,3,4,5,1,2,3,4,5,6,7,8,9,10,10]
# # # 分析：使用not in 或in 方法提取重复的元素返回，并且返回去重后的列表
# def get_reelment():
#     r=[]
#     b=[]
#     for i in a:
#         #去重，挨个元素判断添加，如果元素在里面就不添加
#         if i not in b:
#             b.append(i)
#         #提取重复的元素
#         else:
#             r.append(i)
#     return r,b
#
#
#
#
# # # 作业2：
# # # 判断下面字典在一维是否存在jiaming,若果不存在则添加"jiaming":{'age': '17','courty': '尼日利亚','room': '2套','money':150000}
# # # 再判断二维中谁没有money,如果没有给她添加moeny 200000
#

def handle_dict():
    cities = {
        'hongxin': {
            'age': '19',
            'courty': '中国',
            'room': '2套',
            'money': 100000
        },
        'xiaokang': {
            'country': '美国',
            'age': "16",
            'room': '3套',
            'money': 500000
        },
        'chenxin': {
            'country': '法国',
            'age': '18',
            'room': None
        }
    }
    key=[]
    value=[]
    #判断jiaming在不在一维的字典里
    if 'jiaming' in cities:
        pass
    #如果不在就添加jiaming属性
    else:
        cities['jiaming']={'age': '17','courty': '尼日利亚','room': '2套','money':150000}
    #取出所有key值
    for k in cities:
        key.append(k)
    #取出所有的value值
    for v in key:
        value.append(cities.get(v))
    #因为value是字典,所以对每个value进行判断money在不在字典里
    for v in value:
        #如果在就pass
        if 'money' in v:
            continue
        #如果不在就添加money=200000
        else:
            v['money']=200000
    print(value)
    new_dict=dict(zip(key,value))
    return new_dict
# d=handle_dict()
#
# #作业3写一个校验密码合法性程序，要求密码大于5位且小于10位，且有包含数字和大小写字母
# # 分析：从键盘输入一个密码进行密码合法性校验，合法性密码要求有数字，有大小写字母，且长度大于5位小于10位
# # 1：首先判断密码是否为空，然后再判断密码长度，再判断密码是否包含大小写字母及数字
# def check_passwd():
#     import string
#     #对键盘输入的字符进行去空格处理
#     passwd=input('请输入要校验的密码:').strip()
#     if passwd!='':
#         if len(passwd)>5 and len(passwd)<=10:
#             #取出所有的数字
#             digist=string.digits
#             #取出所有的小写字母
#             lower=string.ascii_lowercase
#             #取出所有的大写字母
#             upper=string.ascii_uppercase
#             #定义数字出现的次数
#             digist_count=0
#             #定义小写字母出现的次数
#             lower_count=0
#             #定义大写字母出现的次数
#             upper_count=0
#             #对键入的密码（字符串）循环
#             b='dsfSr12'
#             for p in passwd:
#                 #判断密码中是否有数字
#                 if p in digist:
#                     digist_count+=1
#                 #判断密码中是否有小写字母
#                 if p in lower:
#                     lower=lower+1
#                     # lower_count+=1
#                 #判断密码中是否有大写字母
#                 if p in upper:
#                     upper_count+=1
#             #判断密码中出现数字的次数和小写字母的数字以及大写字母出现的次数
#             if digist_count>0 and lower_count>0 and upper_count>0:
#                 print('该密码通过校验！')
#             else:
#                 print('该密码不含大写字母或小写字母或数字!请检查~~')
#
#         else:
#             print('你输入的密码长度不符合密码规范，请重新输入！')
#     else:
#         print('你输入的密码不能为空!')


