import os

records = []
filename = None

while True:
    print("=============================================")
    print("\nStudent Record Management System")
    print("1. Add Record")
    print("2. Edit Record")
    print("3. Delete Record")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Open File")
    print("9. Save File")
    print("10. Save As File")
    print("11. Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == "1":  
        student_id = input("\nEnter Student ID (6 digits): ")
        if not student_id.isdigit() or len(student_id) != 6:
            print("Invalid Student ID. Must be exactly 6 digits.")
            continue
        if any(record[0] == student_id for record in records):
            print("Student ID already exists.")
            continue

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = input("Enter Class Standing Grade: ")
        major_exam = input("Enter Major Exam Grade: ")

        records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")

    elif choice == "2":  
        student_id = input("\nEnter Student ID: ")
        for i, (sid, (first_name, last_name), class_standing, major_exam) in enumerate(records):
            if sid == student_id:
                new_first_name = input(f"Enter New First Name [{first_name}]: ") or first_name
                new_last_name = input(f"Enter New Last Name [{last_name}]: ") or last_name
                new_class_standing = input(f"Enter New Class Standing [{class_standing}]: ") or class_standing
                new_major_exam = input(f"Enter New Major Exam [{major_exam}]: ") or major_exam

                records[i] = (sid, (new_first_name, new_last_name), new_class_standing, new_major_exam)
                print("Record updated successfully.")
                break
        else:
            print("Student record not found.")

    elif choice == "3":  
        student_id = input("\nEnter Student ID: ")
        records = [record for record in records if record[0] != student_id]
        print("Record deleted successfully.")

    elif choice == "4":  
        if not records:
            print("No records available.")
        else:
            for student_id, (first_name, last_name), class_standing, major_exam in records:
                final_grade = str((int(class_standing) * 60 + int(major_exam) * 40) // 100)
                print(
                    f"Student ID: {student_id}\n"
                    f"First Name: {first_name}\n"
                    f"Last Name: {last_name}\n"
                    f"Class Standing: {class_standing}\n"
                    f"Major Exam: {major_exam}\n"
                    f"Final Grade: {final_grade}\n"
                    "--------------------------"
                )

    elif choice == "5":  
        records.sort(key=lambda x: x[1][1])  
        print("Records sorted by last name.")

    elif choice == "6":  
        records.sort(key=lambda x: (int(x[2]) * 60 + int(x[3]) * 40) // 100, reverse=True)  
        print("Records sorted by final grade.")

    elif choice == "7":  
        student_id = input("\nEnter Student ID: ")
        found = False
        for student_id_rec, (first_name, last_name), class_standing, major_exam in records:
            if student_id_rec == student_id:
                final_grade = str((int(class_standing) * 60 + int(major_exam) * 40) // 100)
                print(
                    f"Student ID: {student_id_rec}\n"
                    f"First Name: {first_name}\n"
                    f"Last Name: {last_name}\n"
                    f"Class Standing: {class_standing}\n"
                    f"Major Exam: {major_exam}\n"
                    f"Final Grade: {final_grade}\n"
                    "--------------------------"
                )
                found = True
                break
        if not found:
            print("Student record not found.")

    elif choice == "8":  
        file_name = input("\nEnter filename: ")
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                records.clear()
                student_data = file.read().strip().split("\n--------------------------\n")
                for data in student_data:
                    lines = data.strip().split("\n")
                    if len(lines) == 5:
                        student_id = lines[0].split(": ")[1]
                        first_name = lines[1].split(": ")[1]
                        last_name = lines[2].split(": ")[1]
                        class_standing = lines[3].split(": ")[1]
                        major_exam = lines[4].split(": ")[1]
                        records.append((student_id, (first_name, last_name), class_standing, major_exam))
            filename = file_name
            print(f"File '{file_name}' loaded successfully.")
        else:
            print("\nFile not found.")

    elif choice == "9":  
        if filename:
            with open(filename, 'w') as file:
                for student_id, (first_name, last_name), class_standing, major_exam in records:
                    file.write(
                        f"Student ID: {student_id}\n"
                        f"First Name: {first_name}\n"
                        f"Last Name: {last_name}\n"
                        f"Class Standing: {class_standing}\n"
                        f"Major Exam: {major_exam}\n"
                        "--------------------------\n"
                    )
            print("\nRecords saved successfully.")
        else:
            print("\nNo file loaded. Use 'Save As' to specify a filename.")

    elif choice == "10":  
        filename = input("\nEnter filename: ")
        with open(filename, 'w') as file:
            for student_id, (first_name, last_name), class_standing, major_exam in records:
                file.write(
                    f"Student ID: {student_id}\n"
                    f"First Name: {first_name}\n"
                    f"Last Name: {last_name}\n"
                    f"Class Standing: {class_standing}\n"
                    f"Major Exam: {major_exam}\n"
                    "--------------------------\n"
                )
        print("Records saved successfully.")

    elif choice == "11":  
        print("\nExiting program.")
        break

    else:  
        print("Invalid choice, please try again.")