# Defining an Abstract class
from abc import abstractmethod, ABC

class A(ABC):
    @abstractmethod
    def show_class(self):
        pass

class B(A):
    def show_class(self):
        print("Class B")

class C(A):
    def show_class(self):
        print("Class C")
        
# Creating an object of an abstract class throws an error!
# a = A()
# a.show_class()

b = B()
b.show_class()

c = C()
c.show_class()
