import random

list1 = ["Snake", "Water", "Gun"]
t = 0
c = 0
win = 0
print("Welcome to snake water gun game\n", "Choose any one :Snake, Water, Gun")
while t < 10:
    a = random.choice(list1)
    b = str(input("Your Choice="))
    b = b.capitalize()
    if a == b:
        print("no result")
        t += 1
        print("Your turn left = ", 10 - t)
    elif b == "Snake" and a == "Water":
        print("-----You win this round-----")
        t += 1
        win += 1
    elif b == "Snake" and a == "Gun":
        print("-----You lost this round-----")
        c += 1
        t += 1
        print("Your turn left = ", 10 - t)
    elif b == "Water" and a == "Snake":
        print("-----You lost this round-----")
        c += 1
        t += 1
        print("Your turn left = ", 10 - t)
    elif b == "Water" and a == "Gun":
        print("-----You win this round-----")
        t += 1
        win += 1
        print("Your turn left = ", 10 - t)
    elif b == "Gun" and a == "Snake":
        print("-----You win this round-----")
        t += 1
        win += 1
        print("Your turn left = ", 10 - t)
    elif b == "Gun" and a == "Water":
        print("-----You lost this round-----")
        c += 1
        t += 1
        print("Your turn left = ", 10 - t)
    else:
        print("`````invalid input`````")
    continue
if win > c:
    print("_____Congrats you are the Winner_____\n", "__________Your win's = ", win,
          "__________" "\nComputer win's= ", c)
elif win == c:
    print("Game is Draw\n", "__________Your win's = ", win, "__________" "\ncomputer's win's= ", c)
else:
    print("You lost the game\n", "Your win's = ", win, "\ncomputer's win's= ", c)
