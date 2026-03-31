
password_database = {
    'teja' : 'password'
}

class BankAccount:
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance
        
        
    def deposit(self, amount):
        
        self.balance += amount
        print(f"{amount} deposited sucessfully to {self.holder}")
        return self.balance
    
    def withdraw(self,amount):
        self.password = input(f"Enter Password for {self.holder} :")
        if self.__auth(self.holder,self.password,password_database):
            if amount < self.get_balance() :
                final_balance = self.get_balance() -amount
                self.set_balance(final_balance)
                print(f"{amount} withdraw successfully")
                print(f"remaining balance{self.get_balance()}")
            else:
                print("Insufficient balance")
        
    def __auth(self,name,password,database):
        if database[name] == password:
            print("Authentication Successsssss")
            return True
        print("Authentication Failed")
        return False
    
    def set_balance(self,number):
        self.__balance = number
        
    def get_balance(self):
        self.password = input(f"Enter Password for {self.holder} :")
        if self.__auth(self.holder,self.password,password_database):
            print(f"Balance is {self.__balance}")
            return self.__balance
        return None


teja_account = BankAccount("teja",500000)


teja_account.withdraw(5000)
teja_account.get_balance()

    