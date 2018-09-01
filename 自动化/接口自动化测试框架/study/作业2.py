# 1：随机产生5位数的字符串（要求是字符）作为KEY值，再随机产生5位数的字符串（要求是数字）作为value，组合成字典，输入多少条产生多少个字典元素（键值对），
# 不能使用dict(zip方法)
# 分析：首先随机获取key值，和value值，再通过字典的添加元素方法，组合成字典
import random
import string

def get_new_dict():
    num=input('请输入要产生的多少字典键值对数:')
    num=int(num)
    new_dict={}
    for i in range(num):
        key=''.join(random.sample(string.ascii_lowercase,5))
        value=''.join(random.sample(string.digits,5))
        new_dict[key]=value



# 2：有一个列表d=['wanba','zhangyimin','liuxiaokang','feilong','gaoshang','wuijiankai','cuijiaming','wanghongxing','hongxing','chenxin','zhangchang','liyongquan','luzhiwei']
# 获取最长及最短的元素，并打印出元素及下标位置
# 分析：首先循环取出列表中的元素进行长度的计算，然后再对长度进行比较处理，打印出长度最短的元素和最长的元素以及对应的下标位置

def element_len():
    d = ['wanba', 'zhangyimin', 'liuxiaokang', 'feilong', 'gaoshang', 'wuijiankai', 'cuijiaming', 'wanghongxing','hongxing', 'chenxin', 'zhangchang', 'liyongquan', 'luzhiwei']
    ele_len=[]
    for i in d:
        ele_len.append(len(i))
    max_len=max(ele_len)
    min_len=min(ele_len)
    index1=ele_len.index(max_len)
    index2=ele_len.index(min_len)
    ele_name1=d[index1]
    ele_name2=d[index2]
    print('列表中元素长度最大的为%s,位于列表的下标位置%s,其元素名为%s'%(max_len,index1,ele_name1))
    print('列表中元素长度最大的为%s,位于列表的下标位置%s,其元素名为%s'%(min_len,index2,ele_name2))




# 3：获取1-100之间的且可以整除3和5的奇数

def odd_num():
    od_num=[]
    for i in range(1,101):
        if i%2==0:
            continue
        else:
            if i%3==0 and i%5==0:
                od_num.append(i)
    return od_num

