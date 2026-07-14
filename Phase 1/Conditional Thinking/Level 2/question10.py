# 10. Take a month number (1–12) and print the number of days in that month (ignore leap years).

month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month")

elif month == 2:
    print("28 days")

elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")

else:
    print("31 days")