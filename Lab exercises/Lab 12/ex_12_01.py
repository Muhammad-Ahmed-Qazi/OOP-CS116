class Vector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"{self.i}i+{self.j}j"

# Main program
if __name__ == "__main__":
    # Create two vectors
    c1 = Vector(3, 4)
    c2 = Vector(1, 2)

    # Print the vectors
    print("Vector 1:", c1)
    print("Vector 2:", c2)

""" Output:

Vector 1: 3i+4j
Vector 2: 1i+2j

"""