class Numbers:
    def __init__(self):
        self.size=0
        self.arr=list()
    
    def Accept(self):
        print("Enter how many elements you want: ")
        self.size=int(input())

        print("Enter the elements")
        vlaue=0
        for i in range(0,self.size):
            value=int(input())
            self.arr.append(value)
    def display(self):
        print("Elemnts from list are: ")
        for i in range(0,self.size):
            print(self.arr[i])
    def Summation(self):
        sum=0
        for i in range(0,self.size):
            sum=sum+self.arr[i]
        return sum
def main(): 
    obj=Numbers()
    obj.Accept()
    obj.display()
    output=obj.Summation()
    print("summation of all elements is: ",output)
if __name__=="__main__":
    main()
