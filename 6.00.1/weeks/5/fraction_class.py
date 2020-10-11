class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def getNumer(self):
        return self.num

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)

    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)

    def convert(self):
        return self.getNumer() / self.getDenom()


fract = Fraction(2, 3)
print(fract)
test = fract + (Fraction(1, 3))
print(test)

print(test.getDenom())
print(test.convert())

testSub = fract - (Fraction(1, 3))

print(testSub)
