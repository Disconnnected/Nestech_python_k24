"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""

name = input("Tên là gì?: \n")
age = int(input("tuổi bao nhiêu? : \n"))
current_year = 2023

birth_year = current_year - age
year_you_turn_100 = birth_year + 100

print(f"{name} will turn 100 in {year_you_turn_100}")
