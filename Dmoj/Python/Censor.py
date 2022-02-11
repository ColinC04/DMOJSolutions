n = int(input())

for i in range(n):
    ls = input().split()

    for i in range(len(ls)):
        if len(ls[i]) == 4:
            ls[i] = "****"


    print(" ".join(ls))