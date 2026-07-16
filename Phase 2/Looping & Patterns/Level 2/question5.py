# 5. Check if a number is an Armstrong number.

num = int(input("Enter a number : "))
print(f"Number before : {num}")

org_num = num
power = len(str(num))
arm_str_num = 0

while num != 0:

    rem = num % 10
    arm_str_num = arm_str_num + rem**power
    num //= 10

print(f"Number after : {arm_str_num}")

if arm_str_num == org_num:
    print("Armstrong number")
else:
    print("Not armstrong number")