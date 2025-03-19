import unittest


from user import User

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.user_class = User("Mercy","Babayemi","mercy@gmail.com","Password1.")

    def test_that_user_class_returns_correct_firstname(self):
        self.assertEqual("Mercy", self.user_class.first_name)

    def test_that_user_class_asserts_false_if_first_name_is_empty(self):
        self.assertFalse(self.user_class.first_name == " ")

    def test_that_user_class_returns_correct_lastname(self):
        self.assertEqual("Babayemi", self.user_class.last_name)

    def test_that_user_class_asserts_false_if_last_name_is_empty(self):
        self.assertFalse(self.user_class.last_name == " ")

    def test_that_user_class_returns_correct_email(self):
        self.assertEqual("mercy@gmail.com", self.user_class.email)

    def test_that_user_class_asserts_false_if_email_is_empty(self):
        self.assertFalse(self.user_class.email == " ")

    def test_that_user_class_returns_correct_password(self):
        self.assertEqual("Password1.", self.user_class.get_password())

    def test_that_user_class_asserts_false_if_password_is_empty(self):
        self.assertFalse(self.user_class.get_password() == " ")


if __name__ == '__main__':
    unittest.main()
