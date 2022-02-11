inp = int(input())

list = []

for i in range(2*inp):
    list.append(input())

totalScore = 0

for i in range(inp):
    userInput = list[i]
    correctAnswer = list[inp+i]
    if userInput == correctAnswer:
        totalScore += 1

print(totalScore)
