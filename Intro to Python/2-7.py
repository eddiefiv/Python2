import math
# 2.7
# A car can cover distance of N kilometers per day. 
# How many days will it take to cover a route of length M kilometers? 
# The program gets two numbers: N and M.
N = 0
M = 0
while True:
    n = int(input("Input an integer for N (how many kilometers traveled per day)\n"))
    m = int(input("Input an integer for M (total number of kilometers needed to be traveled)\n"))

    if isinstance(n, int) and isinstance(m, int):
        N = n
        M = m
        break
    else:
        print("Please input an integer for M and N")

print(f"The car can cover the {M}km trip in {math.ceil(M / N)} days")