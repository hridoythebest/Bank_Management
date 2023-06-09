class Admin:
    def __init__(self):
        self.bank_balance = 0.0
        self.total_loan_amount = 0.0
        self.loan_feature_enabled = True

    def create_account(self):
        # Create a new user account
        pass

    def check_bank_balance(self):
        print(f"Bank Balance: {self.bank_balance}")

    def check_loan_amount(self):
        print(f"Total Loan Amount: {self.total_loan_amount}")

    def toggle_loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled
        status = "enabled" if self.loan_feature_enabled else "disabled"
        print(f"Loan Feature {status}")

    def deposit_to_bank(self, amount):
        if amount > 0:
            self.bank_balance += amount

    def withdraw_from_bank(self, amount):
        if amount > 0 and amount <= self.bank_balance:
            self.bank_balance -= amount
            return True
        return False

    def add_to_loan_amount(self, amount):
        if amount > 0:
            self.total_loan_amount += amount

    def subtract_from_loan_amount(self, amount):
        if amount > 0 and amount <= self.total_loan_amount:
            self.total_loan_amount -= amount
            return True
        return False
