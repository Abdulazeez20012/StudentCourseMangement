import time

import authentication


def display(professor):


    print(f"""
            
    1. Add courses
    2. Assign courses
    3. View student Enrolled in course
    4. Remove courses
    5. View courses Teaching
    6. Log Out""")

    choice = input("Enter your choice: ").strip()
    while choice not in ['1', '2', '3', '4', '5',"6"]:
        print(f'\033[1;31mInvalid Input\nTry Again please Enter from 1-6\033[0m')
        choice = input("Enter your choice: ").strip()
    case(professor,choice)
    return choice


def case(professor,choice):
    match choice:
        case '1':
            try:
                course = input("Enter course name:").lower()
                professor.add_course(course)
                print(f"{course} successfully added")
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case '2':
            try:
                course = input("Enter course name:").lower()
                student_email = input("Enter student email:")
                student_email = authentication.Authentication.validate_email(student_email)
                grade = int(input("Enter grade:"))
                professor.professor_assign_grades(course,student_email,grade)
                print("Grade as been successfully added")
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case '3':
            try:
                course = input("Enter course name:").lower()
                professor.student_enrolled_in_course(course)
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case '4':
            try:
                course = input("Enter course name:").lower()
                professor.remove_course(course)
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')


        case '5':
            try:
              professor.view_courses()
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case '6':
            print_loading_message("Log in out")


def print_loading_message(message, delay=2.5):
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()