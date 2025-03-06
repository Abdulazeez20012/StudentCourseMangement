import re

import bcrypt
from email_validator import EmailNotValidError


class User:
    def __init__(self, password):
        self.__email = "email"
        self.__password = self.hashed_password(password)
        self.__first_name = "first_name"
        self.__last_name = "last_name"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = self.validate_user_firstname(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = self.validate_user_lastname(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = self.validate_user_email(value)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = self.validate_user_password(value)

    def register(self,first_name,last_name,email, password):
        raise NotImplementedError("Subclass must implement register method.")

    def login(self,email,password):
        if email == self.email and password == self.password:
            return True
        raise NotImplementedError("Subclass must implement login method.")

    def view_courses(self):
        raise NotImplementedError("Subclass must implement view courses method.")


    def hashed_password(self, password):
            try:
                password_input = self.validate_user_password(password)
                return bcrypt.hashpw(password_input.encode('utf-8'), bcrypt.gensalt())
            except ValueError:
                print("Invalid input.")


    def validate_user_password(self, password):
        if password is None or not re.fullmatch(r'[A-Za-z0-9\-!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/]{8,16}', password):
            raise ValueError("Invalid password.\nYour password must contain at least 8 characters.  ")
        return password

    def validate_user_firstname(self, firstname):
        if firstname is None or not re.fullmatch('[a-zA-Z]+', firstname):
            raise ValueError("Invalid firstname.")
        return firstname

    def validate_user_lastname(self, lastname):
        if lastname is None or not re.fullmatch('[a-zA-Z]+', lastname):
            raise ValueError("Invalid lastname.")
        return lastname

    def validate_user_email(self, email):
        if email is None or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email")
        return email

    def save_to_file(self):
        raise NotImplementedError("Subclass must implement save to file method.")

    def load_from_file(self, password, email):
        raise NotImplementedError("Subclass must implement load to file method.")

    def collect_user_password(self):
            try:
                password_input = input("""
                 Username must contain capital letters
                 Username must contain small letters
                 Username must contain at least 1 number, at least 1 punctuation and must be 8 to 16 alphanumeric - symbol long
                 Enter your password:
                 """)
                password = self.validate_user_password(password_input)
                return password
            except ValueError as e:
                print("Invalid password.")

    def collect_user_firstname(self):
            try:
                firstname_input = input("""
                     Your firstname cannot be an empty space or contain space character
                     Enter your firstname:
                  """)

                firstname = self.validate_user_firstname(firstname_input)
                return firstname
            except ValueError:
                print("Invalid firstname.")

    def collect_user_lastname(self):
            try:
                lastname_input = input("""
                     Your lastname cannot be an empty space or contain space character
                     Enter your lastname:
                 """)
                lastname = self.validate_user_lastname(lastname_input)
                return lastname
            except ValueError:
                print("Invalid lastname.")

    def collect_user_email(self):
        try:
            email_input = input("""
                     Enter a valid email address:
                 """)
            email = self.validate_user_email(email_input)
            return email
        except ValueError:
            print("Invalid email.")