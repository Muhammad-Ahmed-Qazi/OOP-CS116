class Bank:
    def setLoanHistory(self, loan):
        self.loan_take_previously = loan
    
    def applicationForLoan(self):
        if not self.loan_take_previously:
            print("Loan application accepted")
        else:
            print("Loan application rejected")

b1 = Bank()
b1.setLoanHistory(False)
b1.applicationForLoan()

b2 = Bank()
b2.setLoanHistory(True)
b2.applicationForLoan()