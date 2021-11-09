class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print('User: ' + self.name + ', ' + 'Balance: ' + str(self.account_balance))
        # Comeback to this, think you should be using "return"

guido = User("Guido R.", "guido@python.com")
monty = User("Monty P.", "monty@python.com")
mike = User("Mike U.", "mike@python.net")
max = User("Max C.", "max@python.net")
mario = User("Mario B.", "mariob@python.edu")

# print(guido.name)
# print(monty.name)

# Deposits
# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(20)
# mike.make_deposit(1500)
# mike.make_deposit(1500)
# mike.make_deposit(5000)
# max.make_deposit(300)
# max.make_deposit(250)
# mario.make_deposit(350)

# print(guido.account_balance)
# print(monty.account_balance)

# Withdrawels
# guido.make_withdrawal(100)
# monty.make_withdrawal(15)
# mike.make_withdrawal(3000)
# max.make_withdrawal(50)
# max.make_withdrawal(80)
# mario.make_withdrawal(150)
# mario.make_withdrawal(100)
# mario.make_withdrawal(300)

# print(guido.account_balance)
# print(monty.account_balance)

# Account Balance
# guido.display_user_balance()
# mike.display_user_balance()
# max.display_user_balance()
# mario.display_user_balance()

# Chaining Method:

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
mike.make_deposit(1500).make_deposit(1500).make_deposit(5000).make_withdrawal(3000).display_user_balance()
max.make_deposit(300).make_deposit(250).make_withdrawal(50).make_withdrawal(80).display_user_balance()
mario.make_deposit(350).make_withdrawal(150).make_withdrawal(100).make_withdrawal(300).display_user_balance()
