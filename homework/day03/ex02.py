"""
Bài tập 1: vẽ hình tam giác vuông, 
    - sử dụng hàm Print
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
    - yêu cầu viết bằng function, với số dòng được truyền vào
ví dụ:

*
**
***
****
*****
******

"""

# def square(a):

# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")

def square(a):
    for i in range(a):
        print("*" * i)


square(10)