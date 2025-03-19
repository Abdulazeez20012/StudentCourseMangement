import os
from course import Course

class Enrollment:
    def __init__(self):
        self.course = Course()
        self.__enrolled_courses = {}
        self.ensure_file_exists()
        self.load_enrolled_courses()

    def ensure_file_exists(self):
        if not os.path.exists("../data/enrolled_courses.txt"):
            with open("../data/enrolled_courses.txt", "w") as file:
                pass

    def enroll(self, student_email, course_name):
        available_courses = self.course.view_course()

        if course_name not in available_courses:
            raise ValueError(f"Course '{course_name}' does not exist.")

        if student_email in self.__enrolled_courses:
            if self.__enrolled_courses[student_email] == course_name:
                raise ValueError(f"You are already enrolled in '{course_name}'.")
        self.__enrolled_courses[student_email] = course_name
        print(f"You have successfully enrolled in {course_name}.")
        self.save_enrolled_courses()


    def un_enroll(self, student_email, course_name):
        if student_email in self.__enrolled_courses and self.__enrolled_courses[student_email] == course_name:
            del self.__enrolled_courses[student_email]
            print(f"You have successfully Un enrolled from '{course_name}'.")
            self.save_enrolled_courses()
        else:
            raise ValueError(f"You are  not enrolled in '{course_name}'.")

    def save_enrolled_courses(self):
        with open("../data/enrolled_courses.txt", "a") as file:
            for student_email, course_name in self.__enrolled_courses.items():
                file.write(f"{student_email}:{course_name}\n")

    def load_enrolled_courses(self):
        self.__enrolled_courses = {}
        try:
            with open("../data/enrolled_courses.txt", "r") as file:
                for line in file:
                    student_email, course_name = line.strip().split(":")
                    self.__enrolled_courses[student_email] = course_name
        except Exception as e:
            print(f"Error loading enrollments: {e}")


    def view_students_in_course(self, course_name):
        students = [student_email for student_email, course in self.__enrolled_courses.items() if course == course_name]
        if students:
            return students
        else:
            raise ValueError(f"No students enrolled in '{course_name}'.")

    def view_enrolled_courses(self):
        enrolled_courses = list(set(self.__enrolled_courses.values()))
        print(enrolled_courses)
        return enrolled_courses