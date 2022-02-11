done = False

tempValues = []
cityNames = []

while done == False:
    city, temp = input().split()

    tempValues.append(int(temp))
    cityNames.append(city)

    if city == "Waterloo":
        break

lowest = tempValues[0]

for item in tempValues:
    if item < lowest:
        lowest = item

print(cityNames[tempValues.index(lowest)])