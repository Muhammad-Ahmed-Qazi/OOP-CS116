class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other_point):
        return isinstance(other_point, Point) and self.x == other_point.x and self.y == other_point.y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def distance_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
    
class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
    
    def __str__(self):
        return f"Line from {self.start_point} to {self.end_point}"
    
    def __eq__(self, other_line):
        return isinstance(other_line, Line) and (self.start_point == other_line.start_point and self.end_point == other_line.end_point) or (self.start_point == other_line.end_point and self.end_point == other_line.start_point)
    
    def length(self):
        return self.start_point.distance_to(self.end_point)
    
    def slope(self):
        if self.end_point.x - self.start_point.x == 0:
            raise ValueError("Slope is undefined for vertical lines.")
        return (self.end_point.y - self.start_point.y) / (self.end_point.x - self.start_point.x)

# Custom exception: DuplicatePointError
class DuplicatePointError(Exception):
    def __init__(self, x, y):
        self.message = f"Point with coordinates ({x}, {y}) already exists. Duplicate points are not allowed."
        super().__init__(self.message)

class DuplicateLineError(Exception):
    def __init__(self, start_point, end_point):
        self.message = f"Line from {start_point} to {end_point} already exists. Duplicate lines are not allowed."
        super().__init__(self.message)

class InvalidLineError(Exception):
    def __init__(self, start_point, end_point):
        self.message = f"Invalid line from {start_point} to {end_point}. Lines must have different start and end points."
        super().__init__(self.message)