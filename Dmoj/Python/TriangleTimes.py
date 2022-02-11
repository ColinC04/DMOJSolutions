side1 = int(input())
side2 = int(input())
side3 = int(input())

sums = side1 + side2 + side3

if sums == 180:
    if side1 == side2 == side3:
        print("Equilateral")
    
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles")

    else:
        print("Scalene")

else:
    print("Error")