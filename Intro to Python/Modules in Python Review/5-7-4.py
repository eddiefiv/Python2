import math
d = 1
s = 0

for i in range(1000000):
 
    if i % 2 == 0:
        s += 4/d
    else:
        s -= 4/d

    d += 2
     
print(f"Estimated pi: {s}")
print(f"math.pi: {math.pi}")