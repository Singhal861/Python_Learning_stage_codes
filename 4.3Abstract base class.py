from abc import ABC, abstractmethod

class Shape(ABC):
    # @abstractmethod makes down def essential to be in son class
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self, side1, side2):
        self.s1 = side1
        self.s2 = side2

    def printarea(self):
        return self.s1*self.s2



rect = Rectangle(8,9)
print(rect.printarea())


