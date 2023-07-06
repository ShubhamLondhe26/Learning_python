class Arthematic:

    def __init__(self):
        self.num1=0
        self.num2=0
    
    def Accecpt(self):
        self.num1=int(input("Enter the first number:"))
        self.num2=int(input("Enter the second number:"))
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def multi(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def display(self,result):
        print("Result:",result)

def main():
    obj=Arthematic()
    obj.Accecpt()
    result_add=obj.add()
    result_sub=obj.sub()
    result_multi=obj.multi()
    result_div=obj.div()
    obj.display(result_add)
    obj.display(result_sub)
    obj.display(result_multi)
    obj.display(result_div)

if __name__=="__main__":
    main()