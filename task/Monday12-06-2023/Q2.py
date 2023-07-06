#2. Write a program to find second largest number in a list.
def second_largest_number(lst):
    lst.sort()
    return lst[-2]
def main():
    size=int(input("Enter The size for list: "))
    lst=[]
    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print(lst)
    output=second_largest_number(lst)
    print("second largest number is: ",output)
if __name__=="__main__":
    main()