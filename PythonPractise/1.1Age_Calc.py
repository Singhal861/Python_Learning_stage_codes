def age():
    v1 = int(input("Enter your current age or year of birth = "))
    if v1 > 2022:
        print(f"You are not yet born")
    else:
        while 0 <= v1 <= 2021:
            if 100 >= v1 >= 0:
                print("You entered yours age")
                v2 = 100 - v1
                v3 = v2 + 2021
                print(f"you are getting 100yr old in = {v3}")
                break
            elif 1920 <= v1 <= 2021:
                print("You entered yours year of birth")
                v2 = 2021 - v1
                v3 = 100 - v2
                v4 = v3 + 2021
                print(f"you are getting 100yr old in = {v4}")
                v5 = input(f"do you want to know your current age\n 'y'  or   'n' = ")
                if v5 == "n":
                    break
                else:
                    print(v2)
                    break
            else:
                print(f"You seem to be the oldest person alive")
                break
try:
    age()
except Exception as e:
    print(f" {e}\n  Enter input in Numbers")
