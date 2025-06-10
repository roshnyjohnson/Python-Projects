x=input("enter the account holders name")
y=int(input("enter the account holders balance"))
z=int(input("enter the account holders required amount"))
task=input("Enter w for eithdrawal and d for deposit")
class atm:
    def __init__(self,name,balance,amount):
        self.name = name
        self.balance = balance
        self.amount = amount
    def withdraw(self):
        if self.balance<self.amount:
            print("not enough balance")
        else:
            print("successfully withdrawn")
            self.balance-=self.amount
            print("balance is:",self.balance)
    def deposit(self):
        self.balance += self.amount
        print("successfully deposited")
        print("balance is:",self.balance)
a=atm(x,y,z)
if task=="w":

    a.withdraw()
elif task=="d":
    a.deposit()
else:
    pass
