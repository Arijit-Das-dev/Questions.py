# 4. Print numbers between 1–100 whose digits add up to a multiple of 3. 

for num in range(1, 101):

    temp = num
    summ = 0

    while temp > 0:

        rem = temp%10
        summ = summ + rem
        temp //= 10
        
    if summ % 3 == 0:
        print(num)