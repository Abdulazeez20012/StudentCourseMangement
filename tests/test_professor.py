import os
import unittest
from unittest.mock import patch
from professor import Professor

class TestProfessor(unittest.TestCase):

    def setUp(self):
        self.professor1 = Professor("Mercy", "Babayemi", "mercy@gmail.com", "Password1.")
        self.test_file = "../data/professor_details.txt"
        self.test_file_two = "course_details.txt"
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)
        if os.path.isfile(self.test_file_two):
            os.remove(self.test_file_two)

    def tearDown(self):
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)
        if os.path.isfile(self.test_file_two):
            os.remove(self.test_file_two)



    def test_add_course_success(self):
        self.professor1.add_course("Mathematics")
        self.assertIn("Mathematics", self.professor1.get_courses().values())

    def test_that_i_can_login_successfully(self):
            self.professor1.register("Mercy","Babayemi","mercy@gmail.com","Password1.")
            self.assertTrue(self.professor1.login("mercy@gmail.com","Password1."))

    def test_add_course_duplicate(self):
        self.professor1.add_course("Physics")
        result = self.professor1.add_course("Physics")
        self.assertEqual(result, "Course Physics already exists")

    def test_remove_course_success(self):
        self.professor1.add_course("Computer Science")
        result = self.professor1.remove_course("Computer Science")
        self.assertEqual(result, "Course 'Computer Science' removed successfully.")
        self.assertNotIn("Computer Science", self.professor1.get_courses())

    def test_view_courses(self):
        self.professor1.add_course("Mathematics")
        self.professor1.add_course("Physics")
        with patch('builtins.print') as mock_print:
            self.professor1.view_courses()
            mock_print.assert_any_call("Teaching course/courses:")
            mock_print.assert_any_call("- Mathematics")
            mock_print.assert_any_call("- Physics")

if __name__ == '__main__':
    unittest.main()