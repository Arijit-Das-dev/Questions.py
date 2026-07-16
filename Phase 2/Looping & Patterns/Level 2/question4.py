# 4. Find the sum of digits of a number. 

num = int(input("Enter a number : "))

summ = 0

while num != 0:

    rem = num % 10
    summ = summ + rem
    num //= 10

print(summ)