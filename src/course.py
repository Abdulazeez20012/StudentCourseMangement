class Course:
    def __init__(self):
        self.courses = {}
        self.course_id = 1
        self.load_courses_from_file()

    def get_courses(self) -> dict:
        return self.courses

    def add_course(self, course):
        if course not in self.courses.values():
            self.courses[self.course_id] = course
            print(f"Here is your course id: {self.course_id}")
            self.save_courses_to_file()
            self.course_id += 1
        else:
            raise Exception(f"Course {course} already exists")

    def save_courses_to_file(self):
        with open("../data/courses.txt", "a") as file:
            for course_id, course_name in self.courses.items():
                file.write(f"{course_id}:{course_name}\n")

    def load_courses_from_file(self):
        try:#
            with open("../data/courses.txt", "r") as file:
                for line in file:
                    data = line.strip().split(":")
                    if len(data) == 2:
                        course_id, course_name = data[0], data[1]
                        self.courses[int(course_id)] = course_name

                if self.courses:
                    self.course_id = max(self.courses.keys()) + 1
                else:
                    self.course_id = 1
        except FileNotFoundError:
            self.courses = {}

    def remove_course(self, input_course):
        found = False#
        for id_number, course in list(self.courses.items()):
            if input_course == course:
                del self.courses[id_number]
                found = True
                self.save_courses_to_file()
        if not found:
            raise ValueError(f"Course '{input_course}' not found")

    def remove_using_id(self, id_number):
        if id_number in self.courses:
            del self.courses[id_number]
            self.save_courses_to_file()
        else:
            raise ValueError(f"Course ID '{id_number}' not found")

    def view_course(self):
        return list(self.courses.values())


    def find_course_using_id(self, id_number):
        if id_number in self.courses:
            return self.courses.get(id_number)
        raise Exception(f"Course ID '{id_number}' not found")

    def find_id_by_course(self, course):
        for course_id, course_name in self.courses.items():
            if course_name == course:
                return course_id
        raise Exception(f"Course '{course}' not found")