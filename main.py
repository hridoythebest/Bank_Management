from user import User
from admin import Admin

def display_menu():
    print(' ')
    print("<============ Banking Management System ============>")
    print(' ')
    print(">------------------User-------------------->")
    print("1. Create User Account, 2. Deposit Amount, 3. Withdraw Amount, 4. Transfer Amount, 5. Check Balance, 6. Check Transaction History, 7. Request Loan")
    print(' ')
    print(">>---------------Admin-------------->>")
    print(".......")
    print("00. Exit")
    print(' ')
    print("<============ Banking Management System ============>")


def create_user_account():
    name = input("Enter user name: ")
    user = User(name)
    users.append(user)
    print(f"User account created successfully. Account number: {user.account_number}")

def deposit_amount():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to deposit: "))
    user = find_user(account_number)
    if user:
        user.deposit(amount)
        print("Amount deposited successfully.")
    else:
        print("Invalid account number.")

def withdraw_amount():
    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))
    user = find_user(account_number)
    if user:
        if user.withdraw(amount):
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or bank is bankrupt.")
    else:
        print("Invalid account number.")

def transfer_amount():
    account_number = int(input("Enter account number: "))
    recipient_account_number = int(input("Enter recipient's account number: "))
    amount = float(input("Enter amount to transfer: "))
    user = find_user(account_number)
    recipient = find_user(recipient_account_number)
    if user and recipient:
        if user.transfer(amount, recipient):
            print("Amount transferred successfully.")
        else:
            print("Insufficient balance or bank is bankrupt.")
    else:
        print("Invalid account number(s).")

def check_balance():
    account_number = int(input("Enter account number: "))
    user = find_user(account_number)
    if user:
        user.check_balance()
    else:
        print("Invalid account number.")

def check_transaction_history():
    account_number = int(input("Enter account number: "))
    user = find_user(account_number)
    if user:
        user.check_transaction_history()
    else:
        print("Invalid account number.")

def request_loan():
    account_number = int(input("Enter account number: "))
    user = find_user(account_number)
    if user:
        user.request_loan()
    else:
        print("Invalid account number.")


def find_user(account_number):
    for user in users:
        if user.account_number == account_number:
            return user
    return None

# Main program

users = []
admin = Admin()

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        create_user_account()
    elif choice == "2":
        deposit_amount()
    elif choice == "3":
        withdraw_amount()
    elif choice == "4":
        transfer_amount()
    elif choice == "5":
        check_balance()
    elif choice == "6":
        check_transaction_history()
    elif choice == "7":
        request_loan()
    elif choice == "00":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")


