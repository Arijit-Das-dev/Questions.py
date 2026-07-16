# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend.

week_num = int(input("Enter weekday number (1 - 7): "))

if week_num == 6 or week_num == 7:
    print("Weekend")
else:
    print("Weekday")