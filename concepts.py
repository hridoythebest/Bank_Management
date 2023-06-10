"""
in order to better readability and reduce code complexity let's split code into few file like main.py, admin.py and user.py
<========================================================================================================>

Main Page functions (methods) can be implement step by step : 
---------------------------------------------------->
1. create_user
    - create users empty list to store all user
    - to create user I need a starting account number
    - also need a account number auto generate method to create user account number dynamically
    - add user name
    - a starting balance
    - add transaction history
    - add loan amount 
    - print a message to input 1 in order to create new user
    - check if input 1 then call new user create method
    - take user name and call generate account number for that user
    - also print success message with user name and account number
    - add user to user list


2. deposit_amount
    - to deposit money we need a validator that user submitting money more than 0
    - if money more than 0 then add that amount in balance
    - also add transaction history with time
    - in that case must need to import datetime 
    - if deposit amount less than or equal 0 then return false
    - print a message to input 2 in order to deposit money
    - check if user input 2 then call deposit_amount method
    - to deposit amount we need user account number (take input and use int to convert user input)
    - also need a deposit amount (take input and use float  to convert user input)
    - use find_user method to find user 
    - add deposit amount to user account (deposit method)
    - add deposit amount to user transaction history(deposit method)
    - print successful message with user name, amount and account number
    -

3. withdraw_amount
    - to withdraw balance create withdraw method
    - check balance more than 0 and less than balance
    - if true then deduct that amount 
    - add transaction history
    - or return false
    - print a message to input 3 in order to withdraw money
    - check if user input 3 then call withdraw_amount method
    - to withdraw amount we need user account number (take input and use int to convert user input)
    - also need a withdraw amount (take input and use float  to convert user input)
    - deduct withdraw amount to user account (withdraw method)
    - add withdraw amount to user transaction history(withdraw method)
    - print successful message with user name, amount and account number
    -
4. transfer_amount
    - to transfer amount we need a validator that user submitting money more than 0 and less than balance 
    - if condition true then deduct amount from user balance and add that amount to recipient balance
    - add transaction history to for user and recipient also
    - print a message to input 4 in order to transfer money
    - check if user input 4 then call transfer_amount method
    - to transfer amount we need user account number (take input and use int to convert user input)
    - to transfer amount we need recipient account number (take input and use int to convert user input)    - 
    - also need a transfer amount (take input and use float  to convert user input)
    -find user with find_user method and use account number
    -find recipient with find_user method and use recipient account number
    - if user and recipient exists 
    - deduct transfer amount to user account (transfer method)
    - add transfer amount to recipient account (transfer method)
    - add transfer amount to user transaction history(transfer method)
    - add transfer amount to recipient transaction history(transfer method)
    - print successful message with user name, amount and account number
    

5. check_balance
    - create a method for check balance
    - print account number
    - print name
    - balance
    - print a message to input 5 in order to check money
    - check if user input 5 then call check balance method
    - take account number input from user and use int to convert input
    - use find_user method to validate user
    - if user found call check_balance 


6. check_transaction_history
    - create a method for check transaction history
    - print account number
    - use loop to print all the transaction
    - print a message to input 6 in order to check transaction
    - check if user input 6 then call check check transaction history method
    - take account number input from user and use int to convert input
    - use find_user method to validate user
    - if user found call check transaction history method 

7. take_loan
    - create request loan method
    - check if previous loan amount o then multiply balance with 2 and add that on balance
    - add loan amount to user transaction history
    - print loan taken successfully message
    - print a message to input 7 in order to take loan
    - check if user input 7 then call check take loan method
    - take account number input from user and use int to convert input
    - use find_user method to validate user
    - if user found call take loan method 



Admin Page methods 
------------------------------------>
1. create_account
2. check_total_balance
3. check_total_loan_amount
4. toggle_loan_feature

"""
                                                                      