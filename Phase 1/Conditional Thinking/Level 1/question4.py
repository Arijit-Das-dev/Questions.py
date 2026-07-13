# 4. Check if a number is divisible by both 3 and 5.

num = int(input("Enter a number : "))

print("divisible by both 3 and 5" if num%5==0 and num%3==0 else "Not divisible by both 3 and 5")