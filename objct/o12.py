class College:
    
    def __init__(self):
        self.name=""
        self.age=0
        self.mobile=0
        self.rollno=0
    def Create_id(self):
        self.name=input("Enter your Name:")
        self.age=int(input("Enter your Age:"))
        self.mobile=int(input("Enter your Mob.No: "))
        self.rollno=int(input("Enter your Roll.No:"))
    def Display_Student_info(self):
        print("*Student Information*")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No::",self.rollno)
        print("Mobile No:",self.mobile)
    @staticmethod
    def details():
        print("Please attach these Documents given below:")
        print("Passport size photograph")
        print("Address Proof:(Aadhar car/ Latest Light Bill)")
        print("Fee Receipt")

def main():
    Student1=College()
    Student2=College()

    College.details()
    
    print("Student 1:")
    Student1.Create_id()
    print("Student 2:")
    Student2.Create_id()

    
    Student1.Display_Student_info()
    Student2.Display_Student_info()
if __name__=="__main__":
    main()
