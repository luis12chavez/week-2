class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.2, balance = 0): 
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
    

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.02, balance=0)]
    
    # other methods
    
    def make_deposit(self, amount, index = 0):
    	# your code here
        if(index > len(self.account) - 1):
            print("++++++++++++++++++++")
            print(f"{index} is not an option.")
            print("++++++++++++++++++++\n")
            print("Available Accounts:")
            print("--------------------")
            for i in range(len(self.account)):
                print(f"{i}: ${self.account[i].balance}")
            return self
        else:
            self.account[index].deposit(amount)
            # print(self.account[index].balance)
            return self

    def make_withdrawal(self, amount, index = 0):
         if(index > len(self.account) - 1):
            print("++++++++++++++++++++")
            print(f"{index} is not an option.")
            print("++++++++++++++++++++\n")
            print("Available Accounts:")
            print("--------------------")
            for i in range(len(self.account)):
                print(f"{i}: ${self.account[i].balance}")
            return self
         else:
            self.account[index].withdraw(amount)
            # print(self.account[index].balance)
            return self
        

    def display_user_balance(self):
        for i in range(len(self.account)):
            print(f"Balance: ${self.account[i].balance}")

    def add_account(self, name = "Default"):
        name = BankAccount()
        self.account.append(name)
        return self


test_user2 = User("TEST", "TEST@gmail.com")
test_user2.add_account().add_account()
# print(test_user2.account[1].balance)
# print(" ")

print(" ")
test_user2.make_deposit(500,1).make_withdrawal(3000,3).make_deposit(40,2).make_withdrawal(20, 0)
print(" ")
test_user2.display_user_balance() # checking balance in all accounts


