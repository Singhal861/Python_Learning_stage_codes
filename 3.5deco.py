def dec(Func1):
    def executor():
        print("Executing Function")
        Func1()
        print("Executed")
    return executor()
@dec
def who_is_singhal():
    print("Abhishek is a good  boy")

# who_is_singhal = dec(who_is_singhal) or @dec

# who_is_singhal()