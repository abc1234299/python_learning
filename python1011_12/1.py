# class Person:
#     def __init__(self, name=None):
#         self.name = name
#
# p = Person("张三")
# print(p.name)  # 张三
#
# p.age = 20
# print(p.age)
#
# Person.age = 200
# print(Person.age)
# file1 = open("test.txt","w")
# file1.write("hello world\nhello python\n")
# file1.close()

# 拷贝文件
def copy_file(src,dest):
    src_file = open(src, "rb")
    context = src_file.read()
    dest_file = open(dest, "wb")
    dest_file.write(context)
    src_file.close()
    dest_file.close()

copy_file("C:\\Users\\liang\\Desktop\\梁明秋 签名.jpg","D:\\PythonProject\\python1011\梁明秋签名.jpg")