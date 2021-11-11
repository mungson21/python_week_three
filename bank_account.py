class BankAccount:
    # class attributes
    balance = []
    int_rate = 0.01
    def __init__(self, int_rate = 0.01, account_balance = 0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.account_balance = account_balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.account_balance -= 5
            return self
        else:
            self.account_balance -= amount
            return self
        return self
    def display_account_info(self):
        print('Balance: ' + str(self.account_balance))
    def yield_interest(self):
        if self.account_balance > 0:
            x = self.account_balance
            x *= 0.01
            self.account_balance += x
            return self
        else:
            pass

guido = BankAccount()
mario = BankAccount()
# print(guido.account_balance)
# print(guido.int_rate)

# guido.deposit(50)
# guido.withdraw(200)
# print(guido.account_balance)

guido.deposit(500).deposit(300).deposit(50).withdraw(200).yield_interest().display_account_info()
mario.deposit(200).deposit(200).withdraw(75).withdraw(75).withdraw(200).withdraw(175).yield_interest().display_account_info()