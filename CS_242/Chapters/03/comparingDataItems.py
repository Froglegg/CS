class SavingsAccount(object):
    ''' demo for defining comparison operators within a Class' methods '''

    def __init__(self, name, PIN, balance=0.0) -> None:
        super().__init__()
        self.name = name
        self.PIN = PIN
        self.balance = balance

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name


s1 = SavingsAccount("ken", 123, 0)
s2 = SavingsAccount("bill", 321, 30)
print(s1 < s2)
print(s2 < s1)
s3 = SavingsAccount("ken", 123, 0)
print(s1 == s3)
