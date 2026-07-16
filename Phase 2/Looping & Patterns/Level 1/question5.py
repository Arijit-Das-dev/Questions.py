# 5. Print the table of a given number (n × 1 to n × 10). 

# using for loop
n = int(input("Enter a number : "))

for i in range(1, 11):
    print(f"{n} × {i} = ", n*i)

# using while loop
i = 1
num = 11

while (i< num):

    print(f"{n} × {i} = ", n*i)

    i += 1