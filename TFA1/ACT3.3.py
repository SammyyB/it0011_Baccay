fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")
contNum = input("Enter contact number: ")
course = input("Enter course: ")

studentInfo = (
    f"Last Name: {lname}\n"
    f"First Name: {fname}\n"
    f"Age: {age}\n"
    f"Contact Number: {contNum}\n"
    f"Course: {course}\n"
    "-------------------------------------\n"
)

with open("students.txt", "a") as file:
    file.write(studentInfo)
print("Student Information has been saved to 'students.txt'.")