import re

class Authentication:

    @staticmethod
    def validate_name(name,element:str):
        if name is None or not re.fullmatch('[a-zA-Z]+', name) or len(name) < 2:
            raise ValueError(f"Invalid {element}.\nYour name must contain only letters and the length must be greater than 2")
        return name

    @staticmethod
    def validate_email(email):
        if email is None or not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email")
        return email

    @staticmethod
    def validate_password(password):
        if password is None or not re.fullmatch(r'[A-Za-z0-9\-!$%^@&*()_+|~=`{}\[\]:";\'<>?,.]{8,16}', password):
            raise ValueError("Invalid password.\nYour password must contain at least 8 characters and max 16 characters.  ")
        return password