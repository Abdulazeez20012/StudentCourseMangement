from grade import Grade
from student import Student
from professor import Professor
from course import Course
from enroll import Enrollment

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = Course()
        self.grades = []
        self.roll = Enrollment()

    def get_students(self):
        return self.students


    def register_student(self, first_name, last_name, email, password):
        try:
            student = Student(password)
            student.register(first_name, last_name, email, password)
            self.students.append(student)
        except Exception as e:
            print(e)

    def enroll_course(self,course):
        try:
            self.roll.enroll(course)
        except Exception as e:
            print(e)


    def register_professor(self, first_name, last_name, email, password):
        professor = Professor(password)
        professor.first_name = first_name
        professor.last_name = last_name
        professor.email = email
        professor.register(first_name, last_name, email, password)
        self.professors.append(professor)
        print(f"Professor {first_name} {last_name} registered successfully.")

    def create_course(self, course_name):
        if not self.professors:
            print("No professors available to create a course.")
            return
        professor = self.professors[0]
        professor.add_course(course_name)
        print(f"Course {course_name} created successfully.")

    def assign_grade(self, student_email, course_name, grade):
        student = next((student for student in self.students if student.email == student_email), None)
        if not student:
            print("Student not found.")
            return
        if course_name not in self.courses.courses:
            print("Course not found.")
            return
        self.grades.append(Grade(student_email, course_name, grade))
        print(f"Grade {grade} assigned to {student_email} for {course_name}.")

    def view_student_grades(self, student_email):
        student_grades = [grade for grade in self.grades if grade.student == student_email]
        if not student_grades:
            print("No grades found for this student.")
            return
        for grade in student_grades:
            print(grade)

    def view_course(self):
        if not self.courses:
            print("No courses available.")
            return

        courses = self.courses.view_course()

        if not courses:
            print("No courses found.")
            return

        for course_id,course in courses.items():
            print(f"- Here is the course id:{course_id} and course:{course}")

    def login_in_student(self,email,password):
        try:
            student = Student(password)
            student.login(email,password)
        except Exception as e:
            print(e)



    def add_course(self,course_name):
        try:
            self.courses.add_course(course_name)
        except Exception as e:
            print(e)

    def remove_course(self, course):
        try:
            self.courses.remove_course(course)
        except Exception as e:
            print(e)

    def find_course_id(self,id_number):
        return self.courses.find_course_using_id(id_number)

    def view_enrolled_courses(self):
        enrolled_courses = self.roll.view_enroll_courses()
        for course in enrolled_courses:
            print(f"- {course}")

    def grade_student(self,course,student,grade):
        grades = Grade(course,student, grade)

    def verify_student_role(self, password, email):
        try:
            student = Student(password)
            return student.verify_email_in_file(email, password)
        except Exception as e:
            print(e)

    def verify_teacher_role(self, password, email):
        try:
            professor = Professor(password)
            return professor.verify_email_in_file(email, password)
        except Exception as e:
            print(e)

    def login_in_teacher(self,email,password):
        try:
            professor = Professor(password)
            professor.login(email,password)
        except Exception as e:
            print(e)









