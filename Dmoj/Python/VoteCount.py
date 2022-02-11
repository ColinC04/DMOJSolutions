n = int(input())
line = input()

if line.count("A") > (n/2):
    print("A")

elif line.count("B") > (n/2):
    print("B")

else:
    print("Tie")