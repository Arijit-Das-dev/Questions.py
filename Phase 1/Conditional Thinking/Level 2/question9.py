# 9. Take a day number (1–7) and print the corresponding day name. 

days = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
}

day_num = int(input("Enter day : "))

if 0 < day_num > 7:
    print("Invalid Day")

elif day_num in days.keys():
    print(f"{day_num} : {days[day_num]}")