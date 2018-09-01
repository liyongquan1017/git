import random
import string
class hongxing(object):
    def get_dict(self):
        a=input("请输入要产生的键值对数：")
        try:
            a=int(a)
            d={}
            for i in range(a):
                key=''.join(random.sample(string.ascii_lowercase,5))
                value=''.join(random.sample(string.digits,5))
                d[key]=value
            return d
        except Exception as b:
            print(b)

    def get_ele_len(self):
        a=['wanb','zhangyimin','liuxiaokang','feilong','gaoshang','wuijiankai','cuijiaming','wanghongxing','hongxing','chenxin','zhangchang','liyongquan','luzhiwei']
        l=[]
        for i in a:
            l.append(len(i))
        max_len=max(l)
        min_len=min(l)
        index1=l.index(max_len)
        index2=l.index(min_len)
        ele1=a[index1]
        ele2=a[index2]
        print('列表中最大的元素是%s,长度为%s,位于列表的第%s位置'%(ele1,max_len,index1))
        print('列表中最大的元素是%s,长度为%s,位于列表的第%s位置'%(ele2,min_len,index2))


    def get_odd_num(self):
        s=[]
        for i in range(1,101):
            if i%2==0:
                continue
            elif i%3==0 and i%5==0:
                s.append(i)
        return s

class chenxin(object):
    def money(self):
        print('我有三千万美元')


if __name__ == '__main__':
    y=chenxin()
    y.money()
