''' Rondas is a fraud because he make a faulty  program of table teller for exam by which he can top in exam,
But you find by any means that he is fooling whole class and you make the program to reveal its truth'''

def Rohan_table(table_of, table_range, list1):
    import random
    a = random.randint(45, 50)
    for item in range(table_range + 1):
        if item != 0 and item != 8:
            list1.append(table_of * item)
        if item == 8:
            list1.append(a)
    print(f"Rohan das table of:\n  {table_of} is {list1}")


def Right_table(table_of, table_range, list2, list1):
    for item in range(table_range + 1):
        if item != 0:
            list2.append(table_of * item)
    if list2 != list1:
        print(f"Rohan das table is wrong:\n  Right table of\n  {table_of} is {list2}")
    elif list2 != list1:
        print(f"Rohan das table is Right:\n  table of {table_of} is {list1}")


table_of = int(input('Table of which no. you want\n'))
table_range = int(input(f'range of {table_of} table you want = '))
list1 = []
list2 = []

try:
    Rohan_table(table_of, table_range, list1)
    Right_table(table_of, table_range, list2, list1)
except Exception as e:
    print(e)
