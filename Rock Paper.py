


"""
WORKFLOW  OF PROJECT:
1- Input from user (Rock , Paper, Scissor)
2- Computer Choice (Computer will choose randomly not conditionaly)
3- Print result

Cases:
A- Rock
Rock  -  Rock = tie
Rock  -  paper = paper win
Rock  -  Scissor = Rock win 

B- Paper
Paper - Paper  = tie
Paper - Rock = Paper win 
Paper - Scissor = scissor win

C- Scissor
Scissor - scissor = tie
Scissor - Rock = Rock win
Scissor - paper = Scissor win

"""

import random 
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your Move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same = Match tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers rock = Computer win")
    else:
            print("Rock smashes scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper = Computer win")
    else:
        print("Paper covers rock = you win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper = you win")
    else:
        print("Rock smashes scissor = computer win")
        
        
