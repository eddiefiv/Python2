import math
# 2.1
# Given a two-digit integer, print its left digit (a tens digit) and then its right digit (a ones digit).
# Use the operator of integer division for obtaining the tens digit and the operator of 
# taking remainder for obtaining the ones digit.
num = 0
while True:
    x = input("Input a 2 digit integer: \n")

    if len(str(x)) == 2:
        num = int(x)
        break
    else:
        print("Please input a 2 digit integer")

print(f"First digit is {math.floor((num / 100) * 10)}, and second digit is {num % 10}")