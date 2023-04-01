"""
Ghép nhiều chuỗi riêng biệt thành 1 chuỗi hoàn chỉnh, ngăn cách bởi dấu cách

đề bài:
    họ: "Nguyễn "
    Tên đệm: "Văn"
    Tên: "Tèo"

    output: Nguyễn Văn Tèo
"""

input_list = ["Nguyễn", "Văn", "Tèo"]

message = ""

# for char in input_list:
    # message += char + " "
message = "_".join(input_list)
# string method

print(message)