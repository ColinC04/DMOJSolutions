n = int(input())

li = []

for i in range(n):
    li.append(int(input()))


for i in range (n):
    minimumValue = 1000000000
    for item in li:
        if item < minimumValue:
            minimumValue = item

    li.remove(minimumValue)
    print(minimumValue)


