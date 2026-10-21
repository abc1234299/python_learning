

# seq1=[1,2,3,4,5]
# seq2=[6,7,8,9]
# # print(seq1[1:3])
# # print(seq1+seq2)
# str3=["hello","world"]
# print(str3*2)
# print("hello" in str3)
# print(len(seq1))
# print(max(str3))
list1 = [100, 200, 300, 400, 500]
# print(list1[2:-1])
# print(list1[2::-1])
# list1.append(600)
# print(list1)
# list1.insert(2,10000)
# print(list1)
# list1[2:4]=["hello", "world"]
# print(list1)
# for i in list1:
#     print(i)

# for i in range(len(list1)):
#     print(i,list1[i])

# for i,val in enumerate(list1):
#     print(i, val)
# list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for inner_list in list2:
#     print(inner_list)

# 列表推导
# squares = [x**2 for x in range(5)]
# print(squares)
#
# seq1 = [x for x in range(5) if (x%2==0)and(x!=0)]
# print(seq1)
#
# list1 = [1, 2, 3, 4, 5]
# list2 = ["a", "b", "c", "d", "e"]
# zipped = zip(list1, list2)
# print(list(zipped))
# str1 = "hello world"
# print(str1 * 2)  # hello worldhello world

# set1 = {1, 2, 3}
# set2 = set([1, 2, 3])  # 使用set()函数从列表创建集合
# set3 = set()
# print(set1, set2, set3)

dict1={}
dict2=dict()
# print(dict1)
# print(dict2)
dict3={"name":"liangmingqiu","age":23,"gender":"female"}
print(dict3["name"])
print(len(dict3))
dict4=dict(name= "liangmingqiu",age=23,gender="female")
print(dict4)
dict5=dict([("name","liangmingqiu"),("age",23)])
print(dict5)