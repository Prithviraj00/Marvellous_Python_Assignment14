class BankAccount:
    def __init__(self,A,B,C):
        self.name = A
        self.account_number = B
        self.balance = C

    def Deposite(self,value):
        self.balance = self.balance + value
        print(" Balance After Deposite is :",self.balance)
        
        
    def Withdraw(self,value):
        self.balance = self.balance - value
        print(" Balance After Withdraw is :",self.balance)
        
    def Display(self):
        print("Name :",self.name)
        print("Account Number :",self.account_number)
        print("Total Balance is :",self.balance)


def main():
    obj1 = BankAccount("Rahul",1000020345,4000)
    obj1.Deposite(50000)
    obj1.Withdraw(2000)
    obj1.Display()
    

if __name__ == "__main__":
    main()