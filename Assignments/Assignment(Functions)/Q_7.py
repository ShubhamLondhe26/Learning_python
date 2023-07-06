#7) Write a program which accept N numbers from user and store
#it into List. Return frequency of that number from that List.
#Input:
#Number of elements: 11
#Enter value : 13 5 4 2 5 7 8 9 5 10 5
#Element to search: 5
#Output: 4
def Element_to_search(intro,lst):
    num=0
    for i in lst:
        if (i==intro):
            num=num+1
    return num


def main():
    size=int(input("Enter the Number: "))
    lst=[]
    print("Enter the value: \n")
    for i in range(0,size):
        Value=int(input())
        lst.append(Value)
    print(lst)
    intro=int(input("Element to search: "))
    output=Element_to_search(intro,lst)
    print(output)

if __name__=="__main__":
    main()