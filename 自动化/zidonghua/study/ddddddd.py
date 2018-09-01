#类的集成
class yeye(object):
    def yeye1(self):
        print('我爷爷有100块钱')

class baba(yeye):
    def baba1(self):
        print('我爸爸有一套房子')

class wo(baba):
    pass









class buy_car(object):
    def jiaoxiao(self):
        print('学驾照')
    def s4(self):
        print('我来店里买了车了')
    def dishuiju(self):
        print('我来交税了')
    def jiaotongju(self):
        print('我来注册了')


if __name__ == '__main__':
    print('33333')