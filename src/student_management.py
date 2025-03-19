import time

import authentication
import professor_view
import student_view
from database import Database
from professor import Professor
from student import Student


class StudentManagementSystem:
    def __init__(self):
        pass


    def register_student(self, first_name, last_name, email, password) -> None:
        try:
            first_name = authentication.Authentication.validate_name(first_name)
            last_name = authentication.Authentication.validate_name(last_name)
            email = authentication.Authentication.validate_email(email)
            password = authentication.Authentication.validate_password(password)
            student = Student(first_name, last_name, email, password)
            student.register(first_name, last_name, email, password)
            print_loading_message("Registering Student")
            print("------------------------------------------------------------------")
            print(f"{first_name} {last_name} is Successfully registered as a student in MEA-INSTITUTE.!")
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')

    def register_professor(self, first_name, last_name, email, password) -> None:
        try:
            first_name = authentication.Authentication.validate_name(first_name)
            last_name = authentication.Authentication.validate_name(last_name)
            email = authentication.Authentication.validate_email(email)
            password = authentication.Authentication.validate_password(password)
            professor = Professor(first_name, last_name, email, password)
            professor.register(first_name, last_name, email, password)
            print_loading_message("Registering Professor")
            print("!------------------------------------------------------------------!")
            print(f"Registered Professor {first_name} {last_name} successfully!")
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')

    def log_in_professor(self, email, password) -> None:
        try:
            email = authentication.Authentication.validate_email(email)
            password = authentication.Authentication.validate_password(password)
            holder_tuple = Database("../data/professor_details.txt").load_from_file(email, password)
            holder = holder_tuple[0]
            print_loading_message("Logging Professor In")
            if holder_tuple[1]:
                stored_first_name,stored_last_name,stored_email,stored_password = holder[0],holder[1],holder[2],holder[3]
                professor = Professor(stored_first_name, stored_last_name, stored_email, stored_password)
                professor.login(stored_email,stored_password)
                choice = ""
                print(f"""
                       You have logged in Successfully, Professor {stored_first_name} {stored_last_name}. 
                       Welcome to MEA Institute
                       """)
                print("------------------------------------------------------------------")
                while choice != '6':
                    choice = professor_view.display(professor)
            else:
                print(f'\033[1;31mInvalid email or password\033[0m')
        except Exception as e:
            print("\033[1;31mSomething went wrong!\033[0m")
            print(f'\033[1;31m{e}\033[0m')

    def log_in_student(self, email, password) -> None:
        try:
            email = authentication.Authentication.validate_email(email)
            holder_tuple = Database("../data/student_details.txt").load_from_file(email, password)
            holder = holder_tuple[0]
            print_loading_message("Login Student")
            if holder_tuple[1]:
                stored_first_name,stored_last_name,stored_email,stored_password = holder[0],holder[1],holder[2],holder[3]
                student = Student(stored_first_name, stored_last_name, stored_email, stored_password)
                student.login(stored_email,stored_password)
                print(f"""
                            You have logged in successfully, {stored_first_name} {stored_last_name}. 
                            Welcome to MEA Institute
                            """)
                choice = ""
                while choice != "8":
                    choice = student_view.display(student, stored_first_name, stored_last_name, stored_email)
        except Exception as e:
            print("\033[1;31mSomething went wrong!\033[0m")
            print(f'\033[1;31m{e}\033[0m')




def print_loading_message(message, delay=0.5) -> None :
    print(message, end="", flush=True)
    for _ in range(8):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

