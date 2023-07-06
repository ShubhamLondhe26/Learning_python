def count_num(lst1,num):
    count=0
    for i in lst1:
        if (i==num):
            count=count+1
    return count


def main():
    size=int(input("Enter the number: "))
    lst1=[]
    for i in range(0,size):
        intro=input("Enter the value: ")
        lst1.append(intro)
    print(lst1)
    num=int(input("Enter the number you want to search: "))
    ans=count_num(lst1,num)
    print(num," is repeating",ans, "times")

if __name__=="__main__":
    main()

