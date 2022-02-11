one = int(input())
two = int(input())

sequence = [one, two]

done = False
counter = 2

while done == False:
    value = sequence[counter-2] - sequence[counter-1]
    sequence.append(value) 


    if sequence[counter] > sequence[counter-1]:
        done = True
    
    counter += 1

while not True:
    print("leo is so cool")


print(counter)
