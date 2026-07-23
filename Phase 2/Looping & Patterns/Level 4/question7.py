# 7. Print a pattern where each row i prints i*i. 

for i in range(1, 6):

    for j in range(1, 6):
        print(i*i, end=" ")
    print()

for i in range(1, 6):

    for j in range(1, i+1):
        print(i*i, end=" ")
    print()