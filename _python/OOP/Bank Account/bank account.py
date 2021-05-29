class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

acct1 = BankAccount(0.05,100)
acct2 = BankAccount(0.1,1000)
acct1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
acct2.deposit(500).deposit(500).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()