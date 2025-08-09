import system_functionality as sf

while True:
    print("==== Student Management System ====")
    print("1. Add New Student\n2. Add New Course")
    print("3. Enroll Student in Course\n4. Add Grade for Student")
    print("5. Display Student Details\n6. Display Course Details")
    print("7. Save Data to File\n8. Load Data from File\n0. Exit")

    choice = input("\nEnter your choice:")

    if choice == "1":
        sf.add_new_student()
    elif choice == "2":
        sf.add_new_course()
    elif choice == "3":
        sf.enroll_student_course()
    elif choice == "4":
        sf.add_grade_for_student()
    elif choice == "5":
        sf.display_student_details()
    elif choice == "6":
        sf.display_course_details()
    elif choice == "7":
        sf.save_data()
    elif choice == "8":
        sf.load_data()

    elif choice == "0":
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Choice must be 0 - 8")
