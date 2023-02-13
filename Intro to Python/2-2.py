import math
# 2.2
# Given a two-digit integer, swap its digits and print the result.
num = 0
while True:
    x = input("Input a 2 digit integer: \n")

    if len(str(x)) == 2:
        num = int(x)
        break
    else:
        print("Please input a 2 digit integer")

print(f"Inversed int {num % 10}{math.floor((num / 100) * 10)}")