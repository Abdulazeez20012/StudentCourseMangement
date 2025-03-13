from database import Database
from course import Course
from enroll import Enrollment
from grade import Grade
from grade_type import GradeType
from user import User


class Professor(User):
    def __init__(self, first_name,last_name,email, password):
        super().__init__(first_name,last_name,email,password)
        self.__professor_course = Course()
        self.__is_logged_in = False
        self.__student_enrolled = Enrollment()


    def get_courses(self):
        return self.__professor_course.get_courses()

    def get_course(self, course_id):
        return self.__professor_course.courses.get(course_id, None)


    def register(self,first_name,last_name,email,password):
            if not Database("student_details.txt").verify_email_exist(email) and not Database("professor_details.txt").verify_email_exist(email):
                self.__first_name = first_name
                self.__last_name = last_name
                self.__email = email
                self.__password = password
                Database("professor_details.txt").save_to_file(self.__first_name,self.__last_name,self.__email,self.__password)
            else:
                raise ValueError("Email already registered")



    def add_course(self, input_course):
        try:
            self.__professor_course.add_course(input_course)
            return f"Course {input_course} added successfully."
        except Exception as e:
            return str(e)

    def remove_course(self, input_course):
        try:
            self.__professor_course.remove_course(input_course)
            return f"Course '{input_course}' removed successfully."
        except Exception as e:
            return str(e)


    def view_courses(self):
        if not self.__professor_course.view_course():
            print("You are not teaching any course yet.")
        else:
            print("Teaching course/courses:")
            for particular_course in self.__professor_course.view_course():
                print(f"- {particular_course}")

    def login_state(self):
        return self.__is_logged_in


    def login(self,email,password):
        try:
            if Database("professor_details.txt").load_from_file(email,password):
                self.__is_logged_in = True
                print("You are logged in.")
            return self.__is_logged_in
        except Exception as e:
            print(e)

    def logout(self):
        self.__is_logged_in = False

    def professor_assign_grades(self,course_name,student_email, grade):
        if course_name in self.__professor_course.view_course():
            if student_email in self.__student_enrolled.view_students_in_course(course_name):
                Grade().set_numeric_grade(course_name,student_email,grade)
                Database("grade_details.txt").save_to_file_grades(course_name,student_email,grade,GradeType.from_numeric(grade))
            else:
                raise ValueError("Student not enrolled")
        else:
            raise ValueError(f"Invalid course .")



    def student_enrolled_in_course(self,course_name):
        try:
            self.__student_enrolled.view_students_in_course(course_name)
        except ValueError as e:
            print(e)