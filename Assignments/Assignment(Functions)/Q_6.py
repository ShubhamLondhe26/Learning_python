#6)Write a program which accept N numbers from user and store it
#into List. Return Minimum number from that List.
#Input:
#Number of elements:8
#Enter value : 11 13 14 56 57 58 12 19
#Output : Minimum Number of the given list : 11#

def Max_number(num):
    intro=num[0]
    for i in num:   
        if i< intro:
            intro=i
    return intro
def main():
    size=int(input("Enter the Number: "))
    lst=[]
    print("Enter the value: \n")
    for i in range(0,size):
        Value=int(input())
        lst.append(Value)
    print(lst)
    output=Max_number(lst)
    print("Minimum Number of the given list :",output)

if __name__=="__main__":
    main()