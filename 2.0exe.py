n1 = 1
T = 21
while(n1<=3):
    I = int(input("Enter your no.\n"))
    if I > T:
        print("Your no. is greater then my no.")
    elif I < T:
        print("Your no. is smaller then my no.")
    else:
        print("You got it")
        print(n1)
        break
    print("guessleft", 3-n1)
    n1 = n1 + 1

if n1 <= 3:
    pass
else:
    print("game over")