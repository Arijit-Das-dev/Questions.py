# 3. Print all numbers that are palindromes between 1–500. 

for num in range(1, 501):

    temp = num
    pallindrome = 0

    while num != 0:

        rem = num%10
        pallindrome = pallindrome*10 + rem
        num //= 10

    if pallindrome == temp:
        print(temp)