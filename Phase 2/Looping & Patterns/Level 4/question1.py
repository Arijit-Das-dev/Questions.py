# 1. Print all numbers whose sum of digits is even (1–100).
for num in range(1, 101):

    temp = num
    summ = 0

    while num>0:

        rem = num%10
        summ = summ + rem
        num //= 10

    if summ%2 == 0:
        print(temp)