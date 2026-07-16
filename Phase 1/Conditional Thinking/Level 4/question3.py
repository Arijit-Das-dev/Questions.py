# 3. Take three numbers and print the median value (neither maximum nor minimum).


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

asc_list = [num1, num2, num3]

for i in range(0, len(asc_list)-1):  
    min_index = i

    for j in range(1, len(asc_list)):
        if (asc_list[j]<asc_list[min_index]):
            min_index = j
    
    asc_list[i], asc_list[min_index] = asc_list[min_index], asc_list[i]

median = asc_list[1]
print(median)