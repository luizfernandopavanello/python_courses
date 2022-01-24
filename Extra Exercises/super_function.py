"""
→ super() = Function used to give access to the methods of a parent class;
            Returns a temporary object of a parent class when used
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Square(Rectangle):

    def __init__(self, length, width):
       super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

rectangle = Rectangle(3, 3)
square = Square(2, 2)
cube = Cube(3, 3, 3)

print(rectangle.area())
print(square.area())
print(cube.volume())



