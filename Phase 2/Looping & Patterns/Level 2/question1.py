# 1. Count the number of digits in a given number. 

dig = int(input("Enter a number : "))

count = 0

while dig != 0:

    count += 1
    rem = dig % 10
    dig //= 10

print(count)