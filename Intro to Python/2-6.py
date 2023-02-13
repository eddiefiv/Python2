import math
# 2.6
# Give a positive real number, print its first digit to the right of the decimal point
num = 0
while True:
    x = float(input("Input a positive number\n"))

    if isinstance(x, float):
        num = math.fabs(x)
        break
    else:
        print("Please input a positive number")

print(f"Number in the tens decimal: {math.floor(num * 10) % 10}")