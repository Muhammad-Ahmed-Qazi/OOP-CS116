class Person:
    def __init__(self, name=''):
        self.name = name
    
    def printInfo(self):
        print(f'Name: {self.name}')

class Student(Person):
    def __init__(self, name='', department='', year=0):
        super().__init__(name)
        self.department = department
        self.year = year
    
    def printInfo(self):
        super().printInfo()
        print(f'Department: {self.department}')
        print(f'Year: {self.year}')

class Teacher(Person):
    def __init__(self, name='', course=''):
        super().__init__(name)
        self.course = course
    
    def printInfo(self):
        super().printInfo()
        print(f'Course: {self.course}')

s = Student('John', 'Computer Science', 2)
s.printInfo()

t = Teacher('Jane', 'Python Programming')
t.printInfo()