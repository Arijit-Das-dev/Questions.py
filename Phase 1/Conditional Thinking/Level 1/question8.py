# 8. Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.

temp = int(input("Enter temparature : "))

if temp in range(0, 20):
    print("Cold")

elif temp in range(20, 30):
    print("Warm")

else:
    print("Hot")