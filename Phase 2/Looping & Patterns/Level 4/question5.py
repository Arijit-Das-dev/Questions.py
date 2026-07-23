# 5. Find the smallest and largest digit in a given number. 
num = int(input("Enter a number: "))

smallest = 9
largest = 0

while num != 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    if digit > largest:
        largest = digit

    num //= 10

print("Smallest digit:", smallest)
print("Largest digit:", largest)