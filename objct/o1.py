#accept 2 numbrs and perfor addition and subtraction of it
#kya karenge->behaviour(functions)
#performing addition and subtraction

#performing k liye kya lagega->characterstics
#2
#class= characterstics + behaviour
#class= data + functions

class Arthematic:
    #def __init__(self,A,B):#__init__ is a method
    #    self.no1=A
    #    self.no2=B
    #def add(self):
    #    return self.no1+self.no2
    #def __init__(self, A, B):
    #  self.No1 = A
    #  self.No2 = B
    #def sub(self):
    #    return self.No1-self.No2
    
#    def __init__(self, A, B):
#      self.No1 = A
#      self.No2 = B
#    def multiplicattion(self):
#        return self.No1*self.No2
    def __init__(self, A, B):
      self.No1 = A
      self.No2 = B
    def division(self):
        return self.No1//self.No2
    

    
def main():
    value1=int(input("Enter the number: "))
    value2=int(input("Enter the number: "))
    obj=Arthematic(value1,value2)
    Ans=obj.division()#class.method() is used
    #print("additon is: ",Ans)
    #print("Subtraction is: ",Ans)
    #print("Multiplication is: ",Ans)
    print("Division is: ",Ans)

if __name__=="__main__":
    main()



        