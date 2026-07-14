# 1. Take a 3-digit number and check if all digits are distinct.

num = int(input("Enter a number : "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

if digit1 != digit2 and digit2 != digit3 and digit3 != digit1:
    print("All are distinct")
else:
    print("Not distinct")