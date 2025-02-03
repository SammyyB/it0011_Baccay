fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

fullName = fname + " " + lname
slicedName = (fullName[:3])

greetings = f"Hello {slicedName}! Welcome. You are {age} years old "
print("\nFull Name: ", fullName)
print("Sliced Name: ", slicedName)
print("Greeting Message: ", greetings)