
# import random module

import random

# define a function with a parameter x:

def guess(X):
    random_number = random.randint(1, X)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {X}: "))
        print(guess)
        if guess < random_number:
            print("sorry!, guess is lesser than random number")
        elif guess > random_number:
            print("Sorry!, guess is too high")
        else:
            print(f"hooray!, you've guessed the random number {random_number} correctly...")


guess(10)