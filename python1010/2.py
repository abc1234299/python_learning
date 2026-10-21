#解包传参
"""
    若函数的形参是定长参数，可以通过*和**对列表、元组、字典等解包传参
"""
# def func(a, b, c):
#     print(a, b, c)
#
# tup1 = (1, 2, 3)
# func(*tup1)
# dict1={'a':1,'b':2,'c':3}
# func(**dict1)

#强制使用位置参数或者关键字参数
"""
    /前面的参数必须使用位置传参，*后面的参数必须使用关键字传参
"""
# def f(a,b,/,c,*,d,e,f):
#     print(a,b,c,d,e,f)
#
# f(1,2,3,d=4,e=5,f=6)

#防止函数修改列表
"""
    有时要函数对列表进行处理，又不希望函数修改原列表，可以使用copy.deepcopy()
"""

#闭包
"""
    在一个函数体中定义另外一个函数
    外层的函数的返回值是内存函数对象
    在内函数中访问外函数定义的变量
    
    在闭包中，会延长外层函数中定义的变量的生命周期（相当于外层变量的生命周期和内层函数绑定，内函数结束之后，变量才被销毁）
"""
# def outer():
#     a = 10
#     def inner():
#         print(a)
#     return inner
#
# # outer()()
# f = outer()
# f()

# a = int(10.0) #int:内建作用域
def outer():
    var1=20
    def inner():
        nonlocal var1
        var1 =0
        print(var1)
    inner()
    print(var1)
outer()