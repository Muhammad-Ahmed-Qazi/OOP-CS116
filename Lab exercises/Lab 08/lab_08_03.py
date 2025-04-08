from abc import abstractmethod, ABC

class Polygon(ABC):
    @abstractmethod
    def noOfSides(self):
        pass

