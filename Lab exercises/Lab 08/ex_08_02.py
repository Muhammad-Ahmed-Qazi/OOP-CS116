from abc import abstractmethod, ABC

class Super(ABC):
    def delegate(self):
        self.action()
    
    @abstractmethod
    def action(self):
        pass

class Sub(Super):
    def action(self):
        print("Action performed in Sub class")

X = Sub()
X.action()

"""
The error occurs because the abstract method 'action' is not implemented in the subclass 'Sub'.
To solve the error, we need to implement the 'action' method in the 'Sub' class.
"""