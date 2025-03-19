import os
import bcrypt

class Database:
    def __init__(self, file_name):
        self.__file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                pass

    @property
    def file_name(self):
        return self.__file_name

    def save_to_file(self, first_name, last_name, email, password):
        try:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            with open(self.__file_name, 'a') as file:
                file.write(f'{first_name}:{last_name}:{email}:{hashed_password}\n')
        except Exception as e:
            print(f"\033[1;31mError saving to file: {e}\033[0m")

    def load_from_file(self, email, password):
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(':')
                    if len(data) != 4:
                        print(f"\033[1;31mInvalid data format in file: {line}\033[0m")
                        continue
                    stored_firstname, stored_lastname, stored_email, stored_password = data
                    if email == stored_email:
                        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                            return [stored_firstname, stored_lastname, stored_email, stored_password], True
                        else:
                            return [], False
                print(f"\033[1;31mEmail doesn't exist\033[0m")
                return [], False
        except Exception as e:
            print(f"\033[1;31mError loading from file: {e}\033[0m")
            return [],False

    def verify_email_exist(self, email):
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(':')
                    if len(data) != 4:
                        print(f"\033[1;31mInvalid data format in file: {line}\033[0m")
                        continue
                    stored_firstname, stored_lastname, stored_email, stored_password = data
                    if stored_email == email:
                        return True
            return False
        except Exception as e:
            print(f"\033[1;31mError verifying email: {e}\033[0m")
            return False

    def save_to_file_grades(self, course_name, student_email,grade_type):
        try:
            with open(self.__file_name, 'a') as file:
                file.write(f"{course_name}:{student_email}:{grade_type}\n")
        except Exception as e:
            print(f"\033[1;31mError saving grades to file: {e}\033[0m")

    def load_from_file_grades(self):
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    data = line.split(':')
                    if len(data) != 3:
                        print(f"\033[1;31mInvalid data format in file: {line}\033[0m")
                        continue
                    course_name, student_email,grade_type = data
                    return [course_name, student_email, grade_type]
            return []
        except Exception as e:
            print(f"\033[1;31mError loading grades from file: {e}\033[0m")
            return []