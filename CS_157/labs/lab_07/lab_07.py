class Student:
    Scores = {}

    # initializing the constructor method
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getScores(self):
        # begin function to obtain scores #
        answer_key = []
        # read into answer_key list, the answer key from file
        answer_key = [line.strip() for line in open("answers.txt", 'r')]

        student_answers = []
        # read into student_answers list, student answers from file
        student_answers = \
            [line.strip().split(',') for line in open("data.txt", 'r')]

        total_score = 100

        for student in student_answers:
            if self.name in student:
                for idx, el in enumerate(student[1:]):
                    if el != answer_key[idx]:
                        total_score -= 10

        Student.Scores[self.getName()] = total_score

    def getName(self):
        return self.name

    @ staticmethod
    def sortDict():
        return sorted(Student.Scores.items())


student_objs = [
    Student("Sammy Student", 65),
    Student("Betty Sanchez", 45),
    Student("Alice Brown", 100),
    Student("Tom Schulz", 50),
    Student("Richard Hayes Crowley", 0)
]

for index in range(len(student_objs)):
    student_objs[index].getScores()


sortList = Student.sortDict()

for k, v in sortList:
    print(k, "has score:", v)
