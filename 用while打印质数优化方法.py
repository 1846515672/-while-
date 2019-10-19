from time import *

class ZhiSshu:
#一.
    def func1(self):
        t1 = time()
        i = 2
        while i < 10000:
            flag = True
            j = 2
            while j < i:
                if i % j == 0:
                    flag = False
                j += 1
            if flag:
                print(i)
            i += 1
        t2 = time()
        print('耗时:',t2-t1,'秒')
#二.
    def func2(self):
        t3 = time()
        i = 2
        while i < 10000:
            flag = True
            j = 2
            while j < i:
                if i % j == 0:
                    flag = False
                    break#给代码一添加break让程序执行出现不满足条件的时候不执行以下代码
                j += 1
            if flag:
                print(i)
            i += 1
        t4 = time()
        print('耗时:',t4-t3,'秒')

#三.
    def func3(self):
        t5 = time()
        i = 2
        while i < 10000:
            flag = True
            j = 2
            while j <= i ** 0.5:#这里必须是<=符号,要不然打印结果不准确,会打印出4这样的数
                if i % j == 0:
                    flag = False
                j += 1
            if flag:
                print(i)
                break
            i += 1
        t6 = time()
        print('耗时:',t6-t5,'秒')

z = ZhiSshu()
# z.func1()
# z.func2()
# z.func3()
