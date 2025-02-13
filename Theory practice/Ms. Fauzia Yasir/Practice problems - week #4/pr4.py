class Vehicle:
    """
    A class to represent a vehicle.
    Attributes
    ----------
    colour : str
        The default color of the vehicle (class attribute).
    name : str
        The name of the vehicle.
    max_speed : int
        The maximum speed of the vehicle.
    seats : int
        The number of seats in the vehicle.
    mileage : float
        The mileage of the vehicle.
    Methods
    -------
    setName(name):
        Sets the name of the vehicle.
    setMaxSpeed(max_speed):
        Sets the maximum speed of the vehicle.
    setSeats(seats):
        Sets the number of seats in the vehicle.
    setMileage(mileage):
        Sets the mileage of the vehicle.
    getName():
        Gets the name of the vehicle.
    getMaxSpeed():
        Gets the maximum speed of the vehicle.
    getSeats():
        Gets the number of seats in the vehicle.
    getMileage():
        Gets the mileage of the vehicle.
    seating_capacity():
        Returns the seating capacity of the vehicle.
    find_fare():
        Returns the fare of the vehicle based on the number of seats.
    """
    colour = 'white'
    
    def __init__(self, name='', max_speed=0, seats=0, mileage=0.0):
        self.name = name
        self.max_speed = max_speed
        self.seats = seats
        self.mileage = mileage

    def setName(self, name):
        self.name = name
    def setMaxSpeed(self, max_speed):
        self.max_speed = max_speed
    def setSeats(self, seats):
        self.seats = seats
    def setMileage(self, mileage):
        self.mileage = mileage
    
    def getName(self):
        return self.name
    def getMaxSpeed(self):
        return self.max_speed
    def getSeats(self):
        return self.seats
    def getMileage(self):
        return self.mileage
    
    def seating_capacity(self):
        return f"The seating capacity of a {self.getName()} is {self.getSeats()} passengers."
    
    def find_fare(self):
        return f"The fare of a {self.getName()} is {self.getSeats() * 100} dollars."
    

# Creating dummy objects
vehicle1 = Vehicle("Car", 180, 5, 15.0)
vehicle2 = Vehicle("Bus", 120, 50, 8.0)

# Displaying the details of vehicle1
print(vehicle1.seating_capacity())
print(vehicle1.find_fare())

# Displaying the details of vehicle2
print(vehicle2.seating_capacity())
print(vehicle2.find_fare())