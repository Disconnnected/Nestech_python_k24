"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""

"""
input  = 10
for 1 - 10
if input % 2 - a 
"""

def prime_number(a):
    if a <= 0:
        return "Wrong input, try again"
    elif a == 1:
        return f"{a} are not prime"
    # elif a == 2:
    #     return f"{a} are prime"
    else:
        for i in range(2, a):
            if a % i == 0:
                return "They are not prime"
        return f"{a} are prime"

# prime_number(2)
print(prime_number(97))