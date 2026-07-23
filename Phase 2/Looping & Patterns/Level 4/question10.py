# 10. Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print the sum of all non-zero numbers entered.

summ = 0

for num in range(5):

    num = int(input("Enter a number : "))

    if num == 0:
        continue

    else:
        summ = summ + num

print(summ)