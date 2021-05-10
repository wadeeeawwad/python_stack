class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
    	self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)


user1=user("Wadee","wadee@gmail")
print(user1.name)
user1.make_deposit(100)
user1.make_deposit(50)
user1.make_deposit(60)
user1.make_withdrawal(30)
user1.display_user_balance()

user2=user("amro","amro@gmail.com")
print(user2.name)
user2.make_deposit(100)
user2.make_deposit(200)
user2.make_withdrawal(50)
user2.make_withdrawal(50)
user2.display_user_balance()

user3=user("byatneh","nyatneh@gmail.com")
print(user3.name)
user3.make_deposit(400)

user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.display_user_balance()