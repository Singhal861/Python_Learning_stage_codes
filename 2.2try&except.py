def function1(a, b):
    """"This function add only two no.'s"""
    sum = int(a) + int(b)
    print("sum=", sum)
    return sum


print(function1.__doc__)
a = input("enter n1\n")
b = input("enter n2\n")
try:
    function1(a, b)
except Exception as z:
    print(z)
