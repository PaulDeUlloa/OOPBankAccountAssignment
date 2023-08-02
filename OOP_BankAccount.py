class BankAccount:
    int_rate = 0.0
    balance = 0.0
    all_account = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self
        else:
            self.balance = self.balance - amount
            return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0.0:
            self.balance = self.balance * self.int_rate
        return self

Paul = BankAccount(1.0, 3000)
Joe = BankAccount(2.0, 2000)

Paul.deposit(100).deposit(50).deposit(40).withdraw(30).yield_interest().display_account_info()
Joe.deposit(100).deposit(50).withdraw(30).withdraw(70).withdraw(90).withdraw(20).yield_interest().display_account_info()