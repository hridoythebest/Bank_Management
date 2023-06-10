import datetime

class User:
    account_start_num = 1000

    def __init__(self, name):
        self.account_number = self.generate_acc_num()
        self.name = name
        self.balance = 0.0
        self.transaction_history = []
        self.loan_amount = 0.0

    def generate_acc_num(self):
        account_number = User.account_start_num
        User.account_start_num += 1
        return account_number


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.datetime.now(), "Deposit", amount))
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append((datetime.datetime.now(), "Withdrawal", -amount))
            return True
        return False

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append((datetime.datetime.now(), f"Transfer to {recipient.name}", -amount))
            recipient.transaction_history.append((datetime.datetime.now(), f"Transfer from {self.name}", amount))
            return True
        return False

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")

    def check_transaction_history(self):
        print(f"Transaction History for Account Number: {self.account_number}")
        for transaction in self.transaction_history:
            timestamp, description, amount = transaction
            print(f"{timestamp}: {description} - Amount: {amount}")

    def request_loan(self):
        if self.loan_amount == 0:
            self.loan_amount = 2 * self.balance
            self.balance += self.loan_amount
            self.transaction_history.append((datetime.datetime.now(), "Loan", self.loan_amount))
            print(f"Loan of {self.loan_amount} granted. Current balance: {self.balance}")
        else:
            print("You Took Loan Before")

    
