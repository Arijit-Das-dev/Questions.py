# 7. Print all prime numbers between 1 and 100. 

for num in range(1, 101):

    if num < 2:
        continue

    is_prime = True

    for j in range(2, num):
        if num%j == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
    else:
        continue