"""
    函数参数传递的形式
"""
#1.必须参数：按照参数位置进行匹配
"""
    调用函数时，每个实参都关联到函数定义中的一个形参
"""
# def print_info(a, b, c):
#     print(a, b, c)
#
# print_info(1, 2, 3)

#关键字参数，按照参数的名称进行匹配
"""
    使用关键字参数允许函数调用时参数的顺序与声明时不一致
"""
# def print_info(name,age):
#     print(name)
#     print(age)
#
# print_info("liangmingqiu", 23)
# print_info(age=23,name='lmq')

#默认值参数
"""
    定义函数时，可以给每个形成执行默认值
    注意：非默认参数必须放在默认参数之前
"""
# def print_info(name,age=20):
#     print(name,age)
#
# print_info("lmq")

#不定长参数：参数的个数是不确定的
"""
语法1：
    def 函数名([普通参数，]*var_agrs_tuple):
        函数体
"""
# def print_info(name,*args):
#     print(name,args)
#
# print_info("lmq",1,2,3,4,5)

#注意：如果不定长的参数后面还有参数，必须通过关机纳兹参数传参
# def print_info(name, *args,age):
#     print(name, args, age)
#
# print_info("lmq", 1,2,3,4,5, age=6)
# print_info("lmq", age=6)
#注意：如果没有给不定长的参数传参，那么得到空元组
#如果形参中出现不定长参数，那么在调用函数的时候，才能通过位置进行必须参数的匹配，然后不定长参数后面必须通过关键字参数匹配
"""
语法2：
    def 函数名([普通参数，] **var_args_dict):
        函数体
加了两个**的参数会以字典的形式导入，后面就不能有其他参数了
"""
def print_info(name, **agrs):
    print(name, agrs)

print_info("lmq", a = 10, b = 20, c = 30)