# Ask for initial balance
balance = float(input("Enter your initial balance: "))

# Ask for withdrawal amount
withdrawal = float(input("Enter amount to withdraw: "))

# Check if withdrawal is possible
if withdrawal <= balance:
    print("Transaction Successful")
    remaining_balance = balance - withdrawal
    print("Remaining balance:", remaining_balance)
else:
    print("Insufficient Balance")