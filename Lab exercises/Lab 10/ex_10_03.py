from abc import ABC, abstractmethod

class Person:
    def ticket_price(self):
        pass

class Student(Person):
    def ticket_price(self):
        return 5.0

class Employed_person(Person):
    def ticket_price(self):
        return 10.0

# Main program
s = Student()
e = Employed_person()

print("Student ticket price: $", s.ticket_price())
print("Employed person ticket price: $", e.ticket_price())