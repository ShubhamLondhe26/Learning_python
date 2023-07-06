#1 . Write a program which will count the frequency of letters of the string.
def main():
    size=input("Enter The string: ")
    lst=list(size)
    for i in lst:
        frequency=lst.count(i)# used count to find the count of elements in list
        print(frequency)
if __name__=="__main__":
    main()
