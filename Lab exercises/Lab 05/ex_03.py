"""
Develop a class ‘Person’ that has attributes of name and age. There are two methods in the same class
to print each of the attribute (name and age). Develop another class ‘Student’ that has attributes of
student_id and roll_number. Implement a class resident for a person who is also the student.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

class Student:
    def __init__(self, student_id, roll_number):
        self.student_id = student_id
        self.roll_number = roll_number

class Resident(Person, Student):
    def __init__(self, name, age, student_id, roll_number):
        Person.__init__(self, name, age)
        Student.__init__(self, student_id, roll_number)

r = Resident("John", 20, 1234, 5678)
r.print_name()
r.print_age()