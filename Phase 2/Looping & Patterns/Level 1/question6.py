# Print the sum of first n natural numbers.

# using for loop
n = int(input("Enter number : "))

summ_1 = 0
for i in range(1, n+1):
    summ_1 += i
print(summ_1)


# using while loop
summ_2 = 0
i = 1
while (i<n+1):

    summ_2 += i
    i += 1
print(summ_2)