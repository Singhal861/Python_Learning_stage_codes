
def Players_number_gusser():
    import random
    # Random no. generation and taking player's name
    a = random.randint(1, 20)
    # Player 1
    player1 = input("Enter your Name = ")
    turns_left1 = 7
    turns_taken1 = 0
    # Player 2
    player2 = input("Enter your Name = ")
    turns_taken2 = 0
    turns_left2 = 7
    # loop until the max no. of guess complete of any one player
    while turns_left1 and turns_left2:
        # Taking number as input from player1
        p1 = int(input(f"Enter your number {player1} = "))
        # Comparing Player1 number with my number
        if p1 == a:
            turns_left1 -= 1
            turns_taken1 += 1
            print(f"Winner: {player1}\n Congrats you defeat me in = {turns_taken1}\n Chances left = {turns_left1} ")
            # Declaring Player1 as winner
            break

        elif p1 > a:
            turns_left1 -= 1
            turns_taken1 += 1
            print(f"Wrong guess {player1}:\n "
                  f"Your number is larger then my number\n "
                  f"Turns left = {turns_left1}\n "
                  f"Turns taken = {turns_taken1}")

        elif p1 < a:
            turns_left1 -= 1
            turns_taken1 += 1
            print(f"Wrong guess {player1}:\n "
                  f"Your number is smaller then my number\n "
                  f"Turns left = {turns_left1}\n "
                  f"Turns taken = {turns_taken1}")

        # Taking number as input from player2
        p2 = int(input(f"Enter your number {player2} = "))
        # Comparing Player2 number with my number
        if p2 == a:
            turns_left2 -= 1
            turns_taken2 += 1
            print(f"Winner: {player2}\n Congrats you defeat me in = {turns_taken2}\n Chances left = {turns_left2} ")
            # Declaring Player2 as winner
            break

        elif p2 > a:
            turns_left2 -= 1
            turns_taken2 += 1
            print(f"Wrong guess {player2}:\n "
                  f"Your number is larger then my number\n "
                  f"Turns left = {turns_left2}\n "
                  f"Turns taken = {turns_taken2}")

        elif p2 < a:
            turns_left2 -= 1
            turns_taken2 += 1
            print(f"Wrong guess {player2}:\n "
                  f"Your number is smaller then my number\n "
                  f"Turns left = {turns_left2}\n "
                  f"Turns taken = {turns_taken2}")
    print(f"~~~~~~~~~~~~~~~Game finish~~~~~~~~~~~~~~~")


try:
    Players_number_gusser()
except Exception as e:
    print(e)
