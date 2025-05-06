class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

# Example usage
if __name__ == "__main__":
    radius = float(input("Enter the radius of the circle: "))
    circle1 = Circle(radius)

    radius = float(input("Enter the radius of another circle: "))
    circle2 = Circle(radius)

    # Compare the two circles
    print("Is circle1 smaller than circle2?", circle1 < circle2)
    print("Is circle1 larger than circle2?", circle1 > circle2)

""" Output:



"""