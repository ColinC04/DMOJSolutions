n = int(input())

for i in range(n):
    k = int(input())
    
    done = False
    while done == False:
        value = k**3
        if str(value)[-3:] == "888":
            print(k)
            break
        k+=1
