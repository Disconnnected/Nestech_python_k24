"""
write a program that swap first and last element of a list
"""

sample_list = [0,1,2,3,4,5,6,7]

first_element = sample_list[0]
last_element = sample_list[-1]

# print(first_element)
# print(last_element)


sample_list[0] = last_element
sample_list[-1] = first_element

print(sample_list)