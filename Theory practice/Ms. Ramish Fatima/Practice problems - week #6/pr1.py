class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def setx(self, xcoord):
        self.x = xcoord
    
    def sety(self, ycoord):
        self.y = ycoord
    
    def get(self):
        return (self.x, self.y)
    
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"P1: {p1.get()}") # P1: (1, 2)
print(f"P2: {p2.get()}") # P2: (3, 4)

p3 = p1 + p2
print(f"P3: {p3.get()}") # P3: (4, 6)

p4 = -p1
print(f"P4: {p4.get()}") # P4: (-1, -2)