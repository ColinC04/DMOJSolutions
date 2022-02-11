numRounds = int(input())

antoniaScore = 100
davidScore = 100

for i in range(numRounds):
    antoniaDie , davidDie = input().split()
    antoniaDie, davidDie = int(antoniaDie) , int(davidDie)

    if antoniaDie > davidDie:
        davidScore -= antoniaDie

    elif davidDie > antoniaDie:
        antoniaScore -= davidDie

print(antoniaScore)
print(davidScore)
    
