class TollBooth:
    def __init__(self):
        self.numCar = 0
        self.totalAmt = 0.0

    def payingCar(self):
        self.numCar += 1
        self.totalAmt += 50.0
    
    def nonPayingCar(self):
        self.numCar += 1
    
    def display(self):
        print("Number of cars passed: ", self.numCar)
        print("Total amount collected: Rs.", self.totalAmt)
        print("No. of defaulters: ", self.numCar - (self.totalAmt / 50.0))

toll = TollBooth()
while True:
    print("-'p': Paying Car\n-'n': Non-Paying Car\n-'d': Display\n-'e': Exit")
    choice = input("Enter your choice: ")
    
    if choice == "p":
        toll.payingCar()
    elif choice == "n":
        toll.nonPayingCar()
    elif choice == "d":
        toll.display()
    elif choice == "e":
        print("Exiting program!")
        break
    else:
        print("Invalid choice!")
