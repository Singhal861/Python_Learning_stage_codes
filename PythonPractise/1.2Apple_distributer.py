try:
    n = int(input(f"Enter the no. of Apples you want to give = "))
    mn = int(input(f"Enter the minimum value of Student = "))
    mx = int(input(f"Enter the maximum value of Student = "))
    if mn <= mx:
        if mn < mx:
            for y in range(mn, mx + 1):
                if n % y == 0:
                    print(f"{y} is a divisor of {n}")
                elif n % y != 0:
                    print(f"{y} is not a divisor of {n}")
        elif mn == mx:
            print(f"This is not a accurate ran"
                  f"ge because mn = mx ")
            if mn % n == 0:
                print(f"{mn} is a divisor of {n}")
            else:
                print(f"{mn} is a divisor of {n}")
    else:
        print(f"ERROR:\n Your minimum valve is greater then maximum value")
except Exception as e:
    print(e)
