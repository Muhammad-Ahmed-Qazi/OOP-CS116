class Fraction:
    def __init__(self, num=0, den=1):
        if den == 0:
            print("Denominator cannot be zero!")
            return
        self.numerator = num
        self.denominator = den
    
    def setNumerator(self, num):
        self.numerator = num
    def setDenominator(self, den):
        if den == 0:
            print("Denominator cannot be zero!")
            return
        self.denominator = den
    
    def getFraction(self):
        return self.numerator, self.denominator
    
    

f = Fraction(3, 0)
        