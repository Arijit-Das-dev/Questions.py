# 9. Print the sum of all odd digits and even digits separately in a number.

num = int(input("Enter a number : "))

odd_sum = 0
even_sum = 0

while num > 0:

    rem = num%10

    if rem%2==0:
        even_sum += rem

    else:
        odd_sum += rem


    num //= 10

print(f"sum of odd digits : ",odd_sum)
print(f"sum of even digits : ",even_sum)