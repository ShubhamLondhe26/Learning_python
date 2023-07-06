class Bank:
    bank_name="ICICI BANK"
    Rate_of_intrest=6.5

    def __init__(self) -> None:
        self.name=""
        self.account=0
        self.address=""
        self.dposit=0
    def create_account(self):
        self.name=input("Enter your name:")
        self.account=int(input("Enter Account no:"))
        self.address=input("Enter your address:")
        self.dposit=int(input("Enter Amount:"))
    def displayaccinfo(self):
        print("*Bank Account Information*")
        print("Name: ",self.name)
        print("Account No: : ",self.account)
        print("Address: ",self.address)
        print("Balance Amount: ",self.dposit)
    @classmethod
    def bankinfo(cls):
        print(f"Welcome to {cls.bank_name}")
        print("Rate Of Intrest:",cls.Rate_of_intrest)
    @staticmethod
    def DisplayKYCInfo():
        print("Please fill the KYC information")
        print("After filling the form please submit the document as mention below")
        print("1. Clear passport size photo")
        print("2. Photocopy of adhar card")
        print("3. Photocopy of PAN card")
def main():
    Bank.bankinfo()
    user1=Bank()
    print("Creating Account")
    user1.create_account()
    print("*Account Information*")
    user1.displayaccinfo()


if __name__=="__main__":
    main()