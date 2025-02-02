print("\n=========================================")
userInput = input("Enter a string: ")
vowels = consonants = spaces = others = 0

for char in userInput:
    if char in "AEIOUaeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isspace():
        spaces += 1
    else:
        others += 1
        
print("\n===============OUTPUT====================")
print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Spaces: ", spaces)
print("Others: ", others)
print("========================================")