# 10. Take a password string and check basic rules (length ≥ 8 and contains at least one digit).

password = input("Enter password : ")

is_digit = False

if len(password) >= 8:
    
    for char in password:
        if char.isdigit():
            is_digit = True
            break

    if is_digit == True:
        print("Valid password")
    else:
        print("Not valid")
else:
    print("Not valid")