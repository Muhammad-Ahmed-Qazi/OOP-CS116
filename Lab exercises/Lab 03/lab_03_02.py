# Composition class example

class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary = Salary(pay, bonus)
    
    def total_salary(self):
        return self.salary.annual_salary()

emp = Employee("John Doe", 30, 5000, 2000)
print(f"Employee Name: {emp.name}")
print(f"Employee Age: {emp.age}")
print(f"Employee Annual Salary: {emp.total_salary()}")