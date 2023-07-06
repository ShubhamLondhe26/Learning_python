class Bank_Account:

  def __init__(self):
    self.name = ""
    self.amount = 0
    self.adress= ""
    self.accountno=0
  def Create_Account(self):
    self.name=input("Enter Your name: ")
    self.amount=int(input("Enter  Amount: "))
    self.address=input("Enter  Address: ")
    self.accountno=int(input("Enter  Account No: "))

  def DisplayAccountInfo(self):
      print("-------- Your Account informartion is as below --------")
      print("Name of Account Holder : ",self.name)
      print("Account Number : ",self.accountno)
      print("Address of Account Holder : ",self.address)
      print("Current Amount in account : ",self.amount)
def main():
  User1=Bank_Account
  User2=Bank_Account

  print("Creating the first account")
  User1.Create_Account()

  print("Creating the second account")
  User2.Create_Account()

  User1.DisplayAccountInfo()
  User2.DisplayAccountInfo()
   
if __name__ == "__main__":
    main()