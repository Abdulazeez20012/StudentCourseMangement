from enum import Enum
class GradeType(Enum):
    A = 4.0
    B = 3.0
    C = 2.0
    D = 1.0
    F = 0.0
    NONE = -1.0

    @staticmethod
    def convert_score_to_grade_type(score: float) -> 'GradeType':
        if score >= 90:
            return GradeType.A
        elif score >= 80:
            return GradeType.B
        elif score >= 70:
            return GradeType.C
        elif score >= 60:
            return GradeType.D
        else:
            return GradeType.F

