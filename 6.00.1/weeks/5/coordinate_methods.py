from coordinate_class import Coordinate, c, origin

# adding a method dynamically... importing class, defining a function that binds to self (this in JS), and adding it onto the class.

# looks like I'm able to define a method on a class, and then previously defined instances inherit that method?

# deifning special operators on class


def __str__(self):
    return "<" + str(self.x) + ", " + str(self.y) + ">"


def __sub__(self, other):
    return (self.x - other.x, self.y - other.y)


Coordinate.__str__ = __str__
Coordinate.__sub__ = __sub__

print(c)
print(c.distance(origin))
print(isinstance(c, Coordinate))
foo = origin - c
print(foo)
