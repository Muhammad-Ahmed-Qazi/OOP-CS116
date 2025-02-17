"""
Develop a class rectangle that takes width and height as argument in default constructor and
calculates area in the same default constructor.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height

r = Rectangle(10, 20)
print(r.area)
