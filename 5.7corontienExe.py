def reader():
    f = "hello my name is abhishek singhal i live in pilibht uttarpardesh india and i completed my b.tech from lucnow university in mechanical engineering"
    # f = open("trash1.txt")
    # f.read()
    # # z = print(f.read())

    while True:
        content = (yield)
        if content in f:
            print("Your text is in file")
        else:
            print("Your text is not in file")


func = reader()
next(func)
func.send(input("Enter your text = "))
