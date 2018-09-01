#数组格式,元素是以逗号来隔开区分
a=['a','b','c','d','aa','dddd','ccccccc','dsfewtr','tttt']
###数组的处理方法
###添加某个元素append
# a.append('d')
# index来找元素的下标
# print(a.index('dddd'))
#通过下标来删除某个元素
# del a[5]
# print(a)
# a.pop(5)
# print(a)
###通过元素名来删除某个元素
# a.remove('dddd')


# remove,del 两种方式删除元素，remove是通过元素名来删除元素，del是通过下标来删除元素


##字典，字典是以k-v的形式来表现的,他就是键值对
##type方法用来查看变量的数据类型
# ac=[]
# print(type(ac))
###isinstance来校验某个变量是不是指定的数据类型
# a=[]
# print(isinstance(a,list))

###字典的key值是通过循环来取的
###字典的value值是通过get方法来取的dict.get('key')
hongixng={
    'username':'hongxing',
    'age':'18',
    'height':'180',
    'wight':'70KG',
    'phone':'123456789',
    'room':'2套'
}
# hongixng['room']='3套'
# hongixng['car']='1辆车'
# print(hongixng)
####通过循环来取字典的key值
# ###只要数据类型里有元素且有下标的都可以进行元素的遍历循环
##通过循环来获取KEY值
# for c in hongixng:
#     print(c)
###通过.get方法来获取value值
# print(hongixng.get('room'))
# key=[]
# value=[]
# for pp in hongixng:
#     # print(pp)
#     key.append(pp)
# for bb in key:
#     value.append(hongixng.get(bb))
##dict(zip(list1,list2)把两个列表组成一个字典（list1为key,list2为value）
# yy=dict(zip(key,value))
# print(yy)

###如果你想把这个def函数的运行结果拿来调用的话你就要return，看到有return的函数就说明这个函数是有返回结果的
###函数的结果用变量来保存

# def sum1(a,b=99):
#     sum=a+b
#     return sum
# c=sum1(20,89)
# print(c)
hongxing={
    "user":"yangjianbo",
    "age":"15",
    "sex":"男",
    "htight":"170",
    "phone":"13720094293"
}
def get_new_dict(tttt):
    if isinstance(tttt,dict)==True:
        key=[]
        value=[]
        for aa in tttt:
            key.append(aa)
        for bb in key:
            value.append(hongixng.get(bb))
        new_dict=dict(zip(key,value))
        return new_dict
    else:
        print('你输入的参数数据类型错误，请输入正确的字典')

###random模块是一个随机产生数的模块
##input()获取你从键盘输入的数据
####random.randint()产生随机整数
###break结束循环
####int()强制类型转为整型，str()强制转为字符串类型
###猜猜游戏
def guess():
    import random
    value = random.randint(1, 100)
    while True:
        res = input('请输入你竞猜的数字')
        try:
            res = int(res)
            if res > value:
                print('你猜的数字太大了，请继续!')
            elif res < value:
                print('你猜的数字太小了，请继续!')
            else:
                print('恭喜你答对了!')
                break
        except Exception as t:
            print(t)


#字符串格式
# y='杨建波'
# age=18
# print('我的名字是%s,我的年龄是%s'%(y,age))
