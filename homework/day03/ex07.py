"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
example:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""
iteration over list a
if an element appear in list b ==> it's commmon between 2 list
else ==> not 
"""

expected_output = []

for i in a:
    if i in b:
        expected_output.append(i)

print(list(set(expected_output)))

