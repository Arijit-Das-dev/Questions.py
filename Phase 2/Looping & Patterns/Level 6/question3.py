# Print a Right-Aligned Triangle of Stars

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

# method 1
rows = 5

for i in range(1, rows+1):

    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()

# method 2
n = 5

for i in range(1, n+1):

    for j in range(i, n):
        print(" ", end=" ")

    for k in range(i):
        print("*", end=" ")

    print()