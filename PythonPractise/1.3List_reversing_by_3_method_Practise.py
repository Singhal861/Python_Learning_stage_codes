v1 = input("Enter the Food and Calories in this way\n Food-Calories Food-Calories Food-Calories\n = ")
# v1 = "h-21 l-3 p-0 z-6 j-89"
l = v1.split()
l1 = v1.split()
l2 = v1.split()
l1.reverse()
b = l2[::-1]
print(l1)
print(b)
a = l.__len__()

for i in range(0,a):
    l[i], l[a-1] = l[a-1], l[i]
    a = a-1
    if (i == a)|(i == a-1):
        print(l)
