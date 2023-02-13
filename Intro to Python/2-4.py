import math
# 2.4
# Given an integer, print its tens digit.
num = 0
while True:
    x = int(input("Input an integer greater than 9 \n"))

    if x > 9:
        num = x
        break
    else:
        print("Please input an integer greater than 9")

print(f"Tens digit {math.floor((num % 100) / 10)}")