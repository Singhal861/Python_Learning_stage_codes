# a = input("what is your name")
# b = int(input("how much do you earn"))
# if b==0 :
#     raise ZeroDivisionError
# if a.isnumeric():
#     raise Exception("no. is not allowed")
# print(f"hello {a}")

c = input("Enter your name")
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError('harry is blocked by company')

    print("Exception is handel")
