#reduce
#syntax->reduce(function,sequence)
from functools import reduce
def square(number1,number2):
    return number1*number2

def main():
    size=int(input("enter the number: "))
    lst=[]
    print("Enter the values:")
    for i in range(0,size):
        values=int(input())
        lst.append(values)
    print(lst)
    square1=reduce(square,lst)
    print("After mapping: ",square1)

if __name__=="__main__":
    main()