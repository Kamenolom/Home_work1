def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    for i in range(end):
        yield begin
        begin = func(begin)
from inspect import isgenerator
gen = some_gen(2, 3, pow)
print(isgenerator(gen))
print(list(gen))
