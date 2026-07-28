class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount("Kalpak", 1000)

account.deposit(500)
account.withdraw(300)
account.show_balance()