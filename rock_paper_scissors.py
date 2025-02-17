import random

choices = ['r', 'p', 's']

while True:
    user = input("Choice rock(r), paper(p), scissors(s):").lower()
    computer = random.choice(choices)

    if user == 'r' or user == 'p' or user == 's':
        print(f"Computer choose :{computer}")
        if user == computer:
            print("tie")
        elif (user =='r' and computer == 'p') or(user == 'p' and computer == 's') or (user == 's' and computer == 'r'):
            print("you lose!")
        elif (user =='p' and computer == 'r') or (user == 's' and computer == 'p') or (user == 'r' and computer == 's'):
            print("you win!")
    else:
        print("Enter valid choice!")
        
    final = input("Continue playing?(y/n):").lower()
    if final != 'y' and final != 'n':
        print("Invalid option")
    elif final == 'n':
        print("Thank you for playing!")
        break

