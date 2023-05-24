# You are developing a program for a university that manages different types of courses. There are three types of courses: Course, LabCourse, and SeminarCourse. Each type of course has specific attributes and behaviors. Implement a base class called Course with derived class called LabCourse that inherits from Course. Also implement a derived class called SeminarCourse that inherits from Course. 
# Write the code for the Course, LabCourse, and SeminarCourse classes according to your attributes and methods. Provide an example usage of the classes to demonstrate inheritance and method overriding.
class Course:
    def __init__(self, code, name, credit):
        self.code = code
        self.name = name
        self.credit = credit

    def display_info(self):
        print(f"Course Code: {self.code}")
        print(f"Course Name: {self.name}")
        print(f"Course Credit: {self.credit}")

class LabCourse(Course):
    def __init__(self, code, name, credit, lab_hours):
        super().__init__(code, name, credit)
        self.lab_hours = lab_hours

    def display_info(self):
        super().display_info()
        print(f"Lab Hours: {self.lab_hours}")

class SeminarCourse(Course):
    def __init__(self, code, name, credit, speaker):
        super().__init__(code, name, credit)
        self.speaker = speaker

    def display_info(self):
        super().display_info()
        print(f"Speaker: {self.speaker}")

# Example Usage
course = Course("C001", "Introduction to Programming", 3)
course.display_info()
print("-" * 20)

lab_course = LabCourse("C002", "Advanced Programming", 4, 2)
lab_course.display_info()
print("-" * 20)

seminar_course = SeminarCourse("C003", "Data Science", 3, "John Smith")
seminar_course.display_info()
