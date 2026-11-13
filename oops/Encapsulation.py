'''
Syntax	    Name	Meaning
balance	    Public 	Normal access
_balance    Protected	Internal-use convention
__balance   Private	Name-mangled, intended to restrict direct access

class bankaccount:
    def __init__(self):
        self.__balance = 10000
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
        print("Insufficient balance")
    def check_balance(self):
        print(self.__balance)
account = bankaccount()
account.deposit(2000)
account.withdraw(3000)
account.check_balance()
o/p: 9000

Account Holder: Madhu
Balance: 10000
Deposited: 5000
Withdrawn: 3000
Account Holder: Madhu
Balance: 12000

class bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
            print("deposited",amt)
        else:
            print("bank minimum balance is must")
    def withdraw(self,amt):
        if amt > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("invalid amount")
        else:
            self.__balance -= amt
            print("withdraw:",amt)
    def check_balance(self):
        print("account holder:", self.name)
        print("balance: ", self.__balance)
account = bankaccount("madhu",10000)
account.check_balance()
account.deposit(4000)
account.withdraw(40000)
account.check_balance()

'''

































