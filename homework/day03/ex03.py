"""
cho dãy số từ 1 đến 100
in ra các số thoả mãn điều kiện:
    - chia hết cho 2
    - chia hết cho 3
    (chia hết cho cả 2 và 3)
"""
output = []
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        output.append(i)

print(output)