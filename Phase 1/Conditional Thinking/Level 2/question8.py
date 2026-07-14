# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’. 

char = ord(input("Enter a char : "))

a = ord('a')
m = ord('m')

if char in range(a, m+1):
    print("lies between 'a' and 'm' ")

else:
    print("lies between 'n' and 'z' ")