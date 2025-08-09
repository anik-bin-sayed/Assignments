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
    if not student or not course:
        print("Student or course not found. ")
        return

    if course.course_name not in student.courses:
        print("Student in not enrolled in course")
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
                    "students": {
                        student.student_id: {
                            "name": student.name,
                            "age": student.age,
                            "address": student.address,
                            "grades": student.grades,
                            "courses": student.courses,
                        }
                        for student in course.students
                    },
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

        for student_id, student_info in data["students"].items():
            print("Student ID ->", student_id)
            print(json.dumps(student_info, indent=4))

        for course_code, course_info in data["courses"].items():
            print("Course code ->", course_code)
            print(json.dumps(course_info, indent=4))

        print("Data loaded successfully.")


# load_data()
