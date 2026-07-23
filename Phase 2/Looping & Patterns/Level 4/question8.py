# 8. Print factorial of each number from 1 to n.

n = int(input("Enter a number : "))

for num in range(1, n+1):

    fact = 1

    while num > 0:

        fact = fact * num
        num = num - 1

    print(fact)