import sys
import authentication
from student_management import StudentManagementSystem


def display_menu():
    print("""
            Welcome to MEA Institute Application 
            Choose between option 1-5:
            1. Register as Student
            2. Register as Professor
            3. Login as Professor
            4. Login as Student
            5. Exit""")

    choice = input("Enter your choice: ").strip()
    while choice not in ["1", "2", "3", "4", "5"]:
        print(f'\033[1;31mInvalid Input\nTry Again!!!\033[0m')
        choice = input("Enter your choice: ").strip()
    cases(choice)


def get_valid_input(prompt, validation_function, field_name=None):
    while True:
        try:
            value = input(prompt).strip()
            if field_name:
                value = validation_function(value, field_name)
            else:
                value = validation_function(value)
            return value
        except Exception as e:
            print(f'\033[1;31m{e}\033[0m')


def cases(choice):
    match choice:
        case "1":
            first_name = get_valid_input("Enter your first name: ", authentication.Authentication.validate_name,
                                         "first name").strip()
            last_name = get_valid_input("Enter your last name: ", authentication.Authentication.validate_name,
                                        "last name").strip()
            email = get_valid_input("Enter your email: ", authentication.Authentication.validate_email)
            password = get_valid_input("Enter your password: ", authentication.Authentication.validate_password).strip()
            StudentManagementSystem().register_student(first_name, last_name, email, password)

        case "2":
            first_name = get_valid_input("Enter your first name: ", authentication.Authentication.validate_name,
                                         "first name").strip()
            last_name = get_valid_input("Enter your last name: ", authentication.Authentication.validate_name,
                                        "last name").strip()
            email = get_valid_input("Enter your email: ", authentication.Authentication.validate_email)
            password = get_valid_input("Enter your password: ", authentication.Authentication.validate_password).strip()
            StudentManagementSystem().register_professor(first_name, last_name, email, password)

        case "3":
            email = get_valid_input("Enter your email: ", authentication.Authentication.validate_email)
            password = get_valid_input("Enter your password: ", authentication.Authentication.validate_password)
            StudentManagementSystem().log_in_professor(email, password)

        case "4":
            email = get_valid_input("Enter your email: ", authentication.Authentication.validate_email)
            password = get_valid_input("Enter your password: ", authentication.Authentication.validate_password)
            StudentManagementSystem().log_in_student(email, password)

        case "5":
            print(f"\033[1;32mThank you for using our application\033[32m")
            sys.exit()


def main():
    while True:
        display_menu()


if __name__ == "__main__":
    main()