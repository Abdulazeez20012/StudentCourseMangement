import unittest
from grade import Grade
from grade_type import GradeType


class MockCourse:
    def __init__(self, course_name):
        self.course_name = course_name


class MockStudent:
    def __init__(self, name):
        self.name = name


class TestGrade(unittest.TestCase):
    def setUp(self):
        self.course = MockCourse("Python Programming")
        self.student = MockStudent("Abdul Azeez")

    def test_that_can_creates_a_Grade_object_with_a_numeric_grade_of_85(self):
        grade = Grade(self.course, self.student, 85.0)
        expected = GradeType.from_numeric(85.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_can_set_a_grade_object_with_70_then_updates_it_to_90(self):
        grade = Grade(self.course, self.student, 70.0)
        grade.set_numeric_grade(90.0)
        expected = GradeType.from_numeric(90.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_95_correctly_converts_to_an_A_grade(self):
        grade = Grade(self.course, self.student, 95.0)
        expected = GradeType.from_numeric(95.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_80_correctly_converts_to_an_B_grade(self):
        grade = Grade(self.course, self.student, 80.0)
        expected = GradeType.from_numeric(80.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_70_correctly_converts_to_an_c_grade(self):
        grade = Grade(self.course, self.student, 70.0)
        expected = GradeType.from_numeric(70.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_50_correctly_converts_to_an_F_grade(self):
        grade = Grade(self.course, self.student, 50.0)
        expected = GradeType.from_numeric(50.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_edge_of_A_range_89point9_should_still_be_a_B_if_A_starts_at_90(self):
        grade = Grade(self.course, self.student, 89.9)
        expected = GradeType.from_numeric(89.9)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_edge_of_B_range_79point9_should_still_be_a_B_if_C_starts_at_80(self):
        grade = Grade(self.course, self.student, 79.9)
        expected = GradeType.from_numeric(79.9)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_edge_of_C_range_69point9_should_still_be_a_B_if_D_starts_at_70(self):
        grade = Grade(self.course, self.student, 69.9)
        expected = GradeType.from_numeric(69.9)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_negative_grade_input_should_return_lowest_possible_grade(self):
        grade = Grade(self.course, self.student, -5.0)
        expected = GradeType.from_numeric(-5.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_numeric_grade_above_100(self):
        grade = Grade(self.course, self.student, 105.0)
        expected = GradeType.from_numeric(105.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_zero_numeric_grade(self):
        grade = Grade(self.course, self.student, 0.0)
        expected = GradeType.from_numeric(0.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_non_numeric_grade_input_raises_exception(self):
        with self.assertRaises(TypeError):
            Grade(self.course, self.student, "Ninety")

    def test_large_negative_numeric_grade(self):
        grade = Grade(self.course, self.student, -100.0)
        expected = GradeType.from_numeric(-100.0)
        actual = grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")



if __name__ == '__main__':
    unittest.main()