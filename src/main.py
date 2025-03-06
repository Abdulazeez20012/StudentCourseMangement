import re

from studentmanagement import StudentManagementSystem

from exception import UserNotFoundException,CourseNotFoundException,GradeOutOfRangeException



def print_menu():
    print("""
                ---WELCOME TO MEA PROGRAMMING INSTITUTE---
        Where Passion for Code Transforms into Innovation.
        --- Main Menu ---
        1. Register Student
        2. Register Professor
        3. Login
        4. Exit""")
def student_menu():
    manager = StudentManagementSystem()
    while True:
        print("""
            --- Student Menu ---
            1. View courses
            2. Enroll in a course
            3. view Enrolled courses
            4. View Grade
            5. find course with id
            6. find course id with course name
            7. Log out
        """)
        choice = input("Enter your choice 1- 7: ").strip()

        match choice:
            case '1':
                manager.view_course()
            case '2':
                    course = input("Enter course : ")
                    manager.enroll_course(course)
            case '3':
                manager.view_enrolled_courses()
            case '4':
                print("You caught us on this one. Working on it")
            case '5':
                id_number = int(input("Enter course id number: "))
                course = manager.find_course_id(id_number)
                print(f"Here is the course: {course}")
            case '6':
                print("You caught us on this one. Working on it")
                #manager.view_grade()
            case '7':
                print("Logging out...\n")
                break
            case _:
                print("Invalid option. Please select a valid option (1-4).")




def teacher_menu():
    manger = StudentManagementSystem()
    while True:
        print("""
            --- Teacher Menu ---
            1. Add course
            2. Remove course
            3. Grade Students
            4. Log out
        """)
        choice = input("Enter your choice 1- 4: ").strip()
        match choice:
            case '1':
                course = input("Enter course name: ")
                manger.add_course(course)
            case '2':
                course = input("Enter course name: ")
                manger.remove_course(course)
            case '3':
                students = manger.get_students()
                for student in students:
                    if not student.courses:
                        print(f"Student {student.name} is not enrolled in any courses.")
                        continue

                    for course in student.courses:
                        try:
                            grade = float(input(f"Enter {student.name}'s score for {course.course_name}: "))
                            manger.grade_student(course, student, grade)
                            print(f"Grade recorded for {student.name} in {course.course_name}: {grade}")
                        except ValueError:
                            print("Invalid input. Please enter a numeric value for the grade.")



def main():
    student_grade = StudentManagementSystem()
    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-4): ").strip()

            while choice not in ['1', '2', '3', '4']:
                print("Invalid menu option. Please select a valid option (1-4).")
                choice = input("Enter your choice (1-4): ").strip()

            match choice:
                case '1':
                    print("-- Register Student --")
                    first_name = input("Enter first Name: ")
                    last_name = input("Enter last name: ")
                    email = input("Email: ")
                    password = input("Password: ")
                    #student_id = input("Student ID: ")
                    student_grade.register_student(first_name, last_name, email, password)

                case '2':
                    print("-- Register Professor --")
                    first_name = input("Enter first Name: ")
                    last_name = input("Enter last name: ")
                    email = input("Email: ")
                    password = input("Password: ")
                    #student_id = input("Student ID: ")
                    try:
                       student_grade.register_professor(first_name, last_name, email, password)
                       print(f"Professor {first_name} {last_name} registered successfully.")
                    except Exception as e:
                        print(e)


                case '3':
                    print("\n-- Login --")
                    email = input("Enter your Email: ")
                    password = input("Password: ")
                    try:
                       if student_grade.verify_student_role(password, email):
                           student_grade.login_in_student(email, password)
                           student_menu()
                       if student_grade.verify_teacher_role(password, email):
                           student_grade.login_in_teacher(email, password)
                           teacher_menu()
                    except Exception as e:
                        print("Error:", e)


                case '4':
                    print("Exiting... Goodbye!\nThanks for using this app")
                    return

                case _:
                    print("Invalid option. Please select a valid option (1-4).")
                    choice = input("Enter your choice (1-4): ").strip()

        except Exception as e:
            print(e)




if __name__ == "__main__":
    main()
