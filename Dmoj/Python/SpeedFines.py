limit = int(input())
speed = int(input())

if speed <= limit:
    print("Congratulations, you are within the speed limit!")

else:
    difference = speed - limit
    if difference < 21:
        fine = 100
    
    elif difference > 20 and difference < 31:
        fine = 270

    elif difference > 30:
        fine = 500
    
    print("You are speeding and your fine is $" + str(fine) + ".")