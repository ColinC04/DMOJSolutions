inp = int(input())

swifts = [int(x) for x in input().split()]
semaphores = [int(x) for x in input().split()]

sumSwifts = 0
sumSemaphores = 0
answer = 0

for i in range(inp):
    sumSwifts += swifts[i]
    sumSemaphores += semaphores[i]

    if sumSwifts == sumSemaphores:
        answer = i + 1

print(answer)

