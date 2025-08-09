import json

from oop import Student, Course

# 1. Add New Studen

students = {}


def add_new_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists.")
        return

    student = Student(name, age, address, student_id)

    students[student_id] = student

    print(f"Student {name} (ID: {student_id}) added successfully.")


# add_new_student()

# 2. Add New Course

courses = {}


def add_new_course():
    course_name = input("Course name: ")
    course_code = input("Course code: ")
    instructor = input("Instructor: ")

    if course_code in courses:
        print("Course Code already exists.")
        return

    course = Course(course_name, course_code, instructor)

    courses[course_code] = course

    print(
        f"Course {course_name} (Code: {course_code}) created with instructor {instructor}."
    )


# add_new_course()


# 3. Enroll Student in Course


def enroll_student_course():
    student_id = input("Student Id: ")
    course_code = input("Course code: ")

    student = students.get(student_id)
    course = courses.get(course_code)

    if not student:
        print("No student found")
        return
    if not course:
        print("No course found")
        return

    # print(json.dumps(vars(course), indent=4, default=str))
    # print(json.dumps(vars(student), indent=4))

    course.add_student(student)

    print(
        f"Student {student.name} (ID: {student.student_id}) enrolled in {course.course_name}(Code: {course.course_code})"
    )


# enroll_student_course()

# # 4. Add Grade for Student


def add_grade_for_student():
    student_id = input("Student Id: ")
    course_code = input("Course code: ")
    grade = input("Grade: ")

    student = students.get(student_id)
    course = courses.get(course_code)

    #  Ensure students are enrolled in a course before assigning grades
    if student not in course.students:
        print("Please enroll first before adding grade")
        return

    student.add_grade(course.course_name, grade)


# add_grade_for_student()


# # 5. Display Student Details


def display_student_details():

    student_id = input("Student ID:")

    student = students.get(student_id)

    if not student:
        print("No student found")
        return

    print("Student Information: ")

    student.display_student_info()


# display_student_details()

# # 6. Display Course Details


def display_course_details():
    course_code = input("Course code: ")

    course = courses.get(course_code)

    if not course:
        print("No course found")
        return

    course.display_course_info()


# display_course_details()


def save_data():
    try:
        data = {
            "students": {
                student_id: {
                    "name": student.name,
                    "age": student.age,
                    "address": student.address,
                    "student_id": student.student_id,
                    "grades": student.grades,
                    "courses": student.courses,
                }
                for student_id, student in students.items()
            },
            "courses": {
                course_id: {
                    "course_name": course.course_name,
                    "course_code": course.course_code,
                    "instructor": course.instructor,
                    "students": [student.student_id for student in course.students],
                }
                for course_id, course in courses.items()
            },
        }

        with open("data.json", "w") as f:
            json.dump(data, f)

        print("All student and course data saved successfully.")

    except Exception as exp:
        print("Failed to save data", exp)


# save_data()


def load_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        f_data = json.dumps(data, indent=4)

        print(f_data)
        print("Data loaded successfully.")


# load_data()

# Sample Input / Output

while True:
    print("==== Student Management System ====")
    print("1. Add New Student\n2. Add New Course")
    print("3. Enroll Student in Course\n4. Add Grade for Student")
    print("5. Display Student Details\n6. Display Course Details")
    print("7. Save Data to File\n8. Load Data from File\n0. Exit")

    choice = input("\nEnter your choice:")

    if choice == "1":
        add_new_student()
    elif choice == "2":
        add_new_course()
    elif choice == "3":
        enroll_student_course()
    elif choice == "4":
        add_grade_for_student()
    elif choice == "5":
        display_student_details()
    elif choice == "6":
        display_course_details()
    elif choice == "7":
        save_data()
    elif choice == "8":
        load_data()

    elif choice == "0":
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Choice must be 0 - 8")
