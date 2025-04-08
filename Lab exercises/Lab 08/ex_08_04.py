from abc import abstractmethod, ABC

class MathOperation(ABC):
    def __init__(self):
        self.a = float(input("Enter first operand: "))
        self.b = float(input("Enter second operand: "))
    
    @abstractmethod
    def operation(self):
        pass

class Addition_operation(MathOperation):
    def __init__(self):
        super().__init__()

    def operation(self):
        return self.a + self.b

class Subtraction_operation(MathOperation):
    def __init__(self):
        super().__init__()
    
    def operation(self):
        return self.a - self.b

class Multiplication_operation(MathOperation):
    def __init__(self):
        super().__init__()
    
    def operation(self):
        return self.a * self.b

class Division_operation(MathOperation):
    def __init__(self):
        super().__init__()
    
    def operation(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

# Main program
while True:
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        operation = Addition_operation()
        result = operation.operation()
        print(f"Result: {result}")
    elif choice == '2':
        operation = Subtraction_operation()
        result = operation.operation()
        print(f"Result: {result}")
    elif choice == '3':
        operation = Multiplication_operation()
        result = operation.operation()
        print(f"Result: {result}")
    elif choice == '4':
        operation = Division_operation()
        result = operation.operation()
        print(f"Result: {result}")
    elif choice == '5':
        break
    else:
        print("Invalid input")