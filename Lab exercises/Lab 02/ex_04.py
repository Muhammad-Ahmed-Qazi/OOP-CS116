class Test:
    def __init__(self, name):
        self.name = name
        self.name = "Hi " + self.name + "!"
        print(self.name)

obj = Test("John")