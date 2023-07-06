def main():
    size=int(input("Enter the number: "))
    lst=[]

    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print("User list:",lst)
    even_number= filter(lambda num: num%2==0,lst)
    output=list(even_number)
    print("After filteration: ",output)
if __name__=="__main__":
    main()