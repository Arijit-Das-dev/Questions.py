# Take 24-hour time (hours and minutes) and print whether it is AM or PM.

hour = float(input("Enter time (hour and minutes) : "))

if hour < 0 or hour > 23:
    print("Invalid hour")

elif 0 <= hour < 12:
    print(f"{hour} AM")
    
else:
    print(f"{hour} PM")