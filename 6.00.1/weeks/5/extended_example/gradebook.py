class Gradebook(object):
    def __init__(self):
        self.students = []
        self.grades = {}
        self.isSorted = True

    def add_student(self, student):
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.getId()] = []
        self.isSorted = False
