from math import sqrt
def func(x):
    return sqrt(x)

def decorator(f):
    count =  0
    def inner(x):
        nonlocal count
        count = count + 1
        x = abs(x)
        return f(x)
    return inner


inn = decorator(func)
print(inn(-4))
