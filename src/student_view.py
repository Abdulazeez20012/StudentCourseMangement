import time

from course import Course

def display(student, stored_first_name, stored_last_name,stored_email):




    print(f"""
    
        Choose from the following options (1-8) to proceed:

        1. View Courses Available
        2. Enroll in Courses
        3. View Enroll Courses
        4. Check Grade for a particular course
        5. find course by id
        6. find course id by course name
        7. Un Enroll Course
        8. Log Out
        
""")

    choice = input("Enter your choice: ")
    cases(student,choice,stored_email)
    return choice


def cases(student,choice,stored_email):
    match choice:
        case "1":
            try:
                courses = Course().get_courses()
                if courses == {}:
                    print("No courses available")
                    return
                print("Here are the courses available:")
                print("-" * 40)
                print(f"{'S/N':<5} | {'ID Number':<10} | {'Course'}")
                print("-" * 40)
                for sn, (id_number, course) in enumerate(courses.items(), start=1):
                    print(f"{sn:<5} | {id_number:<10} | {course}")
                    print("-" * 40)
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case "2":
            try:
                courses = Course().get_courses()
                if courses == {}:
                    print("No courses available")
                    return
                print("Here are the courses available:")
                print("-" * 40)
                print(f"{'S/N':<5} | {'ID Number':<10} | {'Course'}")
                print("-" * 40)
                for sn, (id_number, course) in enumerate(courses.items(), start=1):
                    print(f"{sn:<5} | {id_number:<10} | {course}")
                    print("-" * 40)
                course = input("Enter course:")
                student.enroll(course)
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')


        case "3":
            try:
                data = student.get_enrolled_courses()
                if not data:
                    print("No enrolled courses available")
                    return
                for course in data:
                    print(f"- {course}")
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')


        case "4":
            try:
                courses = Course().get_courses()
                if courses == {}:
                    print("No courses available")
                    return
                print("Here are the courses available:")
                print("-" * 40)
                print(f"{'S/N':<5} | {'ID Number':<10} | {'Course'}")
                print("-" * 40)
                for sn, (id_number, course) in enumerate(courses.items(), start=1):
                    print(f"{sn:<5} | {id_number:<10} | {course}")
                    print("-" * 40)
                course_name = input("Enter course name:")
                student.view_course_grades(course_name)
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')


        case "5":
            try:
                course = int(input("Enter course id:"))
                course_name = Course().find_course_using_id(course)
                print(f"here is the course id:{course}, and the course is:{course_name}")
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')


        case "6":
            try:
                course_name = input("Enter course name:")
                course_id = Course().find_id_by_course(course_name)
                print(f"here is the course id:{course_id}, and the course is:{course_name}")
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case '7':
            try:
                course_name = input("Enter course name:")
                student.un_enroll(course_name)
            except Exception as e:
                print(f'\033[1;31m{e}\033[0m')

        case "8":
            print_loading_message("Log out")




def print_loading_message(message, delay=0.5):
    print(message, end="", flush=True)
    for _ in range(3):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

