import math

class Point:
    """
    Represents a point in 2D space.
    Used by the Circle class to define its center.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle:
    """
    Represents a Circle shape.
    Demonstrates composition by using the Point class for the center.
    """
    def __init__(self, x, y, radius):
        # Composition: The Circle 'has a' Point
        self.center = Point(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(Center={self.center}, Radius={self.radius})"
    



    