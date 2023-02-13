import math
# 2.5
# Given a three-digit number. Find the sum of its digits.
num = 0
while True:
    x = int(input("Input an integer\n"))

    if isinstance(x, int):
        num = x
        break
    else:
        print("Please input an integer")

total = 0

for digit in iter(str(num)):
    total += int(digit)

print(f"Total sum of all digits: {total}")