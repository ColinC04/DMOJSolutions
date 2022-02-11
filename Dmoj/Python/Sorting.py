inpK = int(input())

li = []
for i in range(inpK):
    li.append(int(input()))

isDone = False


for i in range(inpK-1):
    flag = 0

    for j in range(inpK-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]


#Output the list
for item in li:
    print(item)