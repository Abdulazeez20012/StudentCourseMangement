import unittest
from authentication import Authentication

class MyTestCase(unittest.TestCase):

    def test_that_name_validates(self):
        self.authentication = Authentication()
        self.assertEqual(self.authentication.validate_name("Name"), "Name")

    def test_that_email_validates(self):
        self.authentication = Authentication()
        self.assertEqual(self.authentication.validate_email("mercy@gmail.com"), "mercy@gmail.com")

    def test_that_validate_email_throws_exception(self):
        self.authentication = Authentication()
        with self.assertRaises(Exception):
            self.authentication.validate_email("EMAIL")

    def test_that_password_validates(self):
        self.authentication = Authentication()
        self.assertEqual(self.authentication.validate_password("Password1."), "Password1.")

    def test_that_validate_password_throws_exception(self):
        self.authentication = Authentication()
        with self.assertRaises(Exception):
            self.authentication.validate_password("Pass")

if __name__ == '__main__':
    unittest.main()
