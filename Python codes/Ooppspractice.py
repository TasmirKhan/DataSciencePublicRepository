print("Create a function which work like the Bank account and perfor operations on it:")
class Bank:
    name = "Anonymous"
    balance = 0
    account_number =00000000

    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance 
        self.account_number = account_number

    def info(self):
        print("Accountholder = ", self.name)
        print("Available amount = ",self.balance)
    
    def withdraw(self):
        x = int(input("Enter the amount you want to withdraw"))
        if(x<=self.balance):
            self.balance = self.balance-x
            print("Transaction succesfull, Amount =", x, "\nRemained balance =", self.balance)
        elif(0>x>self.balance):
            print("!Insufficient Balance : Balance =", self.balance)
        else:
            print("Invalid input")

    def deposite(self):
        x = int(input("Enter the amount you want to deposite and deposite it in the Machine"))
        if(x>0):
            self.balance = self.balance+x
            print("Balance added successfully :\ncurrent Account balance = ",self.balance)
        else:
            print("Enter valid amount ")

b1 = Bank("Aman",0.0,230193254342)
b1.info()
b1.deposite()
b1.withdraw()