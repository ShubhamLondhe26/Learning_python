class Arthematic:

    def __init__(self):
        self.num1=0
        self.num2=0
    
    def Accecpt(self):
        self.num1=int(input("Enter the first number:"))
        self.num2=int(input("Enter the second number:"))
    def calculate(self):
        result_add = self.num1 + self.num2
        result_sub = self.num1 - self.num2
        result_multiply = self.num1 * self.num2
        result_divide = self.num1 / self.num2
        
        print("Addition result:", result_add)
        print("Subtraction result:", result_sub)
        print("Multiplication result:", result_multiply)
        print("Division result:", result_divide)
def main():
    obj=Arthematic()
    obj.Accecpt()
    obj.calculate()

if __name__=="__main__":
    main()
