

class BankAccount:
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        
        
    def deposit(self, amount):
        
        self.balance += amount
        print(f"{amount} deposited sucessfully to {self.holder}")
        return self.balance
    
    def withdraw(self,amount):
        if amount < self.balance :
            self.balance -=amount
            print(f"{amount} withdraw successfully")
            print(f"remaining balance{self.balance}")
        else:
            print("Insufficient balance")
        
        
        
tarun_account = BankAccount("tarun",15000000)

print(f"account holder name : {tarun_account.holder}")
print(f"account balance : {tarun_account.__balance}")

tarun_account.deposit(100)

print(f"account balance after deposit : {tarun_account.balance}")
praveen_accont = BankAccount("praveen something ", 2)


print(f"account holder name : {praveen_accont.holder}")
print(f"account balance : {praveen_accont.balance}")


print(f"account balance : {tarun_account.balance}")


teja_account = BankAccount("teja",500000)

teja_account.withdraw(20)

print(teja_account.balance)

print(teja_account.withdraw(9000))
