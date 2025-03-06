import bcrypt

from user import User

class Student(User):
    def __init__(self,password):
        super().__init__(password)
        self.enrolled_courses = []
        self.grades = {}


    def register(self,first_name,last_name,email,password):
        try:
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.password = password
            self.save_to_file()
        except ValueError as e:
            print(f"Error during registration: {e}")

    def login(self, email, password):
        if self.load_from_file(password, email):
            return True
        else:
            print("Invalid email or password.")
            return False

    def register_for_course(self, course_name):
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)
            print(f"Successfully enrolled in {course_name}.")
        else:
            print(f"You are already enrolled in {course_name}.")

    def view_courses(self):
        if not self.enrolled_courses:
            print("You are not enrolled in any courses.")
        else:
            print("Your enrolled courses:")
            for course in self.enrolled_courses:
                print(f"- {course}")

    def view_course_grade(self, course_name):
        if course_name in self.grades:
            print(f"Your grade for {course_name} is {self.grades[course_name]}.")
        else:
            print(f"No grade found for {course_name}.")

    def save_to_file(self):
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        with open("student_details.txt", 'a') as file:
            file.write(f'{self.first_name}:{self.last_name}:{self.email}:{hashed_password}\n')

    def load_from_file(self, password, email):
        try:
            with open("student_details.txt", 'r') as file:
                for line in file:
                    data = line.strip().split(':')
                    stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                    if email == stored_email:
                        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                            self.first_name = stored_firstname
                            self.last_name = stored_lastname
                            return True
        except FileNotFoundError:
            print("File not found.")



    def verify_email_in_file(self, email,password):
        with open("student_details.txt", 'r') as file:
            for line in file:
                data = line.strip().split(':')
                stored_firstname, stored_lastname, stored_email, stored_password = data[0], data[1], data[2], data[3]
                if email == stored_email:
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        return True

            return False



