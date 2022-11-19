import random

Selection = ("rock","paper","scissors")
running = True

while running:

        Player1 = None
        Player2 = random.choice(Selection)

        while Player1 not in Selection:
             Player1 = input(" Choose a mobile (rock, paper, scissors): ")

        print(f"Player1: {Player1}")
        print(f"Player2: {Player2}")

        if Player1 == Selection:
            print("It's a tie")
        elif Player1 == "rock" and Player2 == "scissors":
            print("You win")
        elif Player1 == "paper" and Player2 == "rock":
            print("You win")
        elif Player1 == "scissors" and Player2 == "paper":
            print("You win")
        else:
            print("You loes")
        
        if not input("play again? (y/n): ").lower() == "y":
            running = False
            
             