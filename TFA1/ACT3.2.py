fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

fullName = fname + " " + lname

fullNameUpper = fullName.upper()
fullNameLower = fullName.lower()
fullNameLen = len(fullName)

print("Full Name: ", fullName)
print("Full Name (Upper Case): ", fullNameUpper)
print("Full Name (Lower Case): ", fullNameLower)
print("Length of Full Name: ", fullNameLen)