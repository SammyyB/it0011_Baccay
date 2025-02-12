with open("C:/Users/ASUS/OneDrive/Documents/GitHub/it0011_Baccay/Technila Midterm Exam/numbers.txt", "r") as file:
    numbers = file.readlines()

for index, line in enumerate(numbers, start=1):
    line = line.strip()
    numbers_list = map(int, line.split(','))
    total = sum(numbers_list)

    if str(total) == str(total)[::-1]:
        print(f"Line {index}: {line} (sum {total}) - Palindrome")
    else:
        print(f"Line {index}: {line} (sum {total}) - Not a Palindrome")