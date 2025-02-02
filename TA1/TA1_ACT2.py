userInput = input("Enter a string with digits: ")
sum_digits = 0

for char in userInput:
    if char.isdigit():
        sum_digits += int(char)
print("Sum of digits: ", sum_digits)