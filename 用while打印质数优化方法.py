from time import *

def Number(fun):
    def func():
        t1 = time()
        fun()
        t2 = time()
        print('耗时:',t2-t1,'秒')
    return func

#一.
@Number
def func1():
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

#二.
@Number
def func2():
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
#三.
@Number
def func3():
    i = 2
    while i < 10000:
        flag = True
        j = 2
        while j <= i ** 0.5:#这里必须是<=符号,要不然打印结果不准确,会打印出4这样的数
            if i % j == 0:
                flag = False
                break
            j += 1
        if flag:
            print(i)
        i += 1
# func1()
# func2()
# func3()
