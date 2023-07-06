#3) Write a program which contains one class named as BankAccount.
#BankAccount class contains two instance variables as Name & Amount.
#That Class Contains one class variable as ROI which is initialize to 10.5
#Inside init method initialize all name and amount variable by accepting the values from user.
#There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
#Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
#Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
#CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
#And Display () method will display value of all the instance variables as Name and Amount.
#After designing the above class call all instance methids by creating multiple objects

class BankAccount:
    ROI=10.5

    def __init__(self) -> None:
        self.name=input("Enter the name: ")
        self.amount=float(input("Enter the amount"))
    def display(self):
        print("Name:",self.name)
        print("Amount:",self.amount)
    def deposit(self):
        amount=int(input("Enter th amount to deposit:"))
        return self.amount+amount
    def withdraw(self):
        