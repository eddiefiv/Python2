import math
# 2.8
# Given a year (as a positive integer), find the respective number of the century. 
# Note that, for example, 20th century began with the year 1901.

num = 0
while True:
    x = int(input("Input a year\n"))

    if isinstance(x, int):
        num = x
        break
    else:
        print("Please input a valid year")

century = math.floor(num / 100) + 1
suffix = "st" if (math.floor(century % 10)) == 1 else "nd" if (math.floor(century % 10)) == "2" else "rd" if (math.floor(century % 10)) == "3" else "th"
print(f"The year {num} was during the {century}{suffix} century")