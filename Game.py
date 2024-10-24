import random
option =["rock","paper","scissors"]
computer_choice =random.choice(option)

user_input=input("make a choice \nrock\npaper\nscissors\n ")
print("Computer choice =",computer_choice)
if computer_choice == user_input:
    print("Tie!")
elif computer_choice == "rock" and user_input == "paper":
    print("You won!")
elif computer_choice == "rock" and user_input== "scissors":
    print("You lose!")
elif computer_choice == "paper" and user_input == "rock":
    print("You lose!")
elif computer_choice == "paper" and user_input == "scissors":
    print("You won!")
elif computer_choice == "scissors" and user_input== "paper":
    print("You lose!")
elif computer_choice == "scissors" and user_input == "rock":
    print("You won!")
else:
    print("Game End!")

