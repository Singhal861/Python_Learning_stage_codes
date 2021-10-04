# Taking items value of list
v1 = int(input("Enter the length of list = "))

# Making list of given items
l = []

# Add items to list
for i in range(v1):
    v2 = int(input("Enter the no's to be Palindromes "))
    l.append(v2)

# Entity list printing
print(f"List provided by you {l}")

# Making Palindromes list of entity list
l1 = []
for item in l:
    item = str(item)

# Checking is not or id entity number is Palindromes
    if item == item[::-1]:

        # Adding items to list
        l1.append(item)
    elif item != item[::-1]:

        # Finding next Palindromes of entity numbers
        while item != item[::-1]:
            item = int(item)
            item = item + 1
            item = str(item)

        # Adding items to list
        l1.append(item)

# Printing Palindromes list of entity list
print(f"Palindromes list of your list {l1}")
