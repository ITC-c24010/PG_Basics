
a = 1
b = 2
c = 3

def f(x=3):
    return x ** x

def add_it(x, y=10):
    return x + y


result = add_it(2)

print(a + b + c + f() + result)

