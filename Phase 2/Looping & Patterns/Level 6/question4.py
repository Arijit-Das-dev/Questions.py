# 4. Print a Right-Aligned Triangle of numbers
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1

rows = 5

for i in range(1, rows+1):

    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(i, 0,-1):
        print(k, end=" ")
    print()