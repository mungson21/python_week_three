class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print('User: ' + self.name + ', ' + 'Balance: ' + str(self.account_balance))

guido = User("Guido R.", "guido@python.com")
monty = User("Monty P.", "monty@python.com")
mike = User("Mike U.", "mike@python.net")
max = User("Max C.", "max@python.net")
mario = User("Mario B.", "mariob@python.edu")

# print(guido.name)
# print(monty.name)

# Deposits
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(20)
mike.make_deposit(1500)
mike.make_deposit(1500)
mike.make_deposit(5000)
max.make_deposit(300)
max.make_deposit(250)
mario.make_deposit(350)

# print(guido.account_balance)
# print(monty.account_balance)

# Withdrawels
guido.make_withdrawal(100)
monty.make_withdrawal(15)
mike.make_withdrawal(3000)
max.make_withdrawal(50)
max.make_withdrawal(80)
mario.make_withdrawal(150)
mario.make_withdrawal(100)
mario.make_withdrawal(300)

# print(guido.account_balance)
# print(monty.account_balance)

# Account Balance
guido.display_user_balance()
mike.display_user_balance()
max.display_user_balance()
mario.display_user_balance()