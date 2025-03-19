import unittest

from course import Course
from grade import Grade
from grade_type import GradeType
from student import Student


class TestGrade(unittest.TestCase):
    def setUp(self):
        self.course = Course()
        self.grade = Grade()
        self.student = Student("Abdul","Azeez","ighoe571@gmail.com","lase")

    def test_that_can_creates_a_Grade_object_with_a_numeric_grade_of_85(self):
        self.grade.set_numeric_grade("maths","ighoe571@gmail.com",85.9)
        expected = GradeType.convert_score_to_grade_type(85.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_can_set_a_grade_object_with_70_then_updates_it_to_90(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",90.0)
        expected = GradeType.convert_score_to_grade_type(90.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_95_correctly_converts_to_an_A_grade(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",95.0)
        expected = GradeType.convert_score_to_grade_type(95.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_80_correctly_converts_to_an_B_grade(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",80.0)
        expected = GradeType.convert_score_to_grade_type(80.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_70_correctly_converts_to_an_c_grade(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",70.0)
        expected = GradeType.convert_score_to_grade_type(70.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_to_Check_if_50_correctly_converts_to_an_F_grade(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",50.0)
        expected = GradeType.convert_score_to_grade_type(50.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_edge_of_A_range_89point9_should_still_be_a_B_if_A_starts_at_90(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",89.9)
        expected = GradeType.convert_score_to_grade_type(89.9)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_edge_of_B_range_79point9_should_still_be_a_B_if_C_starts_at_80(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",79.9)
        expected = GradeType.convert_score_to_grade_type(79.9)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_edge_of_C_range_69point9_should_still_be_a_B_if_D_starts_at_70(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",69.9)
        expected = GradeType.convert_score_to_grade_type(69.9)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_negative_grade_input_should_return_lowest_possible_grade(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",-5.0)
        expected = GradeType.convert_score_to_grade_type(-5.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_numeric_grade_above_100(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",105.0)
        expected = GradeType.convert_score_to_grade_type(105.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_zero_numeric_grade(self):
        self.grade.set_numeric_grade("physics", "ighoe571@gmail.com", 0.0)
        expected = GradeType.convert_score_to_grade_type(0.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")

    def test_that_non_numeric_grade_input_raises_exception(self):
        with self.assertRaises(TypeError):
            self.grade.set_numeric_grade("physics","ighoe571@gmail.com","fourteen")

    def test_large_negative_numeric_grade(self):
        self.grade.set_numeric_grade("physics","ighoe571@gmail.com",-100.0)
        expected = GradeType.convert_score_to_grade_type(-100.0)
        actual = self.grade.letter_grade
        self.assertEqual(actual, expected, f"Expected: {expected}, Actual: {actual}")



if __name__ == '__main__':
    unittest.main()