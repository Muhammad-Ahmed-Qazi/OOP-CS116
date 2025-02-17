"""
Modify the class 'square' that uses the rectangle class (defined in Exercise-1) as super class and calls
the default constructor using super key word to calculate area of square.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


s = Square(5)
print(s.area)