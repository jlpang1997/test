def mysum(*args):
    # 可变参数
    tmp=0
    for num in args:
        tmp+=num
    return tmp
# print(mysum(1,2,3,4,5))

#命名关键字参数
#默认带默认值
def f(*args,param1=10):
    print(args)
    print(param1)

#不带默认值
def f1(*args,param1):
    print(args)
    print(param1)

# f1(10)
# f1(param1=10)

# def person(name, age, *, city, job):
#     print(name, age, city, job)

# # person('Jack', 24, 'Beijing', 'Engineer')
# person('Jack', 24,city= 'Beijing',job= 'Engineer')

# def person(name, age, *args, city, job):
#     print(name, age, city, job)

# person('Jack', 24, 'Beijing', 'Engineer')
# person('Jack', 24,city= 'Beijing',job= 'Engineer')

############命名关键字参数放在 * 或者 *args 后面 调用的时候必须指明参数名

def fun2(n):
    print(n)
fun2(n=10)

#以下这种形式可以作为有任意参数的函数，也就是任意函数，
# 故总结来说，位置参数存在的意义是：规定这个函数必须要传进来的参数，而且只要按顺序放进来就行，不用指明参数名(想的话也可以)，也就是说方便调用的存在
#默认参数：
#可变参数：针对未知数量的位置参数
#命名关键字参数：
#关键字参数：针对未知参数的关键字参数

def fun1(*args,**kw):
    print(args)
    print(kw)
    # print(para)
# fun1(10,a=2,b=10)