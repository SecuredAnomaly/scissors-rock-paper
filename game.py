import random       #random 

user_action = input("Enter rock, paper, scissors:")  #izvēle
possible_actions = ["rock", "paper", "scissors"]     #vērtības
computer_action = random.choice(possible_actions)    #ran gen for computer_action

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")    #info text

if user_action == computer_action:                                      #rezultāti
    print(f"Both players selected {computer_action}. It's a tie!")      
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock destroys scissors! You win!")
    else:
        print("Paper wraps rock! You lose")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! you win")
    else:
        print("Scissors cuts paper you lose")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors snips paper! you win")
    else:
        print("Rock destroys scissors! you lose")
