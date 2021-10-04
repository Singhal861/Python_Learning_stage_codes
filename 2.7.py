# l = 10 # global variable
# def funct1(n):
#     global l
#     l = 5 # local variable
#     m =8
#     print(l, m)
#     print(n, "i have printed")
#
# funct1("this is me")
# print(l)
x = 92
def abhishek():
    x= 20
    def singhal():
        global x
        x = 90
    print("before calling singhal", x)
    singhal()
    print("after calling singhal", x)
abhishek()
print(x)