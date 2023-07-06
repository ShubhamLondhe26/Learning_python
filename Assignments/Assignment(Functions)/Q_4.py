#4)Write a program which accept N numbers from user and store
#it into List. Return Addition of all elements from that List.
#Input:Number of elements:8
#Enter value : 11 13 14 56 57 58 12 19
#Output : Addition of the given list : 240
from functools import reduce
def addition(num1,num2):
    num=num1+num2
    return num

def main():
    size=int(input("Enter the Number: "))
    lst=[]
    print("Enter the value: \n")
    for i in range(0,size):
        Value=int(input())
        lst.append(Value)
    print(lst)
    output=reduce(addition,lst)
    print("Addition of the given list: ",output)

if __name__=="__main__":
    main()