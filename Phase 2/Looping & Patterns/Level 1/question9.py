# 9. Print the factorial of a given number. 

n = int(input("Enter a number : "))

# using for loop
fact_1 = 1

for i in range(n, 0, -1):
    fact_1 = fact_1 * i

print(fact_1)

# using while loop
fact_2 = 1
i = 0

while (n > i):
    fact_2 = fact_2 * n

    n -= 1

print(fact_2)