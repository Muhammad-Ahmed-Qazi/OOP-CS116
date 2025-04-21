class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __lt__(self, other):
        # Compare points based on their distance from the origin
        return ((self.x**2 + self.y**2) ** 0.5) < ((other.x**2 + other.y**2) ** 0.5)

    def __gt__(self, other):
        # Compare points based on their distance from the origin
        return ((self.x**2 + self.y**2) ** 0.5) > ((other.x**2 + other.y**2) ** 0.5)
    
# Main program
if __name__ == "__main__":
    # Create two points
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    p3 = Point(5, 6)
    p4 = Point(2, 1)

    # Compare the points
    print("Is p1 < p2?", p1 < p2)
    print("Is p1 > p2?", p1 > p2)
    print("Is p3 < p4?", p3 < p4)
    print("Is p3 > p4?", p3 > p4)
