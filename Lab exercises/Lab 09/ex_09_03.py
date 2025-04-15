def print_x(func):
    """
    Decorator to print X to the console.
    """
    def wrapper():
        print("X" * 5)
        func()
        print("X" * 5)
    return wrapper

def print_y(func):
    """
    Decorator to print Y to the console.
    """
    def wrapper():
        print("Y" * 5)
        func()
        print("Y" * 5)
    return wrapper

@print_x
@print_y
def main():
    """
    Main function to demonstrate the use of decorators.
    """
    print("Hello")

# Main program
if __name__ == "__main__":
    main()

""" Output:

XXXXX
YYYYY
Hello
YYYYY
XXXXX

"""