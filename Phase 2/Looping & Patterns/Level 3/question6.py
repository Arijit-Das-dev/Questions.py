# 6. Print all factors of a given number. 

num = 6

for i in range(1, num+1):
    if num%i == 0:
        print(i)