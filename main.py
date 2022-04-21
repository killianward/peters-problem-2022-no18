# Peter's Problem 2022 No.18

from math import sqrt

def check(num):
    new_num = ""
    if sqrt(num).is_integer():
        for digit in str(num):
            new_num += str(int(digit) + 1)
        if sqrt(int(new_num)).is_integer():
            return True
        else:
            return False


for num in range(1000, 10000):
    if check(num):
        print(f"Answer: {num}")
