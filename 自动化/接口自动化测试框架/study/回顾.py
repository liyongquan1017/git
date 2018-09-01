
import random
import string
import json
# # def 封装函数
# def sum():
#     a=8+9
#     return a
#
# c=sum()
# print(c)


# class() 类的封装
# class maiche():
#     def xuejiaozhao(self):
#         print('我去学驾照了')
#
#     def buy_cay(self):
#         print('我去买车了')
#
#
#
# class yeye():
#     def a(self):
#         print('我爷爷有100块钱')
# class baba(yeye):
#     def b(self):
#         print('我爸爸有一套房子')
# class wo(baba):
#     pass
#
# if __name__ == '__main__':
#     y=baba()
#     y.a()

# 列表 []
#列表是通过下标来取值的
#元素之间是以逗号来分开的
#b.append('car')增加元素
#type查看数据类型
# a=[1,2,3,4,5,6]
# b=['yangjianbo','user','passwd','msg','age','8888']
# b.append('car')
# b.remove('8888')
# b.pop(0)
# print(b)
# 列表取值：
# for y in b:
#     print(y)

#字典取值是通过.get()方法来取值的
##for循环取得是字典的KEY值
# a={
#     'user':'jiaming',
#     'age':'20',
#     'height':'180CM',
#     'whgit':'70KG',
# }

# for k in a:
#     print(k)
# c=a.get('age')
# print(c)
# a['car']='3辆车'
# a['age']='16'
# a.pop('age')
# print(a)
# a['age']='19'
# print(a)
#
# a='杨建波'
# b='18岁'
# print('我的名字是%s，年龄是%s'%(a,b))
# for list in range(100):
#     if list%5==0 and list%3==0:
#         print(list)


# list=['user','name','age','heitht']
# list.insert(0,'hongxing')
# list.append('jiaming')
# list.pop(0)
# list.remove('user')
# print(list)
# print(list[1])

# a={"user":"yangjianbo","age":"18"}

# for jjj in a:
#     print(jjj)

# print(a.get('user'))
# key=a.keys()
# value=a.values()
# print(value)
# a['height']='171CM'
# a['user']='jiaming'
# a.pop('user')

# print(a)

# a=[1,2,3,2,3,4,5,6,4,6,4,5,6,7,2,4,6,7]
# b=list(set(a))
# print(b)
# print(type(b))


# user='佳明'
# age='18'
#
# for list in a:
#     print(list)
# print('我的名字是%s我今年已经%s岁了'%(user,age))
# a=[1,2,3,4,5,6,7]
# b='slakjgwieytwuahtlwaiytowa;jfowityyq5842tmlksgj9er'
# n=len(b)
# print(n)


# b=[1,2,3,'yangjianbo',{"user":"name"}]
# print(b)
# c=[1,2,3,4,[5,6,7,[8,9,10]]]
# print(c[4][3][1])

# jiaming={
#     'user':'jiaming',
#     'age':'20',
#     'height':'180CM',
#     'whgit':'70KG',
#     'room':{"北京":"3套房子","河北":"2套房子"}
# }
# key=jiaming.keys()
# value=jiaming.values()
# print(key)
# print(value)


# and(与的关系)or（或的关系） !（不是）
#
# for o in range(1,101):
#     if o%5==0 and o%3==0:
#         print(o)



# def a(sum1=1,sum2=23):
#     c=sum1+sum2
#     return c
#
# c=a()
# print(c)
# print(d)
# c='alskjfoiew'
# print(type(c))


# h=feilong.get('age')
# print(h)
def get_new_dicyt():
    feilong = {
        'user': 'jiaming',
        'age': '20',
        'height': '180CM',
        'whgit': '70KG',
        'car': "凯迪拉克"
    }
    key=[]
    value=[]
    for k in feilong:
        key.append(k)
    # print(key)
    for j in key:
        # print(j)
        value.append(feilong.get(j))

    new_dict=dict(zip(key,value))
    return new_dict





#
# v=['y','j','i','a','n','b','o']
# c="".join(v)
# print(c)
# print(type(c))

# c=random.sample(string.ascii_lowercase,5)
# a=''.join(c)
# print(a)

# b=random.choice(a)
# print(b)

def guess():
    e=random.randint(1,100)
    print(e)
    print('正确的数字是%s'%e)
    while True:
        value = input('请输入一个数')
        value = int(value)
        if value>e:
            print('你输入的数太大了，请重新输入')
        elif value<e:
            print('你输入的数太小了，请重新输入！')
        else:
            print('恭喜你中奖了！！')
            break




def card():
    num=input('请输入你要产生的身份证号码条数:')
    try:
        num=int(num)
        shengfen='11'
        area=['0101','0102','0103','0104','0105','0106','0107','0108','0109','0111','0221','0222','0223','0224','0226','0227','0228','0229']
        years=[]
        moths=[]
        days=[]
        ids=[]
        for y in range(1949,2019):
            years.append(str(y))
        for m in range(1,13):
            if m<10:
                new_m='0'+str(m)
                moths.append(new_m)
            else:
                moths.append(str(m))
        for d in range(1,31):
            if d<10:
                new_d='0'+str(d)
                days.append(new_d)
            else:
                days.append(str(d))
        for i in range(num):
            suiji = ''.join(random.sample(string.digits, 4))
            id=shengfen+random.choice(area)+random.choice(years)+random.choice(moths)+random.choice(days)+suiji
            ids.append(id)
        ids1=set(ids)
        return list(ids1)
    except Exception as e:
        print('请输入正确的数据类型!')



