class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# Main program
if __name__ == "__main__":
    # Create two points
    p1 = Point(3, 4)
    p2 = Point(1, 2)

    # Add the points
    p3 = p1 + p2

    # Print the result
    print("Sum of points:", p3)

""" Output:

Sum of points: (4, 6)

"""