# Instance variable : Name, Amount, Address, AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
#class variable: Bank_Name , ROI_On_FD(_: good practising)
#class method:DisplayBankinformation

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
   
def main():
    Bank_Account.DisplayBankinformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first account")
    User1.CreateAccount()

    print("Creating the second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()