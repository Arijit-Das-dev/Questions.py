# 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”. 

hour = int(input("Enter hour : "))

if hour < 0 and hour > 23:
    print("Invalid hour")
    
elif hour >= 5 and hour <= 11:
    print("Good morning")

elif hour >= 12 and hour <= 15:
    print("Good afternoon")

elif hour >= 16 and hour <= 20:
    print("Good evening")

else:
    print("Good night")