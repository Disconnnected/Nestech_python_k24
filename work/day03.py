"""
Viết chương trình nhập vào 3 số: a,b,c
sử dụng câu lệnh if để tìm ra số lớn nhất trong 3 số
"""

# a = int(input("nhập số a: "))
# b = int(input("nhập số b: "))
# c = int(input("nhập số c: "))

"""
a > b and a > c ==> a = max
a > b and a < c ==> c = max
a < b and b > c ==> b = max
a < b and b < c ==> c = max
"""
# max = None
# if a > b and a > c:
#     max = a

# max = None
# if a > b:
#     if a > c:
#         max = a
#     elif a < c: 
#         max = c
#     else:
#         print("3 số chưa đủ điều kiện")
# elif a < b:
#     if b < c:
#         max = c
#     elif b > c:
#         max = b
#     elif a == b:
#         print("3 số chưa đủ điều kiện")        
# else:
#     print("3 số chưa đủ điều kiện")

# print(f"số lớn nhất là: {max}")




# Loops
# while loop

"""
while condition:
    do st
    iterate
"""
# while

"""
Tìm các số chia hét cho 2 trong khoảng từ 1 đến 10
"""
# i = 0
# list_2 = []
# while i <= 10:
#     if i % 2 == 0:
#         list_2.append(i)
#     i +=1
# print(list_2)

"""
trong khoảng 1 - 100, nếu số đó chia hết cho 3 thì print(Ba)
nếu chia hết cho 5 thì print(Năm)
nếu chia hết cho cả 3 và 5 thì print(ba lăm)
còn các trường hợp còn lại, in ra số
"""

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i %5 == 0:
#         print("Ba Lăm")
#     elif i % 3 == 0:
#         print("Ba")
#     elif i % 5 == 0:
#         print("Năm")
#     else:
#         print(i)
#     i = i + 1

# for loop

# for variable in function:
#     do st
# range() --> build in function của python
# print(range(10))

# for i in range(10):
#     print(i)

# sample_string = "Python"
# #                012345
# for i in sample_string:
#     print(i)
# sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sample_list_2 = ["python", "PHP", "JS"]



# for i in sample_list_2:
#     print(i)

# Mu 0 - 7 Liver
# Tỉ số hiện tai là: 0-3

"""
cho chuỗi: 
input_list = [11,6,"sáu", [1,99,300, 1080], 9, 12, 144, 11]
    - loại bỏ các phần tử ko phải Int
    - sắp xếp lại chuỗi lớn đến nhỏ
"""
# input_list = [11,6,"sáu", [1,99,300, 1080], 9, 12, 144, 11]
# new_list = []
# for i in input_list:
#     if type(i) == int:
#         new_list.append(i)

# new_list = list(set(new_list))
# new_list.sort(reverse=True)
# print(new_list)



"""
cho chuỗi từ 0 tới 100
    - nhân từng phần tử của chuỗi với chính nó (bình thương)
    - tính tổng giá trị của chuỗi sau khi đã bình phương từng phần tử
"""
# total = 0
# for i in range(101):
#     i = i * i
#     # i = i ** 2
#     total = total + i
# print(total)

# quang = {
#     "name" : "nguyen vinh quang", 
#     "age": 18, 
#     "graduate": [
#         "High school",
#         "university",
#         "master"
#     ]
# }

# quang["name"] = "Nguyen Vinh Quang"
# quang["exp"] = 4
# print(quang)

# file handling
# path
# f = open("simple_student.csv")

# """
# r - read
# w - write
# a - append
# """

# f = open("lyrics.txt", "a", encoding="utf8")
# # print(f.read())
# # print(f.readlines())

# f.writelines("Đừng vội vàng em hãy là em của ngày hôm qua, ú u ú ù")

# f.close()

# function
# parameter / argument

def total(a, b):
    """
    Tính tổng của 2 số nguyên
    """
    # print(4 + 5)
    return a + b



x = total(4, 5)

y = sum([30,39,3,3,6,66])


print(f"Hàm x: {x}")
print(f"Hàm y: {y}")

# build in function vs user defined function







