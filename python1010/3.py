def function(a, b, operator):
    return operator(a, b)
print(function(1, 2, lambda x, y: x + y))

student_list=[{"name":"lmq","age":23},{"name":"hql","age":200},{"name":"qq","age":20}]
print(sorted(student_list,key = lambda std_dict:std_dict["age"]))