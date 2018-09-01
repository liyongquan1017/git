
####输入多少条就产生多少条身份证信息
import random
import string
def id():
    num=input("请输入要产生的省份证号码数：")
    try:
        num=int(num)
        shengfen='11'
        area=['0101','0102','0103','0104','0105','0106','0107','0108','0109','0111','0221','0222','0223','0224','0226','0227','0228','0229']
        years=[]
        moths=[]
        days=[]
        ids=[]
        for year in range(1949,2019):
            year=str(year)
            years.append(year)
        for moth in range(1,13):
            if moth<10:
                moth='0'+str(moth)
                moths.append(moth)
            else:
                moth = str(moth)
                moths.append(moth)
        for day in range(1,31):
            if day<10:
                day='0'+str(day)
                days.append(day)
            else:
                day=str(day)
                days.append(day)
        for list in range(num):
            a=random.choice(area)
            y=random.choice(years)
            m=random.choice(moths)
            d=random.choice(days)
            l=''.join(random.sample(string.digits,4))
            id=shengfen+a+y+m+d+l
            print(len(id))
            ids.append(id)
    except Exception as e:
        print(e)


#字典取值，先取出KEY和VALUE然后组成新的字典

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
            value.append(hongxing.get(bb))
        new_dict=dict(zip(key,value))
        return new_dict
    else:
        print('你输入的参数数据类型错误，请输入正确的字典')


#猜数字游戏，猜对程序自动退出
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


