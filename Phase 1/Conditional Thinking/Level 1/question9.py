# 9. Take a character and check if it’s a vowel or consonant. 

char = input("Enter a random alphabet : ")

vowels = ['a', 'e', 'i', 'o', 'u']

if char.lower() in vowels:
    print("vowel")
else:
    print("consonant")