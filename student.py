class Student:
    def __init__(self,  student_id, first, last, grade, student):
        self.grade = grade
        self.first = first
        self.last = last
        self.student_id = student_id
        student[student_id] = [first, last, grade]


    def print_student(self, student):
        print(student)
        # def grade_avg (self):


student_info = {}

p1 = Student(45, "Kaori", "gaddis", 111, student_info)
p1.print_student(student_info)
