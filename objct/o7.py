class Math:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
    def addition(self):
        return self.no1 + self.no2
    def subtraction(self):
        return self.no1 - self.no2
    def division(self):
        return self.no1 / self.no2
    def multiplication(self):
        return self.no1*self.no2
def main():
    object=Math(10,12)
    result=object.addition()
    print("Addition result:", result)
    result = object.subtraction()
    print("Subtraction result:", result)
    result = object.division()
    print("division result:", result)
    result = object.multiplication()
    print("multiplication result:", result)
    
if __name__=="__main__":
    main()