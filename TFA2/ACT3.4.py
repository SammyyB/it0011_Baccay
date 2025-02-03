try:
    with open("students.txt", "r") as file:
        studentInfo = file.read()
        
        print("Reading Student Information:")
        print(studentInfo)
except FileNotFoundError:
    print("Error: 'students.txt' not found. Please ensure the file exists before reading.")