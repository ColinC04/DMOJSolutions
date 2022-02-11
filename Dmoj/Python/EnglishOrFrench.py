inp = int(input())

tTotal = 0
sTotal = 0

for i in range (inp):
    line = input()

    tTotal += line.count("T") + line.count("t")
    sTotal += line.count("S") + line.count("s")

if tTotal > sTotal:
    print("English")

else:
    print("French")
    