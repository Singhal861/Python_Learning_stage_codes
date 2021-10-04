# ls = [i for i in range(100) if i%3 == 0 ]
# print(ls)
# dict = {i:f"item{i}" for i in range(100) if i%5 == 0}
# # dict = {i:f"item{i}" for i in range(5)}
# dict1 = {value:key for key, value in dict.items()}
# print(dict, "\n", dict1)


# sets start with{
d1 = {dre for dre in ["dress1", "dress2","dress1", "dress2"]}
print(d1)


# one line genrators starts with (
# even = (i for i in range(100) if i%2 == 0)
# print(even.__next__())
# for item in even: print(item)