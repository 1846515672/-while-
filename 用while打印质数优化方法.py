from time import *

class ZhiSshu:

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


    def func2(self):
        t3 = time()
        i = 2
        while i < 10000:
            flag = True
            j = 2
            while j < i:
                if i % j == 0:
                    flag = False
                    break
                j += 1
            if flag:
                print(i)
            i += 1
        t4 = time()
        print('耗时:',t4-t3,'秒')


    def func3(self):
        t5 = time()
        i = 2
        while i < 10000:
            flag = True
            j = 2
            while j <= i ** 0.5:
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
