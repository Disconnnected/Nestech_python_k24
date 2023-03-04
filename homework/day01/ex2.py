"""
cho 1 chuỗi có sẵn, in ra màn hình chuỗi trong đó các ký tự đc yêu cầu sẽ được thay thế cho các ký tự có sẵn

đề bài: 
    - chuỗi đã cho: "Aquafina - Vị ngon của sự tinh khiết"
    - Yêu cầu: 
        - ký tự "a" đổi thành "@"
        - Ký tự "o" đổi thành "0"
        - Ký tự "s" đổi thành "$"
        - Ký tự "i" đổi thành "1"
"""
input_string = "Aquafina - Vị ngon của sự tinh khiết"

# string.replace("original string", "replace string")

string_1 = input_string.replace("a", "@")
string_2 = string_1.replace("o","0")
string_x = input_string.replace("o", "0").replace("s", "$").replace("i", "1")
print(string_2)