# 4. Check if one of two given numbers is a multiple of the other. 

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second nummber : "))

if num1 == 0 or num2 == 0:
    print("connot divided by zero")
else:
    if num1%num2 == 0 or num2%num1 == 0:
        print("Multiple of others")
    else:
        print("Not Multiple of others")