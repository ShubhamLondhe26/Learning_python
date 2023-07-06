def check_positive(num):
    if num>=0:
        return True
    return False

def main():
    size=int(input("Enter the number: "))
    lst=[]

    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print("User list:",lst)
    even_number= filter(check_positive,lst)
    output=list(even_number)
    print("After filteration: ",output)
if __name__=="__main__":
    main()