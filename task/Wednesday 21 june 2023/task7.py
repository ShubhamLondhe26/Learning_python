#7) Write a program which contains filter(),map() and reduce() in it. Python application which contains one list of numbers . List contains the numbers which are accepted from user. filter should filter out all such numbers which are even . Map function will calculate its square. Reduce will return addition of all that numbers.
from functools import reduce#reduce
def addition(x,y):#reduce
    return x+y

def square(num):#Map
    return  num**2
def Even_number(num):#filter
    if num%2==0:
        return True
    else:
        return False


def main():
    size=int(input("Enter the size of the list: "))
    lst=[]
    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print(lst)
    even=list(filter(Even_number,lst))#filter
    print("After filteration for even the list is : ",even)#filter
    squar=list(map(square,even))#Map
    print("After Mapping Square for the list is : ",squar)#Map
    add=reduce(addition,squar)#reduce
    print("The addition is ",add)#reduce
if __name__=="__main__":
    main()