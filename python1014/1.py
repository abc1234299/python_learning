# class Person:
#     def __init__(self, name):
#         self.name = name
#
# Person.age = 20
# p1 = Person("lmq")
# print(p1.name, p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @property
#     def eat(self):
#         print(f"{self.name}is eating.")
#
# p = Person("John", 36)
# p.eat

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#
#     @property
#     def age(self):
#         return self.__age
# p = Person("John",20)
# print(p.age)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age

p = Person("John",20)
print(p.age)
p.age = 120
print(p.age)