class Car:
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
    
    def sales_price(self):
        if self.sold_on is not None:
            return 3600000.0 - (.10 * self.miles)
        return 0.0
    
    def purchase_price(self):
        if self.sold_on is not None:
            return 3600000.0
        return 0.0