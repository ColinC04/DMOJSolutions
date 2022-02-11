inp = input()

ls = [[1,2],[3,4]]

for letter in inp:
    if letter == "H":
        
        ls[0][0], ls[1][0] = ls[1][0], ls[0][0]
        ls[0][1], ls[1][1] = ls[1][1], ls[0][1]


    else:
        ls[0][0], ls[0][1] = ls[0][1], ls[0][0]
        ls[1][0], ls[1][1] = ls[1][1], ls[1][0]



for i in range(2):
	
    for j in range(2):
        print(ls[i][j], end = " ")

    print(" ")