import datetime

class User:
    def __init__(self, name):
        self.account_number = generate_account_number()
        self.name = name
        self.balance = 0.0
        self.transaction_history = []
        self.loan_amount = 0.0

    def generate_account_number(self):
        # Generate a unique account number based on some logic
        # This is just a placeholder implementation
        return hash(self.name) % 10000

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
            print("Loan already taken. Please repay your existing loan to request a new loan.")

    def is_bankrupt(self):
        if self.balance <= 0:
            return True
        return False
