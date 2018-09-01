userinfo={
    "uid":"001",
    "usN":"LALA",
    "age":"18",
}

def info():
    a = []
    b = []
    if isinstance(userinfo,dict)==True:
        for x in userinfo:
            a.append(x)
        for y in a:
            b.append(userinfo.get(y))
            c=dict(zip(a,b))
            return c
        else:
            print("fales")
c=info(userinfo)
print(c)


import random
import string
def id():
    num=input("请输入要产生证号码的个数：")
    try:
        num=int(num)
        shengfen='11'
        area=['0101','0102','0103','0104','0105','0106','0107','0108','0109','0111','0221','0222','0223','0224','0226','0227','0228','0229']
        years=[]
        months=[]
        days=[]
        ids=[]
        for year in range(1949,2019):
            year=str(year)
            years.append(year)
        for month in range(1,12):
            if month<10:
                month='0'+str(month)
                months.append(month)
            else:
                month = str(month)
                months.append(month)
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
            m=random.choice(months)
            d=random.choice(days)
            l=''.join(random.sample(string.digits,4))
            id=shengfen+a+y+m+d+l
            ids.append(id)
            print(id)
    except Exception as e:
        print(e)


#第二题
def a():
    import random
    b=random.randint(1,100)
    print(b)
    while True:
        aa=input("请输入数字：")
        try:
            aa=int(aa)
            # print("随机数是：%s"%b)
            if aa>b:
                print("大了 ")
            elif aa<b:
                print("小了 ")
            else:
                print("正确 ")
                break

        except ellipsis as e:
          print(e)

