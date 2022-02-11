currentPoint = 1
done = False

while not done:
    ## input recieving
    inp = int(input())

    if inp == 0:
        print("You Quit!")
        done = True
        break

    snakes = [[54,90,99], [19,48,77]]
    ladders = [[9, 40,67], [34, 64,86]]

    if (currentPoint + inp) <= 100:
        # Get next current point
        currentPoint += inp

    #Check to see if hit snake or ladders
    if currentPoint in snakes[0]:
        currentPoint = snakes[1][snakes[0].index(currentPoint)]
    
    if currentPoint in ladders[0]:
        currentPoint = ladders[1][ladders[0].index(currentPoint)]

    
    print("You are now on square " + str(currentPoint))

    if currentPoint == 100:
        print("You Win!")
        done = True
        break
    
        
    

