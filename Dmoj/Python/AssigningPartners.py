n = int(input())

lsx = input().split()
lsy = input().split()

solve = "good"

for i in range(n):
    
    for j in range(n):
        if lsx[i] == lsy[j]:
            if lsx[j] != lsy[i] or j == i:
                solve = "bad"


print(solve)