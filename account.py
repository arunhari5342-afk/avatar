class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print("Amount deposited successfully.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")
    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder_name)
        print("Balance:", self.balance)
acc1 = BankAccount(1001, "Rajesh", 5000)
acc1.check_balance()
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.deposit(-500)
acc1.withdraw(10000)
acc1.check_balance()
