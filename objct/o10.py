class Mobile:
    def __init__(self):
        self.model=""
        self.ram=""
        self.color=""
        self.brandname=""
        self.storage=""
    def details(self):
        self.brandname=input("Enter the brand name: ")
        self.ram=input("Enter ram: ")
        self.color=input("Enter color: ")
        self.model=input("Enter the model name: ")
        self.storage=input("Enter storage: ")
    def display_details(self):
        print("Mobile Specification:\n")
        print("Brand: ",self.brandname)
        print("Ram: ",self.ram)
        print("color: ",self.color)
        print("Model: ",self.model)
        print("Storage: ",self.storage)
        print()
def main():
    obj=Mobile()
    obj.details()
    obj.display_details()
if __name__=="__main__":
    main()



        