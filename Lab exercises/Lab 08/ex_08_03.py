from abc import abstractmethod, ABC

class Vehicle(ABC):
    def __init__(self, wheels, color):
        self.wheels = wheels
        self.color = color
    
    @abstractmethod
    def print_info(self):
        pass

class Car(Vehicle):
    def __init__(self, wheels, color, brand, model):
        super().__init__(wheels, color)
        self.brand = brand
        self.model = model
    
    def print_info(self):
        print(f"Car: {self.brand} {self.model}, Color: {self.color}, Wheels: {self.wheels}")

class Motorcycle(Vehicle):
    def __init__(self, wheels, color, brand, eng_capacity):
        super().__init__(wheels, color)
        self.brand = brand
        self.eng_capacity = eng_capacity

    def print_info(self):
        print(f"Motorcycle: {self.brand}, Engine Capacity: {self.eng_capacity}cc, Color: {self.color}, Wheels: {self.wheels}")

class Truck(Vehicle):
    def __init__(self, wheels, color, type, load_capacity):
        super().__init__(wheels, color)
        self.type = type
        self.load_capacity = load_capacity
    
    def print_info(self):
        print(f"Truck: {self.type}, Load Capacity: {self.load_capacity} tons, Color: {self.color}, Wheels: {self.wheels}")

# Main program
if __name__ == "__main__":
    car = Car(4, "Red", "Toyota", "Corolla")
    motorcycle = Motorcycle(2, "Blue", "Yamaha", 600)
    truck = Truck(6, "Green", "Volvo", 10)

    vehicles = [car, motorcycle, truck]

    for vehicle in vehicles:
        vehicle.print_info()