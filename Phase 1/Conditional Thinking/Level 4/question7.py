# 7. Take a single digit (0–9) and print its word form (“Zero” to “Nine”).

digit_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
digit = int(input("Enter digit (0-9) : "))

if digit in digit_dict:
    print(f"{digit_dict[digit]}")