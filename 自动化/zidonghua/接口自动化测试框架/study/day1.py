import random
import string
y={
    "user":"yangjianbo",
    "age":"15",
    "sex":"男",
    "htight":"170",
    "phone":"13720094293",
    "room":{"北京":"5套","云南":{"大理":"3套","昆明":"2套"}}
}


def get_new_dict(value):
    if isinstance(value,dict)==True:
        key = []
        value = []
        for list in y:
            key.append(list)
        for list in key:
            value.append(y.get(list))
        new_dict=dict(zip(key,value))
        return new_dict
    else:
        print('输入的类型错误请重新输入')



def guess():
        while True:
            res = input('请输入你竞猜的数字')
            try:
                res = int(res)
                value = random.randint(1, 100)
                if res>value:
                    print('你猜的数字太大了，请继续!')
                elif res<value:
                    print('你猜的数字太小了，请继续!')
                else:
                    print('恭喜你答对了!')
                    break
            except Exception as e:
                print(e)


def id():
    import string
    value = input('请输入要产生的身份证号码条数')
    try:
        value=int(value)
        province='11'#省份
        area=['0101','0102','0103','0104','0105','0106','0107','0108','0109','0111','0221','0222','0223','0224','0226','0227','0228','0229']
        years=[]
        months=[]
        days=[]
        ids=[]
        for year in range(1949,2019):
            years.append(str(year))
        for month in range(1,13):
            if month<10:
                month='0'+str(month)
                months.append(month)
            else:
                months.append(str(month))
        for year in range(1,31):
            if year<10:
                year='0'+str(year)
                years.append(year)
            else:
                months.append(str(year))
        for list in range(value):
            id=province+random.choice(area)+random.choice(years)+random.choice(months)+random.choice(days)+''.join(random.sample(string.digits,4))
            ids.append(id)
        return ids
    except Exception as e:
        print(e)

