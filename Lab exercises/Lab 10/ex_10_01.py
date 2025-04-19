from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        return f"{self.name} says Meow!"

# Main program
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.talk())
print(cat.talk())