class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")


# Main program loop
account = BankAccount()

while True:
    print("\n--- Bank Menu ---")
    print("1 Deposit")
    print("2 Withdraw")
    print("3 Show Balance")
    print("4 Exit")

    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        try:
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        try:
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Thank you for using our bank system. Goodbye!")
        break

    else:
        print("Invalid choice! Please select an option from 1 to 4.")