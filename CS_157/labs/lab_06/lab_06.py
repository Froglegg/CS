class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " + str(self.staffnumber)


x = Person("Sammy", "Student")
y = Employee("Penny", "Peters", "805")


class PartTime(Employee):

    def __init__(self, first, last, staffnum, hourlyRate):
        Employee.__init__(self, first, last, staffnum)
        self.hourlyRate = hourlyRate

    def GetEmployee(self):
        return f"{Employee.GetEmployee(self)}, is a part time employee who makes: {str(self.hourlyRate)}"
        # Modify the above code by deriving a new class from class Employee named as class 	PartTime and derive some objects based on this new class.


partTimeEmployee = PartTime("Hayes", "Crowley", 123, 18.00)
partTimeEmployee.GetEmployee()
