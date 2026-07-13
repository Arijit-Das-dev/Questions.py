# Take three sides and check if they form a valid triangle.

a = int(input("Enter angle a : "))
b = int(input("Enter angle b : "))
c = int(input("Enter angle c : "))

if a+b>c:
    if b+c>a:
        if c+a>b:
            print("Valid Triangle")
        else:
            print("Not a valid triangle")
    else:
        print("Not a valid triangle")
else:
    print("Not a valid triangle")