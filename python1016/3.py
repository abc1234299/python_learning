from math import sqrt
class DecoratorClass:
    def __init__(self, f):
        self.func = f
    def __call__(self, x):
        x = abs(x)
        return self.func(x)

@DecoratorClass
def func(x):
    return sqrt(x)

print(func(-4))
