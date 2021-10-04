"""
iterable - __iter__() or __getitems__()
Iteration- __next__()
Iteration - """
def gen(n):
    f = 1
    for i in range (1, n+1):
        f = f*i
    yield f

def genf(n):
    if n == 1:
        yield 0
    elif n == 2:
        yield 1
    else:
        yield genf(n-1) + genf(n-2)

n = int(input("n = "))
print(gen(n).__next__())
print(genf(n).__next__())
genf(n)
gen(n)
