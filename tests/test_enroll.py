import os
import unittest
from enroll import Enrollment
from course import Course

class TestEnrollment(unittest.TestCase):

    def setUp(self):
        self.enrollment = Enrollment()
        self.enrollment.course = Course()
        if os.path.isfile("../data/enrolled_courses.txt"):
            os.remove("../data/enrolled_courses.txt")

    def tearDown(self):
        if os.path.isfile("../data/enrolled_courses.txt"):
            os.remove("../data/enrolled_courses.txt")

    def test_that_can_enroll_valid_course(self):
        self.enrollment.course.courses = {1: "python", 2: "java"}
        self.enrollment.enroll("ighoe571@gmail.com","python")
        self.assertIn("python", self.enrollment.view_enrolled_courses())

    def test_that_enroll_invalid_course_raise_exception(self):
        self.enrollment.course.courses = {1: "python", 2: "java"}
        with self.assertRaises(Exception):
            self.enrollment.enroll("ighoe571@gmail.com",'jango')

    def test_that_enrolled_courses_should_remove_after_un_enrolled(self):
        self.enrollment.course.courses = {1: "python", 2: "java"}
        self.enrollment.enroll("ighoe571@gmail.com","java")
        self.enrollment.un_enroll("ighoe571@gmail.com","java")
        self.assertNotIn("python", self.enrollment.view_enrolled_courses())

    def test_that_can_view_enrolled_courses(self):
        self.enrollment.course.courses = {1: "python", 2: "java"}
        self.enrollment.enroll("ighoe571@gmail.com","python")
        self.assertEqual(self.enrollment.view_enrolled_courses(), ["python"])

if __name__ == "__main__":
    unittest.main()
