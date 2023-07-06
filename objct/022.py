class BankAccount:
    ROI=10.5
    def __init__(self) -> None:
        self.name=""
        self.amount=0
    def Accept(self):
        self.name=input("Enter name:")
        self.amount=input("Enter amount:")
    def Deposit(self,value):
        self.amount=self.amount+value
    def withdraw(self,value):
        self.amount=self.amount-value
    def calculateintrest(self):
        principal=self.amount
        ROI=self.__class__.ROI
        tenureinyear=1

        intrst=(principal*ROI*tenureinyear)/100
        return intrst
    def display(self):
        print(f"Account holder name:{self.name}")
        print(f"Amount of:{self.name}:{self.amount}")
        print(f"Intrest of {self.amount} for 1 year is:",self.calculateintrest())

user1=BankAccount()
user2=BankAccount()

print("Depositing 500 in user1".center(50,"-"))
user1.Deposit(500)
user1.display()

print("Depositing 500 in user1".center(50,"-"))
user2.Deposit(500)
user2.display() 