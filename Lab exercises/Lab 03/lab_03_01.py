# Aggregate class example

class Salary:
    def __init__(self, pay ,bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.agg_salary = salary
    
    def total_salary(self):
        return self.agg_salary.annual_salary()

salary = Salary(100000, 15000)
employee = Employee("John Doe", 30, salary)
print(f"Employee Name: {employee.name}")
print(f"Employee Age: {employee.age}")
print(f"Employee Annual Salary: {employee.total_salary()}")