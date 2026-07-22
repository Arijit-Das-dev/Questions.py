# 8. Check if a number is a strong number (sum of factorials of digits = number). 

num = int(input("Enter a number : "))
org_num = num

summ = 0

while num != 0:

    fact = 1
    rem = num%10

    for i in range(1, rem+1):
        fact = fact*i

    summ = summ + fact
    num //= 10

if summ == org_num:
    print("Strong number")
else:
    print("Not a strong number")