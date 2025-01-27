class ComplexNumber:
    def setNumber(self):
        self.real = float(input("Enter the real part of the complex number: "))
        self.imaginary = float(input("Enter the imaginary part of the complex number: "))
    
    def displayNumber(self):
        print("The complex number is: ", self.real, "+", self.imaginary, "j")