"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

# random
import random

random_number = random.randint(1,9)

user_guess = int(input("Guess the number: "))
print(f"Random number: {random_number}")

if user_guess > random_number:
    print("you guess too high")
elif user_guess < random_number:
    print("you guess too low")
elif user_guess == random_number:
    print("Bingo, youre correct")
elif user_guess > 10 or user_guess < 1:
    print("invalid input")


