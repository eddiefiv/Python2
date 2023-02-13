import math
# 2.9
# A cupcake costs A dollars and B cents. 
# Determine, how many dollars and cents should one pay for N cupcakes. 
# A program gets three numbers: A, B, N. 
# It should print two numbers: total cost in dollars and cents.
cost = 0
amount = 0
while True:
    x = int(input("Input an integer for the price in ONLY dollars of a cupcake\n"))
    y = float(input("Input an integer for the price in ONLY cents of a cupcake (but as a whole number ie. not .67, just do 67)\n"))
    z = int(input("Input an integer for the amount of cupcakes to buy\n"))

    if isinstance(x, int) and isinstance(y, float) and isinstance(z, int):
        cost = x + (y / 100)
        amount = z
        break
    else:
        print("Please input valid values for all inputs")

total = cost * amount
print(f"Total cost in dollars: {math.floor((total) % 100)} and cents: {math.ceil(((total) * 100) % 100)}")