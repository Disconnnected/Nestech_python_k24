"""
3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Go to the editor
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String


cho 1 chuỗi ký tự, in ra 1 chuỗi kết quả, trong đó gồm 2 ký tự đầu tiên và 2 ký tự cuối cùng của chuỗi đã cho

Ví dụ:
    - Input: "Nestech"
    - output: "Nech"

"""

input_string = "python"

first_2_char = input_string[:2]
last_2_char = input_string[-2:]

output_string = first_2_char + last_2_char

print(output_string)

