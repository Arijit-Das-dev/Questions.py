# 3. Print all odd numbers between 1 and 100.

# using for loop
result = [num for num in range(1, 101) if num%2 != 0]
print(result)

# using while loop
i = 1

while i< 101:

    if i%2 != 0:
        print(i, end=" ")
    
    i += 1