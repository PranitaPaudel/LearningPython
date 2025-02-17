import random 

highest_num = 100
lowest_num = 1

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("Heyy! Welcome to the guessing game.")
print(f"The range for the guesses is from {lowest_num} to {highest_num}")

while is_running == True :
    guess = input("Enter your guess:")
    if guess.isdigit():
        guesses += 1
        guess = int(guess)
        if guess < lowest_num or guess > highest_num:
            print("No No. Try again!")
            print(f"The range for the guesses is from {lowest_num} to {highest_num}")
        elif guess > answer:
            print("Close. Try lower")
        elif guess < answer:
            print("Close. Try higher")
        else:
            print(f"Yesss! you got it right. The number was {answer}")
            print(f"you took {guesses} tries to get the right answer")
            is_running = False
    else:
        print("Guess a number! TRY AGAIN!")

