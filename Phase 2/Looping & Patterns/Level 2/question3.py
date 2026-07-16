# 3. Check if a number is a palindrome.

num = int(input("Enter a number : "))

org_num = num

pallindrome = 0

while num != 0:

    rem = num % 10
    pallindrome = pallindrome*10 + rem
    num //= 10

if pallindrome == org_num:
    print("Pallindrome")
else:
    print("Not pallindrome")