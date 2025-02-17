class BankAccount:
    def __init__(self, accountNum=0):
        self.accountNumber = accountNum
    
    def printInfo(self):
        print(f'Account Number: {self.accountNumber}')

class SavingAccount(BankAccount):
    def __init__(self, accountNum=0, minBalance=0.0, interestRate=0.0):
        super().__init__(accountNum)
        self.minimumBalance = minBalance
        self.interestRate = interestRate
    
    def printInfo(self):
        super().printInfo()
        print(f'Minimum Balance: {self.minimumBalance}')
        print(f'Interest Rate: {self.interestRate}')

class CurrentAccount(BankAccount):
    def __init__(self, accountNum=0, withdrawalLimit=0.0):
        super().__init__(accountNum)
        self.withdrawalLimit = withdrawalLimit
    
    def printInfo(self):
        super().printInfo()
        print(f'Withdrawal Limit: {self.withdrawalLimit}')

s = SavingAccount(123, 1000.0, 0.05)
s.printInfo()

c = CurrentAccount(456, 500.0)
c.printInfo()