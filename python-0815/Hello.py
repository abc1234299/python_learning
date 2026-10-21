import decimal
# a = 2
# b = 10
# print(a, b)
# a , b = b , a
# print("a =",a,"b =", b)
from decimal import *
from operator import is_not

# f1 = decimal.Decimal("0.1")
# f2 = decimal.Decimal("0.2")
# f3 = f1 + f2
# print(f3)
# print(f3)

# str1 = str("18")
# print("今年" + str1 + "岁")
#
# var1 = int("1010",2)
# print(var1)
#
# eval("print(123)")
#
# print(ord('A'))
# print(chr(65))
# str = "你好中国"
# b1 = str.encode(encoding = 'gbk')
# print(b1)
# print(type(b1))
#++
# b2 = b1.decode(encoding='gbk')
# print(b2)
#
# name = input("请输入你的姓名：")
# print("欢迎您，" + name)

# int1 = 10
# float1 = 3.14
# print("int1=%d,float1=%f" % (int1,float1))
int1 = 10
float1 = 3.14
bool1 = True
print("int1={},float1={},bool1={}".format(int1, float1, bool1))
print("int1={2},float1={0},bool1={1}".format(int1, float1, bool1))
print(int1)