class Bank:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0.0
    
    def setBalance(self, amount):
        self.balance = amount
    def getBalance(self):
        return self.balance
    
    def getPassword(self):
        return self.password
    def authenticate(self, password):
        return self.password == password
    
    def deposit(self, amount):
        self.setBalance(self.getBalance() + amount)
        self.showBalance()
    
    def withdraw(self, amount):
        if self.getBalance() < amount:
            print("Insufficient balance!")
        else:
            self.setBalance(self.getBalance() - amount)
            self.showBalance()
    
    def showBalance(self):
        print("Balance: ", self.getBalance())

name = input("Enter your name: ")
password = input("Create password for your account: ")
account = Bank(name, password)
print("Account created successfully! Your starting account balance will be Rs. 0.0/-")

while True:
    print("1. Deposit\n2. Withdraw\n3. Show Balance\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        account.showBalance()
    elif choice == 4:
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice!")