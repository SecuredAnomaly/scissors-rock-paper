
import random    


possible_actions = ["rock", "paper", "scissors"]    

while (True):
    computer_action = random.choice(possible_actions)
    user_action = input("Enter rock, paper, scissors:\n")  

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")   

    if user_action == computer_action:                                     
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
    elif user_action == "your mom":
        print("Your mother is so fat, king kong couldn't lift her")        
    else:

     while True:
        answer = str(input('Atkal? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("iemācies rakstīt")
    if answer == 'y':
        continue
    else:
        print("Atā")
        break
