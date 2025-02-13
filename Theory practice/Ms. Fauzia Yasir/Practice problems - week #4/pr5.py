class Employee:
    """
    A class to represent an employee.
    Attributes
    ----------
    emp_id : int
        Unique identifier for the employee (default is 0).
    emp_name : str
        Name of the employee (default is an empty string).
    emp_salary : float
        Salary of the employee (default is 0.0).
    emp_department : str
        Department of the employee (default is an empty string).
    Methods
    -------
    calculate_emp_salary(salary, hours_worked):
        Calculates the employee's salary based on hours worked. If hours worked exceed 50, 
        additional pay is added for the extra hours.
    emp_assign_department(department):
        Assigns a department to the employee.
    print_employee_details():
        Prints the details of the employee.
    """
    def __init__(self, emp_id=0, emp_name="", emp_salary=0.0, emp_department=""):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    
    # No instruction to write setters and getters for emp_id, emp_name, emp_salary, emp_department

    def calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            return salary + (hours_worked - 50) * (salary / 50)
        return salary

    def emp_assign_department(self, department):
        self.emp_department = department
    
    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")


# Creating an employee object
emp1 = Employee(1, "John Doe", 5000, "HR")

# Assigning a new department
emp1.emp_assign_department("Finance")

# Calculating salary based on hours worked
print(f'Salary: {emp1.calculate_emp_salary(emp1.emp_salary, 55)}')

# Printing employee details
emp1.print_employee_details()