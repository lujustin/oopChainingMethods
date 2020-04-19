class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.amount_balance = 0
    def make_deposit(self, amount):
        self.amount_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.amount_balance -= amount
        return self
    def display_user_balance(self):
        print("User:" + self.name + "Balance:" + "$" + str(self.amount_balance))


joel = User("Joel", "joel@codingdojo.com")
deanna = User("Deanna", "deanna@codingdojo.com")
stevie = User("Stevie", "stevie@codingdojo.com")


joel.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(10).display_user_balance()

deanna.make_deposit(30).make_deposit(30).make_withdrawal(10).make_withdrawal(10).display_user_balance()

stevie.make_deposit(100).make_withdrawal(10).make_withdrawal(10).make_withdrawal(10).display_user_balance()