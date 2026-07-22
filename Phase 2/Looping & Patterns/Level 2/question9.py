# 8. Check if a number is prime or not. 
while True:

    num = int(input("Enter a number : "))

    # conditions
    # condition 1 -> should not be a even number
    # condition 2 -> that number should not be divided within a range between 2 to num-1

    if num < 2:
        print("Not prime")

    elif num == 2:
        print("Prime number")

    else:
        is_prime = True
        for i in range(2, num):
            if num%i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime number")
        else:
            print("Not prime")