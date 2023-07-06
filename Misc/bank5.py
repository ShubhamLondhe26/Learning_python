class Bank_Account:
    Bank_Name = "HDFC BANK"
    ROI_On_FD = 4.5

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name : ",end ="")
        self.Name = input()

        print("Enter your intial amount : ",end = "")
        self.Amount = int(input())

        print("Enter your Address :", end ="")
        self.Address = input()

        print("Enter your Account Number : ",end ="")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-------- Your Account informartion is as below --------")
        print("Name of Account Holder : ",self.Name.capitalize())
        print("Account Number : ",self.AccountNo)
        print("Address of Account Holder : ",self.Address.capitalize())
        print("Current Amount in account : ",self.Amount)

    @classmethod
    def DisplayBankinformation(cls):
        print("----Welcome to Bank---")
        print("Name of our bank:",cls.Bank_Name)
        print("Rate of interest on FD",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please fill the KYC information")
        print("After filling the form please submit the document as mention below")
        print("1. Clear passport size photo")
        print("2. Photocopy of adhar card")
        print("3. Photocopy of PAN card")

    def Deposit(self,value):
        self.Amount =self.Amount+value

    def withdraw(self,value):
        self.Amount = self.Amount-value

def main():
    Bank_Account.DisplayBankinformation()
    print("-"*50)
    Bank_Account.DisplayKYCInfo()
    print("-"*50)
    User1 = Bank_Account()
    User2 = Bank_Account()
    
    print("Creating the first account")
    User1.CreateAccount()

    print("Creating the second account")
    User2.CreateAccount()
    print()
    User1.DisplayAccountInfo()
    print("-"*50)
    User2.DisplayAccountInfo()

    User1.Deposit(200)
    User2.Deposit(300)
    print("Amount of {} after deposit is {}".format(User1.Name,User1.Amount) )
    print("Amount of {} after deposit is {}".format(User2.Name,User2.Amount) )

    User1.withdraw(200)
    User2.withdraw(300)
    print("Amount of {} after withdraw is {}".format(User1.Name,User1.Amount) )
    print("Amount of {} after withdraw is {}".format(User2.Name,User2.Amount) )
if __name__ == "__main__":
    main()