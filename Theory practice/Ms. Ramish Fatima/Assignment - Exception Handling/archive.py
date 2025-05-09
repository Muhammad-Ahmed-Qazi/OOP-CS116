"""main.py"""
from classes import Point, Line, DuplicatePointError, DuplicateLineError, InvalidLineError

class GeometryApp:
    def __init__(self):
        self.points = list()
        self.lines = list()

        while True:
            choice = self.menu()
            if choice == '1':
                x = input("Enter x coordinate: ")
                y = input("Enter y coordinate: ")
                try:
                    x = float(x)
                    y = float(y)
                    self.add_point(x, y)
                except DuplicatePointError as e:
                    print(e)
                except ValueError:
                    print("Invalid input. Please enter numeric values for coordinates.")
                except:
                    print("An unexpected error occurred.")
            elif choice == '2':
                if len(self.points) < 2:
                    print("At least two points are required to create a line. Please add another point.")
                    continue
                points = self.get_points()
                try:
                    if points != None:
                        self.add_line(points[0], points[1])
                except DuplicateLineError as e:
                    print(e)
                except InvalidLineError as e:
                    print(e)
                except:
                    print("An unexpected error occurred.")
            elif choice == '3':
                if len(self.points) < 2:
                    print("At least two points are required to compare them together. Please add another point.")
                    continue
                points = self.get_points()
                try:
                    if points != None:
                        distance = points[0].distance_to(points[1])
                        print(f"Distance between {points[0]} and {points[1]} is {distance}.")
                except:
                    print("An unexpected error occurred.")
            elif choice == '4':
                if not self.lines:
                    print("No lines available. Please add a line.")
                    continue
                line = self.get_line()
                try:
                    length = line.length()
                    print(f"Length of {line} is {length}.")
                except:
                    pass
            elif choice == '5':
                if not self.lines:
                    print("No lines available. Please add a line.")
                    continue
                line = self.get_line()
                try:
                    slope = line.slope()
                    print(f"Slope of {line} is {slope}.")
                except ValueError as e:
                    print(e)
                except:
                    pass
            elif choice == '6':
                if not self.points:
                    print("No points available.")
                else:
                    self.print_points()
            elif choice == '7':
                if not self.lines:
                    print("No lines available.")
                else:
                    self.print_lines()
            elif choice == '8':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_point(self, x, y):
        point = Point(x, y)
        
        if point not in self.points:
            self.points.append(point)
            print(f"Point {point} added.")
        else:
            raise DuplicatePointError(x, y)
    
    def add_line(self, point1, point2):
        line = Line(point1, point2)
        if line not in self.lines:
            if line.start_point == line.end_point:
                raise InvalidLineError(line.start_point, line.end_point)
            self.lines.append(line)
            print(f"{line} added.")
        else:
            raise DuplicateLineError(point1, point2)
    
    def print_points(self):
        for i in range(len(self.points)):
            print(f"{i + 1}. {self.points[i]}")
    
    def print_lines(self):
        for i in range(len(self.lines)):
            print(f"{i + 1}. {self.lines[i]}")
    
    def get_point(self, index):
        if 0 <= index < len(self.points):
            return self.points[index]
        else:
            raise IndexError("Selected point is not available.")
        
    def get_line(self):
        self.print_lines()
        line = input("Select the line: ")
        try:
            index = int(line) - 1
            if 0 <= index < len(self.lines):
                return self.lines[index]
            else:
                raise IndexError("Selected line is not available.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except IndexError:
            print("Invalid line selection. Please select a line in the range of given options.")
        except:
            print("An unexpected error occurred.")
    
    def get_points(self):
        self.print_points()
        point1_index = input("Select the first point: ")
        point2_index = input("Select the second point: ")
        try:
            point1_index = int(point1_index) - 1
            point2_index = int(point2_index) - 1
            points = self.get_point(point1_index), self.get_point(point2_index)
        except IndexError:
            print("Invalid point selection. Please select points in the range of given options.")
        except ValueError:
            print("Invalid input. Please enter numeric values for point selection.")
        except:
            print("An unexpected error occurred.")
        else:
            return points
    
    def menu(self):
        print("\nMenu:")
        print("1. Add Point")
        print("2. Add Line")
        print("3. Distance between Points")
        print("4. Length of Line")
        print("5. Slope of Line")
        print("6. Print Points")
        print("7. Print Lines")
        print("8. Exit")

        return input("Enter your choice: ")

app = GeometryApp()