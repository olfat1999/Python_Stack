class User: 
    def __init__(self,name,balance=0):
        self.name = name 
        self.balance = balance
    

    def  make_deposit(self, amount):
        self.balance = self.balance + amount 
        return self
    
    def make_withdrawal(self, amount):
        if(self.balance - amount > 0):
            self.balance = self.balance - amount
        else:
            print(f"Error: {self.name} does not have enough money {self.balance}")  
        return self     

    def display_user_balance(self):
        print("User name: ",self.name,"   Balance: ",self.balance)
        return self
    
    def transfer_money(self, other, amount):
        self.make_withdrawal(amount)
        other.make_deposit(amount)
        return self

user1 = User("user1",1000)        
user2 = User("user2")
user3 = User("user3",200)




user1.display_user_balance().make_deposit(200).make_deposit(300).make_deposit(300).make_deposit(50).make_withdrawal(1000).display_user_balance()

user2.display_user_balance().make_deposit(200).make_deposit(1500).make_withdrawal(700).make_withdrawal(400).display_user_balance()

user3.display_user_balance().make_deposit(500).make_withdrawal(100).make_withdrawal(400).make_withdrawal(1000).display_user_balance()



print("user1 transfer 100 to user3")

user1.transfer_money(user3,100)
user1.display_user_balance()
user3.display_user_balance()