import os
import unittest
from unittest.mock import patch

from student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("Password1.")
        self.test_file = "student_details.txt"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_register(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com"]):
            self.student1.register("Mercy","Babayemi","mercy.babayemi@example.com","Password1.")
            self.assertTrue(os.path.exists(self.test_file))

    def test_login_success(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com"]):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com","Password1.")

        with patch('builtins.input', side_effect=["mercy.babayemi@example.com", "Password1."]):
            self.assertTrue(self.student1.login("mercy.babayemi@example.com","Password1."))

    def test_login_failure(self):
        with patch('builtins.input', side_effect=["Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1."]):
            self.student1.register("Mercy", "Babayemi", "mercy.babayemi@example.com", "Password1.")

        with patch('builtins.input', side_effect=["mercy.babayemi@example.com", "WrongPassword"]):
            self.assertFalse(self.student1.login("mercy.babayemi@example.com", "wrongPassword"))

    def test_register_for_course(self):
        self.student1.register_for_course("Mathematics")
        self.assertIn("Mathematics", self.student1.enrolled_courses)

    def test_view_courses(self):
        self.student1.register_for_course("Mathematics")
        self.student1.register_for_course("Physics")
        with patch('builtins.print') as mock_print:
            self.student1.view_courses()
            mock_print.assert_any_call("Your enrolled courses:")
            mock_print.assert_any_call("- Mathematics")
            mock_print.assert_any_call("- Physics")

    def test_view_course_grade(self):
        self.student1.grades["Mathematics"] = "A"
        with patch('builtins.print') as mock_print:
            self.student1.view_course_grade("Mathematics")
            mock_print.assert_called_with("Your grade for Mathematics is A.")

    # def test_save_to_file(self):
    #     self.student1.first_name = "Mercy"
    #     self.student1.last_name = "Janet"
    #     self.student1.email = "mercy.babayemi@example.com"
    #     self.student1.save_to_file()
    #
    #     with open(self.test_file, "r") as file:
    #         content = file.read()
    #         self.assertIn("Mercy:Janet:mercy.babayemi@example.com:", content)
    #
    # def test_load_from_file_success(self):
    #     self.student1.first_name = "John"
    #     self.student1.last_name = "Doe"
    #     self.student1.email = "john.doe@example.com"
    #     self.student1.save_to_file()
    #     self.assertTrue(self.student1.load_from_file("Password1.", "john.doe@example.com"))
    #
    # def test_load_from_file_failure(self):
    #     self.student1.first_name = "John"
    #     self.student1.last_name = "Doe"
    #     self.student1.email = "john.doe@example.com"
    #     hashed_pass = self.student1.hashed_password("Password1.")
    #     self.student1.save_to_file()
    #     self.assertFalse(self.student1.load_from_file("WrongPassword", "john.doe@example.com"))

if __name__ == '__main__':
    unittest.main()
