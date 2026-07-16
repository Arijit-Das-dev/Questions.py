# 5. Take income and age, and check if eligible for tax (age > 18 and income > 5 L).

income = int(input("Enter your income : "))
age = int(input("Enter your age : "))

if age > 18 and income > 5:
    print("Eligible for tax")
else:
    print("Not eligible for tax")