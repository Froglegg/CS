class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name

    def __str__(self):
        return f"Animal: {self.name}, age: {self.age}"


myAnimal = Animal(3)
myAnimal.setName("Tom")
print(myAnimal)


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return f"Cat: {self.name}, age: {self.age}"


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def getTag(self):
        return str(self.rid).zfill(3)

    def getParent1(self):
        return self.parent1

    def getParent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def speak(self):
        print("meep")

    def __str__(self):
        return f"Rabbit: {self.name}, age: {self.age}"


jelly = Cat(1)
jelly.setName("JellyBelly")
print(jelly.getName())
print(jelly)
jelly.speak()

peter = Rabbit(5)
peter.setName("Peter")
print(peter)
peter.speak()


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.setName(self, name)
        self.friends = []

    def getFriends(self):
        return self.friends

    def addFriend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def speak(self):
        print("Hello")

    def ageDiff(self, other):
        diff = self.getAge() - other.getAge()
        olderYounger = ""
        if self.age > other.age:
            olderYounger = "years older"
        else:
            olderYounger = "years younger"
        print(f"{self.getName()} is {diff} {olderYounger} than {other.getName()}")

    def __str__(self):
        return f"Person: {self.name}, age: {self.age}"


Hayes = Person("Hayes", 31)
print(Hayes)
Hayes.speak()
Bailey = Person("Bailey", 29)
Bailey.speak()
Hayes.ageDiff(Bailey)

newPeter = Rabbit(2)
cotton = Rabbit(1)
newPeter.setName("peter")
cotton.setName("cotton")
hopsy = Rabbit(0, "peter", "cotton")
hopsy.setName("Hopsy")

mopsy = newPeter + hopsy
mopsy.setName("Mopsy")

print(mopsy)
print(mopsy.getParent1())
print(mopsy.getParent2())
print(mopsy.getTag())
