# 3. Print all numbers between a and b divisible by 7. 

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

for num in range(a, b+1):
    if num%7 == 0:
        print(num)