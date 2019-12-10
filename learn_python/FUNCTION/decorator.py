# def decorater(func):
#     def wrapper(*args,**kw):
#         print('%s is called'%func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @decorater
# def add(x,y):
#     return x+y

# print(add(10,20))

# import functools
# def decorator_check(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         if args[0]<0 or args[0]>100:
#             raise ValueError('bad value')
#         else:
#             return func(*args,**kw)
#     return wrapper

# @decorator_check
# def sub(x,y):
#     return x+y
# # sub(-1,10)
# import functools 
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s is %s'%(func.__name__,text))
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# from enum import Enum



# @log('called')
# def mul(x,y):
#     return x*y
# # print(mul(10,20))
# print(mul.__name__)#如果没有@functools.wraps(func)则名字是wrapper

import functools
def log(text_func):
    if isinstance(text_func,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('%s is %s'%(func.__name__,text_func))
                return func(*args,**kw)
            return wrapper
        return decorator
    # if  isinstance(text_func,function):
    # elif type(text_func)==type(abs):
    elif callable(text_func):#判断是函数
        @functools.wraps(text_func)
        def wrapper(*args,**kw):
            print('%s is called'%text_func.__name__)
            return text_func(*args,**kw)
        return wrapper
    # elif isinstance(text_func,str):


@log
def div(x,y):
    pass
    # return x/y
@log('excute')
def f():
    # print('hello world')
    pass
@log
def g():
    pass
g()

# f()
# div(10,20)
# print(div(10,20))

# print(type(mul))    
# print('hello')    