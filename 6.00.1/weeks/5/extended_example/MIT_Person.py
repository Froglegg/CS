from person import Person


class MIT_Person(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MIT_Person.nextIdNum
        MIT_Person.nextIdNum += 1

    def get_id(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum > other.idNum

    def speak(self, utterance):
        return f"{self.name} says: {utterance}"


m1 = MIT_Person("Dude Duderino")
m2 = MIT_Person("Duderino Dude")
m3 = MIT_Person("The Man!")
m1.set_birthday(6, 20, 1989)
m2.set_birthday(6, 20, 1990)
m3.set_birthday(6, 20, 1991)
mit_list = [m1, m2, m3]

m1.speak("hey")
mit_list.sort()

for p in mit_list:
    print(p)


class Professor(MIT_Person):
    def speak(self, utterance):
        return MIT_Person.speak(self, utterance + " obviously! ")


eric = Professor("eric")
eric.speak("hey it's me,")
