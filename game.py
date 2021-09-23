# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

#  prompt user for input

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

# computer choice (at random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)



if (computer_choice == user_choice) :
    print("TIE")
elif ((user_choice == "rock") and (computer_choice == "scissors")) :
    print("TESS WINS")
elif ((user_choice == "scissors") and (computer_choice == "rock")) :
    print("COMPUTER WINS")
elif ((user_choice == "rock") and (computer_choice == "paper")) :
    print("TESS WINS")
elif ((user_choice == "paper") and (computer_choice == "rock")) :
    print("COMPUTER WINS")
elif ((user_choice == "scissors") and (computer_choice == "paper")) :
    print("TESS WINS")
elif ((user_choice == "paper") and (computer_choice == "scissors")) :
    print("COMPUTER WINS")


print("THANKS PLEASE PLAY AGAIN")