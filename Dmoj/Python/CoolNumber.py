import math
inpLow = int(input())
inpHigh = int(input())

total = 0

for i in range(inpLow, inpHigh+1):
    squareRoot = math.ceil((i**(1/2)))
    cubeRoot = math.ceil((i**(1/3)))
    if  squareRoot**2 == i and cubeRoot**3 == 1:
        total += 1

print(total)