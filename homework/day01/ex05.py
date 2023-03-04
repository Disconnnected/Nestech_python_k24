"""
 Write a Python program to count the number of characters (character frequency) in a string
 ex: 
    - google.com
answer:
    - "g": 2 lần
    - "o": 3 lần
    ....
"""
# input_string = "google.com"
# o = input_string.count("oo")
# print(f"chuỗi o xuất hiện : {o} lần")

# formatted string

first_name = "quang"
last_name = "nguyen"

sample_string = "xin mời phạm nhân có tên ronaldo lên trước bồi thẩm đoàn"
sample_string = "xin mời phạm nhân có tên messi lên trước bồi thẩm đoàn"

name = "messi"

output_string = "xin mời phạm nhân có tên " + name + "lên trước bồi thẩm đoàn"

output_string = "xin mời phạm nhân có tên {} {} lên trước bồi thẩm đoàn".format(first_name, last_name)

output_string = f"xin mời phạm nhân có tên {name} lên trước bồi thẩm đoàn"

print(output_string)

