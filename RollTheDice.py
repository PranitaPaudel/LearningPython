import random

def dice():
    numbers = [1,2,3,4,5,6]
    randNum = random.sample(numbers,2);
    return randNum

while True:
    choice = input("Roll the dice?(y/n):").lower()
    if choice == 'y':
        print(dice())
    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("invalid choice! Please try again.")
