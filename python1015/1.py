# try:
#     res = 10/1
#     print(res)
# except:
#     print("除数不能为0")
#
# print("程序结束")

# def add(num1, num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         return num1 + num2
#     else:
#         raise TypeError("参数类型必须是整数")
#
# sum = add(1.0, 2)
# print(sum)

# def MyException(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#
#     def __str__(self):
#         return self.msg
#
# def add(num1, num2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         return num1 + num2
#     else:
#         raise MyException("参数类型必须是整数")
#
# add(1.0,2)

try:
    with open("text.txt","wt") as file:
        file.write("str1")
finally:
    print("文件是否关闭",file.closed)