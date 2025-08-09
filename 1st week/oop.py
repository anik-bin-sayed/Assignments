# class 1: Person


class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age},Address: {self.address}")


# class 2: Student


class Student(Person):
    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id

        self.grades = {}
        self.courses = []

    # Methods

    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} added for {self.name} in {subject}")
        else:
            print("Not enrolled in course")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print("Already enrolled in course")

    def display_student_info(self):
        self.display_person_info()

        print(f"ID : {self.student_id}")
        print(f"Grades: {self.grades}")

        if self.courses:
            print("Courses are: ")
            for course in self.courses:
                print(course, end=", ")


# according to "Ensure students are enrolled in a course before assigning grades"

# student = Student(name="Anik", age=99, address="Bangladesh", student_id="101")

# student.enroll_course(course="Math")
# student.enroll_course(course="Bangla")

# student.add_grade(subject="Math", grade="A")

# student.display_student_info()


class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def display_course_info(self):
        print(
            f"Course name : {self.course_name}\nCourse code: {self.course_code} \nInstructor: {self.instructor}"
        )

        if self.students:
            for name in self.students:
                print(f"{name}")
        else:
            print("kono students nai")


# course = Course(course_name="Python", course_code="batch-6", instructor="Zayed")

# course.add_student("ANik bin sayed")
# course.add_student("Shuaib")

# course.display_course_info()
