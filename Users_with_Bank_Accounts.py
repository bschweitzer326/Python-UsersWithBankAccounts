class BankAccount:
    def __init__(self, title, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.title = title

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee!")
        return self

    def display_account_info(self,name):
        print(f"User:{name}'s {self.title} interest rate is {self.int_rate} and account balance is ${round(self.balance,2)}.")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        elif self.balance <= 0:
            self.balance = self.balance
        return self

class User:
    def __init__(self,name,email,int_rate):
        self.name = name
        self.email = email
        self.account = BankAccount(title="checking",int_rate = int_rate, balance = 0)
        self.account2 = BankAccount(title="savings",int_rate = int_rate, balance = 0)
    
    def make_deposit(self, amount, num):
        if num == 1:
            self.account.deposit(amount)
        elif num == 2:
            self.account2.deposit(amount)
        return self

    def make_withdraw(self, amount,num):
        if num == 1:
            self.account.withdraw(amount)
        elif num == 2:
            self.account2.withdraw(amount)
        return self

    def display_account_info(self,num):
        if num == 1:
            self.account.display_account_info(self.name)
        elif num == 2:
            self.account2.display_account_info(self.name)
        return self

    def yield_interest(self,num):
        if num == 1:
            self.account.yield_interest()
        elif num == 2:
            self.account2.yield_interest()
        return self

larry = User("larry", "larry@3stooges.com",.02)

larry.make_deposit(100,1).make_deposit(500,1).make_deposit(300.05,1).make_withdraw(200,1).yield_interest(1).display_account_info(1)
larry.make_deposit(200,2).make_deposit(100.05,2).make_withdraw(100,2).make_withdraw(50,2).make_withdraw(150,2).make_withdraw(100,2).yield_interest(2).display_account_info(2)

