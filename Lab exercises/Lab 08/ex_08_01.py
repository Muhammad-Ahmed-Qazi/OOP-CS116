from abc import abstractmethod, ABC

class Super(ABC):
    def delegate(self):
        self.action()
    
    @abstractmethod
    def action(self):
        pass

class Sub(Super): pass

X = Sub()

"""
The error occurs because the abstract method 'action' is not implemented in the subclass 'Sub'.
To solve the error, we need to implement the 'action' method in the 'Sub' class.
"""