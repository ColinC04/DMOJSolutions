quarters, slotA, slotB, slotC = int(input()), int(input()), int(input()), int(input())

turns = 0

slotAWins, slotBWins, slotCWins = 35,100,10

done = False

while done == False:
    #Check slotA
    turns += 1
    slotA += 1
    quarters -= 1
    if slotA == slotAWins:
        slotA = 0
        quarters += 30
    if quarters == 0:
        break
    #Check slotB
    turns += 1
    slotB += 1
    quarters -= 1
    
    if slotB == slotBWins:
        slotB = 0
        quarters += 60

    if quarters == 0:
        break

    #Check slotC
    turns += 1
    slotC += 1
    quarters -= 1
    if slotC == slotCWins:
        slotC = 0
        quarters += 9

    if quarters == 0:
        break

    

print("Martha plays " + str(turns) + " times before going broke.")