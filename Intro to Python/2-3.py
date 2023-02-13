import math
# 2.3
# Given an integer greater than 9, print its last two digits.
num = 0
while True:
    x = int(input("Input an integer greater than 9 \n"))

    if x > 9:
        num = x
        break
    else:
        print("Please input an integer greater than 9")

print(f"Last 2 digits {num % 100}")