class Circle:
    """
    A class used to represent a Circle.
    Attributes
    ----------
    radius : float
        The radius of the circle (default is 1)
    colour : str
        The colour of the circle (default is black)
    Methods
    -------
    set_radius(radius)
        Sets the radius of the circle.
    set_colour(colour)
        Sets the colour of the circle.
    get_radius()
        Returns the radius of the circle.
    get_colour()
        Returns the colour of the circle.
    circumference()
        Calculates and returns the circumference of the circle.
    area()
        Calculates and returns the area of the circle.
    """
    def __init__(self, radius=1, colour="black"):
        self.radius = radius
        self.colour = colour
    
    def set_radius(self, radius):
        self.radius = radius
    def set_colour(self, colour):
        self.colour = colour

    def get_radius(self):
        return self.radius
    def get_colour(self):
        return self.colour
    
    def circumference(self):
        return 2 * 3.14159 * self.get_radius()

    def area(self):
        return 3.14159 * (self.get_radius() ** 2)
    

circle1 = Circle()
circle2 = Circle(5, "red")

print(f"Circle 1: radius = {circle1.get_radius()}, colour = {circle1.get_colour()}, circumference = {circle1.circumference():.2f}, area = {circle1.area():.2f}")
print(f"Circle 2: radius = {circle2.get_radius()}, colour = {circle2.get_colour()}, circumference = {circle2.circumference():.2f}, area = {circle2.area():.2f}")

circle1.set_radius(3)
circle1.set_colour("blue")

print(f"Circle 1 (updated): radius = {circle1.get_radius()}, colour = {circle1.get_colour()}, circumference = {circle1.circumference():.2f}, area = {circle1.area():.2f}")