class Employee:
    def __init__(self, id=0, name='', designation=''):
        self.id = id
        self.name = name
        self.designation = designation
    
    def printInfo(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')
        print(f'Designation: {self.designation}')

class Manager(Employee):
    def __init__(self, id=0, name='', designation='', department=''):
        super().__init__(id, name, designation)
        self.department = department
    
    def printInfo(self):
        super().printInfo()
        print(f'Department: {self.department}')

class TeamLead(Employee):
    def __init__(self, id=0, name='', designation='', project=''):
        super().__init__(id, name, designation)
        self.project = project
    
    def printInfo(self):
        super().printInfo()
        print(f'Project: {self.project}')

class Clerk(Employee):
    def __init__(self, id=0, name='', designation='', section=''):
        super().__init__(id, name, designation)
        self.section = section
    
    def printInfo(self):
        super().printInfo()
        print(f'Section: {self.section}')

m = Manager(123, 'John', 'Manager', 'IT')
m.printInfo()

t = TeamLead(456, 'Jane', 'Team Lead', 'Project A')
t.printInfo()

c = Clerk(789, 'Doe', 'Clerk', 'Section 1')
c.printInfo()
