# question = int(input())

# n = int(input())
# speed = 0

# dmoj = [int(x) for x in input().split()]
# dmoj.sort()
# peg = [int(x) for x in input().split()]
# peg.sort(reverse=True)

# if question == 1:
#     for i in range(n):
#         speed += min(dmoj[i], peg[i])


# else:
#     for i in range(n):
#         speed += max(dmoj[i], peg[i])

# print(speed)

question = int(input())

n = int(input())

totalSpeed = 0

dmoj = [int(x) for x in input().split()]
dmoj.sort()
peg = [int(x) for x in input().split()]
peg.sort()

if question == 1:
    for i in range(n):
        totalSpeed += max(dmoj[i], peg[i])

if question == 2:
    peg.reverse()
    for i in range(n):
        totalSpeed += max(dmoj[i], peg[i])

print(totalSpeed)