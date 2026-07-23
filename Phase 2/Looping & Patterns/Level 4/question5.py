# 5. Find the smallest and largest digit in a given number. 

num = int(input("Enter a number : "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10