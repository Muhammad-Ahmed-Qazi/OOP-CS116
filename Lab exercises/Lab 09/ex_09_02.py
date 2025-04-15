def zero_division(func):
    """
    Decorator to handle division by zero errors.
    """
    def wrapper(num1, num2):
        if num2 == 0:
            return print("Error: Division by zero is not allowed.")
        return func(num1, num2)
    return wrapper

@zero_division
def divide_two_numbers(num1, num2):
    print(f'The result of dividing {num1} by {num2} is: {num1 / num2}')

# Main program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

divide_two_numbers(num1, num2)

""" Output:

Enter the first number: 5
Enter the second number: 2
The result of dividing 5.0 by 2.0 is: 2.5

Enter the first number: 5
Enter the second number: 0
Error: Division by zero is not allowed.

"""