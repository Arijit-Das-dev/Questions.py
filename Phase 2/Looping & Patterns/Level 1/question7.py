# Print the sum of all even numbers up to n.

n = int(input("Enter number : "))

# using for loop
summ_1 = 0
for i in range(1, n+1):
    if i%2 == 0:
        summ_1 += i

print(summ_1)

# using while loop
i = 1
summ_2 = 0
while (i < n+1):

    if i%2 == 0:
        summ_2 += i
    i += 1

print(summ_2)