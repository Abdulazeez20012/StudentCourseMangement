from authentication import Authentication

class User:
    def __init__(self, first_name,last_name,email,password):
        self.__email = email
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def __first_name(self) -> str:
        return self.first_name

    @__first_name.setter
    def __first_name(self, value) -> None:
        self.first_name = value

    @property
    def __last_name(self) -> str:
        return self.last_name

    @__last_name.setter
    def __last_name(self, value) -> None:
        self.last_name = value

    @property
    def __email(self) -> str:
        return self.email

    @__email.setter
    def __email(self, value) -> None:
        self.email = value

    def get_password(self) -> str:
        return self.__password

    def register(self,first_name,last_name,email, password) -> None:
        raise NotImplementedError("Subclass must implement register method.")

    def login(self,email,password) -> None:
        raise NotImplementedError("Subclass must implement login method.")

    def view_courses(self) -> None:
        raise NotImplementedError("Subclass must implement view courses method.")




