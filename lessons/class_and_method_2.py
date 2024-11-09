import math


class Circle:
    radius: float

    def __init__(self, r: float):
        """Initialize the radius of the circle"""
        self.radius = r

    def area(self) -> float:  # area is the method
        """Calculate area based on radius"""
        return (self.radius**2) * math.pi


circ: Circle = Circle(r=2.0)
print(circ.area())


class Rectangle:
    width: float
    height: float

    def __init__(self, w: float, h: float):
        """Initialize the width and height of a rectangular"""
        self.width = w
        self.height = h

    def area(self) -> float:
        """Calculate area based on width and height"""
        return self.width * self.height


rect: Rectangle = Rectangle(w=4.0, h=5.5)
print(rect.area())
