class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.1, balance = 0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate / 100
        self.balance = balance
    
    def deposit(self, amount):
        # your code here
        self.balance +=  amount
        return self

    def withdraw(self, amount):
        # your code here
        if(amount > self.balance):
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else:
            self.balance -=  amount

        return self
    
    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if(self.balance > 0):
            self.balance = (self.balance * self.int_rate) + self.balance

        return self

account = BankAccount(5)
account2 = BankAccount(10, 1000)

account.deposit(25).deposit(10).deposit(5).withdraw(300).display_account_info()
account2.deposit(10).deposit(40).withdraw(1500).withdraw(250).withdraw(10).yield_interest().display_account_info()
