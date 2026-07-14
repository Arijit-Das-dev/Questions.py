# 2. Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 

num = int(input("Enter a number : "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

if digit2 > digit1 and digit2 > digit3:
    print("Middle is Largest")

elif digit2 < digit1 and digit2 < digit3:
    print("Smallest")

else:
    print("Neither")