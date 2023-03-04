# # list
# # variable = value
# # string[]

# sample_number = [1,3,5,6,8,9,10,22, 13]
# sample_string = ["Python", "Javascript", "PHP", "SQL"]
# # list indexing
# # list method
# # sample_string.append("C#")
# # sample_number.insert(1, "2")
# # sample_string.remove("Python")
# # sample_string.clear()
# # sample_string.pop()
# # x = sample_number.index(5)
# # sample_string.count()
# # sample_number.sort()

# # sample_number.copy()

# # x = 10
# # y = x
# # x = x + 5
# # print(f"x = :{x}")
# # print(f"y = :{y}")

# sample_string = ["Python", "Javascript", "PHP", "SQL"]
# # sample_string_2 = sample_string
# sample_string_2 = sample_string.copy()
# sample_string.append("React")

# print(f"sample_string = :{sample_string}")
# print(f"sample_string_2 = :{sample_string_2}")

# # reference

# # sample_string_3 = sample_string.copy()

# # print(sample_string_3)

# # print(sample_number)
import pprint
# dictionary

dict_sample = {
    "python":"Là ngôn ngữ lập trình có khả năng tiếp thu nhanh nhất",
    "PHP":"ngôn ngữ lập trình web số 1 năm 2008",
    "React":"Framework tốt nhất để phát triển giao diện ứng dụng"
}

info = {
    "name": "nguyễn vinh quang",
    "tuổi": 18,
    "trình độ": ["Đại học","Phổ thông","thạc sỹ"],
    "lý lịch": {
        "bố":"something",
    }
}

# pprint.pprint(info)
x = info["trình độ"]
info["age"] = 28

# print(info)

# tuple
# set

tuple_sample = (21,4,7,3,8,9)

# Boolean
is_ronaldo_better_than_messi = False

"""
cho list: input_list = [1,2,5,7,3,7,8,5,3,7,98,4]

yêu cầu: sắp xếp list từ lớn đến nhỏ, và ko có giá trị trùng lặp
"""
input_list = [1,2,5,7,3,7,8,5,3,7,98,4]
# input_list.sort()

# new_input = set(input_list)
# new_input = list(new_input)
# new_input.sort()
x = list(set(input_list))
x.sort()
# print(x)

# print(new_input)
 

# if else statement condition

"""
Nếu hôm nay trời mưa --> ở nhà với vợ
hôm nay trời nắng --> đi uống beer
"""

troi_mua = True
troi_nang = True
tam_trang_vk = "Vui"

# and và or

if troi_nang or  tam_trang_vk == "Buồn":
    print("ở nhà nấu cơm cho vợ")
    print("ko đi đâu cả")

else:
    print("đi nhậu")

"""
if (condition) --> True:
    do this code 
"""

# variable = value
# variable = value

# x = 5
# y = 7

# print(x >= y)

