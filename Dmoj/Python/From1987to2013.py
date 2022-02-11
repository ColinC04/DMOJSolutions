year = int(input())

solve = "N"

currentYear = year + 1

while solve == "N":
    strYear = str(currentYear)

    for i in range(len(strYear)):
        if strYear.count(strYear[i]) >= 2:
            currentYear += 1
            break

        elif strYear.count(strYear[i]) < 2 and i == len(strYear)-1:
            solve = "Y"
            break

print(currentYear)
