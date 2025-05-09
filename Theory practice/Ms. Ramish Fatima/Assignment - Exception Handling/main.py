from classes import Point, Line, DuplicatePointError, DuplicateLineError, InvalidLineError

class GeometryApp:
    def __init__(self):
        self.points = []
        self.lines = []
        self.run()

    def run(self):
        menu_actions = {
            '1': self.handle_add_point,
            '2': self.handle_add_line,
            '3': self.handle_distance,
            '4': self.handle_length,
            '5': self.handle_slope,
            '6': self.print_points,
            '7': self.print_lines,
            '8': self.exit_program
        }

        while True:
            choice = self.menu()
            action = menu_actions.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")

    def handle_add_point(self):
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
            self.handle_unexpected_error()

    def handle_add_line(self):
        if len(self.points) < 2:
            print("At least two points are required to create a line. Please add another point.")
            return
        points = self.get_points()
        if points:
            try:
                self.add_line(points[0], points[1])
            except (DuplicateLineError, InvalidLineError) as e:
                print(e)
            except:
                self.handle_unexpected_error()

    def handle_distance(self):
        if len(self.points) < 2:
            print("At least two points are required to compare. Please add another point.")
            return
        points = self.get_points()
        if points:
            try:
                distance = points[0].distance_to(points[1])
                print(f"Distance between {points[0]} and {points[1]} is {distance}.")
            except:
                self.handle_unexpected_error()

    def handle_length(self):
        if not self.lines:
            print("No lines available. Please add a line.")
            return
        line = self.get_line()
        if line:
            try:
                print(f"Length of {line} is {line.length()}.")
            except:
                self.handle_unexpected_error()

    def handle_slope(self):
        if not self.lines:
            print("No lines available. Please add a line.")
            return
        line = self.get_line()
        if line:
            try:
                print(f"Slope of {line} is {line.slope()}.")
            except ValueError as e:
                print(e)
            except:
                self.handle_unexpected_error()

    def add_point(self, x, y):
        point = Point(x, y)
        if point in self.points:
            raise DuplicatePointError(x, y)
        self.points.append(point)
        print(f"Point {point} added.")

    def add_line(self, point1, point2):
        if point1 == point2:
            raise InvalidLineError(point1, point2)
        line = Line(point1, point2)
        if line in self.lines:
            raise DuplicateLineError(point1, point2)
        self.lines.append(line)
        print(f"{line} added.")

    def print_points(self):
        if not self.points:
            print("No points available.")
        else:
            for i, point in enumerate(self.points, start=1):
                print(f"{i}. {point}")

    def print_lines(self):
        if not self.lines:
            print("No lines available.")
        else:
            for i, line in enumerate(self.lines, start=1):
                print(f"{i}. {line}")

    def get_point(self, prompt):
        index = self.prompt_index(prompt, len(self.points))
        if index is not None:
            return self.points[index]
        return None

    def get_line(self):
        self.print_lines()
        index = self.prompt_index("Select the line: ", len(self.lines))
        if index is not None:
            return self.lines[index]
        return None

    def get_points(self):
        self.print_points()
        p1 = self.get_point("Select the first point: ")
        p2 = self.get_point("Select the second point: ")
        if p1 and p2:
            return (p1, p2)
        return None

    def prompt_index(self, prompt, max_index):
        try:
            index = int(input(prompt)) - 1
            if 0 <= index < max_index:
                return index
            else:
                print("Invalid line selection. Please select a line in the range of given options.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        return None

    def handle_unexpected_error(self):
        print("An unexpected error occurred.")

    def exit_program(self):
        print("Exiting the program.")
        exit()

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

if __name__ == "__main__":
    try:
        app = GeometryApp()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting the program.")
    except:
        print("An unexpected error occurred.")
