class Snake:
    def introduction(self):
        self.name = input("Enter the snake's name: ")
        self.colour = input("Enter the snake's colour: ")
        self.age = int(input("Enter the snake's age: "))
        print("The snake's name is", self.name)
        print("The snake's colour is", self.colour)
        print("The snake's age is", self.age)