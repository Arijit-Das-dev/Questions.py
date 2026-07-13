# 5. Check if a given year is a leap year. 

year = int(input("Enter a year : "))

print("Leap year" if year%4==0 or year%400==0 and year%100!=0 else "Not leap year")