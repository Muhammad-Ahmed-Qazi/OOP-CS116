class Point:
    """
    A class to represent a point in 2D space.
    Attributes:
    -----------
    x : int or float
        The x-coordinate of the point.
    y : int or float
        The y-coordinate of the point.
    Methods:
    --------
    __init__(x=0, y=0):
        Initializes the point with given x and y coordinates.
    setx(xcoord):
        Sets the x-coordinate of the point.
    sety(ycoord):
        Sets the y-coordinate of the point.
    get():
        Returns a tuple (x, y) representing the point's coordinates.
    move(dx, dy):
        Moves the point by dx and dy along the x and y axes, respectively.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def setx(self, xcoord):
        self.x = xcoord
    def sety(self, ycoord):
        self.y = ycoord
    
    def get(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        coords = self.get()
        self.setx(coords[0] + dx)
        self.sety(coords[1] + dy)

# Create some dummy objects
p1 = Point()
p2 = Point(3, 4)

# Output initial coordinates
print("Initial coordinates of p1:", p1.get())
print("Initial coordinates of p2:", p2.get())

# Move points
p1.move(2, 3)
p2.move(-1, -1)

# Output new coordinates
print("New coordinates of p1 after moving:", p1.get())
print("New coordinates of p2 after moving:", p2.get())