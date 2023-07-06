#8)Write a program which accept N numbers from user and store it
#into list. Return addition of all prime numbers from that list.
#Main python file accepts N numbers from user and pass each
#Number to Check_Prime( ) function which is part of our user
#defined module named as NumPrime . Name of the function from
#main python file should be ListPrime().
#Input: Number of elements :10
#Input Elements: 13 12 5 6 8 7 10 2 5 6 

from NumPrime import Check_Prime
def ListPrime(Numbers):
    Prime_Numbers=[]
    for Num in Numbers:
        if (Num == 0 or Num ==1):
            continue
        ret=Check_Prime(Num)
        if (ret == True):
            Prime_Numbers.append(Num)
    return Prime_Numbers
def main():
    num=int(input("Enter the number: "))

    data_input=[]
    print("Enter the data: ")

    for i in range(0,num):
        Num=int(input())
        data_input.append(Num)
    print("List given by user: ",data_input)
    List_Of_Prime=ListPrime(data_input)
    print("list of prime numbers:",List_Of_Prime)

if __name__=="__main__":
    main()