# # var1, var2, var3 = 1, 2, 3
# # print(var1, var2, var3)
# var1 = 10
# var2 = 20
# # print(var1, var2)
# # var2, var1 = var1, var2
# # print(var1, var2)
# # print(type(var1))
# bool1 = True
# print(isinstance(var1, bool))
# print(isinstance(bool1, int))
# print(type(var1) == type(bool1))
import decimal
# from decimal import Decimal
# num1 = 0.1
# num2 = 0.2
# print(num1 + num2)
# print(Decimal(num1 + num2))
# num3 = Decimal('1.0')
# num4 = Decimal('2.0')
# print(num3 + num4)
# str1 = 'this is a string'
# str1 = "this is a 'string'"
# print(str1)
# # print(str2)
# str1 = """this is a
# string"""
# print(str1)
# str1 = '你好中国'
# print(str1)
# print(type(str1))
# byte1 = str1.encode(encoding='utf8')
# print(byte1)
#
# str2 = byte1.decode(encoding='utf8')
# print(str2)
# input_num = input("please input a number:")
# print(type(input_num))
# print("Hello"," Python","hello","world",sep="-----",end="####")
# print("使用###结尾\\n", end="###\n")
# print('使用""结尾', end="")
# int1 = 10
# float1 = 3.14159
# str1 = "int1 = %d, float1 = %.2f" % (int1, float1)
# print(str1)
# str2 = "int1 = {}, float1 = {:.2f}".format(int1,float1)
# print(str2)
# str3 = f"int_num={int1}, float_num={float1:.2f}"
# print(str3)
# float1 = 3.14159
# num1 = 1
# print(f"float_num = {float1:.2f}, int_num = {num1}")
# print("float_num= %.2f, int_num = %d"% (float1, num1))
# print("float_num ={:.2}, int_num={}".format(float1,num1))
# int1 = 10
# float1 = 3.14159
# str3 = f"{int1=}, {float1 = :.2f}"
# print(str3)  # int1 = 10, float1 = 3.14159

# match month := 3:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print(f"{month}月有31天")
#     case 4 | 6 | 9 | 11:
#         print(f"{month}月有30天")
#     case 2:
#         print(f"{month}月可能有28天")
#     case _:
#         print(f"{month}月有?天")
# num1 = 2
# num2 = 3
# max_num = num1 if num1 > num2 else num2
# print(max_num)
# for i in [2, 3, 5, 7, 11, 13, 17, 19]:
#     print(i)
# for i in range(-10, 10):
#     print(i)
sum = 0
for i in range(10):
    sum = sum + i**i
    if sum > 10000000:
        break
    print(i, sum)
else:
    print("循环完成,sum = ", sum)

