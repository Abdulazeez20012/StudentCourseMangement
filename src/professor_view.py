import time

import authentication


def display(professor) -> str:


    print(f"""
    1. Add course
    2. Assign course grade
    3. View students enrolled in course
    4. Remove course
    5. View courses being taught
    6. Log Out""")

    choice = input("Enter your choice: ").strip()
    while choice not in ['1', '2', '3', '4', '5',"6"]:
        print(f'\033[1;31mInvalid Input\nTry Again please Enter from 1-6\033[0m')
        choice = input("Enter your choice: ").strip()
    case(professor,choice)
    return choice


def case(professor,choice) -> None:
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
                grade = float(input("Enter grade:"))
                while grade < 1:
                    print(f'\033[1;31mInvalid grade Please you can not enter number lesser than 1\033[0m')
                professor.professor_assign_grades(course,student_email,grade)
                print("Grade added successfully.")
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
            print_loading_message("Logging out")


def print_loading_message(message, delay=2.5) -> None:
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()