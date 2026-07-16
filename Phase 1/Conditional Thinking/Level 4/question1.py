# 1. Take a character and check if it is a letter, a digit, or neither.

char = input("Enter a character : ")

if char.isdigit():
    print("Digit")

elif char.isalpha():
    print("Letters")

else:
    print("Neither")