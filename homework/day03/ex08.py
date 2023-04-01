"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

example: 
    - anna
    - civic
    - level
    - madam
    - mom
    - noon
    - radar
    - wow

"""

sample_string = "Civic"

if sample_string == sample_string[::-1]:
    print(f"{sample_string} is palindrome")
else:
    print(f"{sample_string} is not a palindrome")
