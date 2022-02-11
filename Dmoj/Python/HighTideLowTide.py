import math
inp= int(input())

ls = input()
ls = ls.split()
ls = [int(x) for x in ls]
ls.sort()


spDescending = math.ceil(len(ls)/2)
spAscending = spDescending + 1

done = False
newls = []

while done == False:
    try:
        newls.append(ls[spDescending-1])
        newls.append(ls[spAscending-1])

    except:
        break

    spDescending -= 1
    spAscending += 1
    
if len(ls) % 2 != 1:
    newls.pop()
a = " ".join([str(x) for x in newls])
print(a)