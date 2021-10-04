# l1 = ["Bhindi", "Aaloo", "Gobi", "bagan"]
#
# for index, item in enumerate (l1):
#     if index%2 == 0:
#         print(f" Jarvis please buy {item}")

# import extraproject
# print(extraproject.getdate())

# list1 = ["teena", "cena", "khali", "randy", "orton", "jinder mahal"]
#
# # for item in list1:
# #     print(item, "and", end=" ")
# a = " and ".join(list1)
# print(a, "all other wwe superstar")
""".....................map function......................"""
# list1 = ["1","2","3" ,"7", "785","575", "76"]
# list1 = list(map(int, list1))
# print(list1[2]+1)
""".....................map + lambda function"""
# def sq(a):
#     return a*a
num = [2,4,6,7,8,9]
# square = list(map( sq, num))
# print(square)
# print(list(map(lambda x:x*x, num)))

# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
#
# fun = [sq, cube]
# for i in range(6):
#     print(list(map(lambda x:x(i), fun)))
"""................filter....................."""
# def is_greater_5(a):
#     return a>5
# is_greater_5 = list(filter(is_greater_5, num))
# print(is_greater_5)
# from functools import reduce
list1 = [3,2,5,8,7,4]
# prod = reduce(lambda x,y:x+y,list1)
# print(prod)
mun = 0
for i in list1:
    mun = mun+i
print(mun)
