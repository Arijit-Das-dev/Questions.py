# 7. Take three numbers and print the largest. 

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter first number : "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num3 and num2 > num1:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")