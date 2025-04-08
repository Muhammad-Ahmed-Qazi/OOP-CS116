from abc import abstractmethod, ABC

class Person(ABC):
    def __init__(self, n, a, g, addr):
        self.name = n
        self.age = a
        self.gender = g
        self.address = addr
    
    @abstractmethod
    def show_data(self):
        pass
    def personal_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}")
    
class Student(Person):
    def __init__(self, n, a, g, addr, batch, dept):
        super().__init__(n, a, g, addr)
        self.batch = batch
        self.dept = dept
    
    def show_data(self):
        super().personal_info()
        print(f"Batch: {self.batch}, Department: {self.dept}")
    
    def cod(self):
        pass

    def has_scholarship(self):
        pass

class Teacher(Person):
    def __init__(self, n, a, g, addr):
        pass