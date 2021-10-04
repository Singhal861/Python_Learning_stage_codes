try:
    v1 = int(input(f"Enter no. of Palindrome series you want = "))

    for i in range(0, v1):
        v2 = int(input("Enter no. for which you want next Palindrome no. = "))
        a = str(v2)
        if a == a[::-1]:
            print(f"Your no.'s Palindrome is {a}")
        elif a != a[::-1]:
            while a != a[::-1]:
                a = int(a)
                a = a + 1
                a = str(a)
            print(f"Your no.'s Palindrome is {a}")
except Exception as e:
    print(f"ERROR:\n     Please enter Number's onl"
          f"y\n     {e}")
