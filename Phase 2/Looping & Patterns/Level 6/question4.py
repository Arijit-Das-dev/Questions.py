rows = 5

for i in range(1, rows+1):

    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(i, 0,-1):
        print(k, end=" ")
    print()