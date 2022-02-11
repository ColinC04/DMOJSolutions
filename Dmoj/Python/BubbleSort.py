n = int(input())
ls = [int(x) for x in input().split()]


strLs = [str(item) for item in ls]
print(" ".join(strLs))

for i in range(n-1):
    for j in range (0, n-i-1):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
            #output the list
            strLs = [str(item) for item in ls]
            print(" ".join(strLs))

            

