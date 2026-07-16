# 6. Check if a number is a perfect number. 

num = int(input("Enter a number : "))

summ = 0

for i in range(1, num):

    if num%i == 0:
        summ += i

if num == summ:
    print("Perfect number")
else:
    print("Not perfect number")