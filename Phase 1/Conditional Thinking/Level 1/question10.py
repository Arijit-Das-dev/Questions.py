# 10. Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 

char = input("Enter a character : ")

if char.islower():
    print("Lowercase")
elif char.isupper():
    print("Uppercase")
elif char.isdigit():
    print("Digit")