def Even_number(lst1):
    lst2=[]
    for i in lst1:
        if i%2==0:
            lst2.append(i)
    return lst2


def main():
    lst1=[]
    size=int(input("Enter the size: "))
    for i in range(0,size):
        intro=int(input("Enter the value: "))
        lst1.append(intro)
    print(lst1)
    ans=Even_number(lst1)
    print("Even numbers in list: ",ans)

if __name__=="__main__":
    main()