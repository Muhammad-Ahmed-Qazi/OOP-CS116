class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Main program
if __name__ == "__main__":
    # Create two points
    p1 = Point(3, 4)
    p2 = Point(1, 2)

    # Print the points
    print("Point 1:", p1)
    print("Point 2:", p2)

""" Output:

Point 1: (3, 4)
Point 2: (1, 2)

"""