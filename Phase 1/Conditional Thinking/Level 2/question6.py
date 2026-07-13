# 6. Check voting eligibility for a given age (18+). 

age = int(input("Enter age : "))

if age <= 0:
    print("Invalid age")

elif age < 18:
    print("Not eligible for vote")

else:
    print("Eligible for vote")