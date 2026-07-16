# 10. Print the product of digits of a given number.

n = int(input("Enter a number : "))

product = 1

while (n > 0):

    rem = n % 10
    product = product * rem
    n //= 10

print(product)