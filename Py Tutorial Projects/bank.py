class Account:
    def __init__ (self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if (self.balance - amount >= self.min_balance):
            self.balance -= amount
        else:
            print("SORRY !! INSUFFICIENT FUNDS !!")

    def statement(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: Rs.{self.balance}")
        
class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)
    def __str__(self):
        return f"{self.name}'s Current Account with balance of Rs.{self.balance}"

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
        return f"{self.name}'s Savings Account with balance of Rs.{self.balance}"