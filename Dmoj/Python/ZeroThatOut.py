k = int(input())

li = []

for i in range(k):
    inp = int(input())

    if inp == 0:
        li.pop()
    
    else:
        li.append(inp)

print(sum(li))
