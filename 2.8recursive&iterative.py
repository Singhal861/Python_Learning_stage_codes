# def factorial_itrative(n):
#     f = 1
#     for i in range (1, n+1):
#         f = f*i
#     return f
# number = int(input("entr no."))
# print(factorial_itrative(number))
#
# def factorial_recursive(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursive(n-1)
# n  = int(input("enter your no."))
# print(factorial_itrative(n))
def febo(n):
    """0 1 1 2 3 5 8 13"""
    if n == 1:
        return 0
    elif n== 2:
        return 1
    else:
        return febo(n-1) + febo(n - 2)
n = int(input("enter upto which place you want febonathy"))
print(febo(n))