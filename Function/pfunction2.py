def Max_number(lst1):
    max_digit=lst1[0]
    for i in lst1:
        if i > max_digit:
            max_digit=i
    return max_digit 


def main():
    lst1=[]
    size=int(input("Enter the size: "))
    for i in range(0,size):
        intro=int(input("Enter the value: "))
        lst1.append(intro)
    print(lst1)
    ans=Max_number(lst1)
    print("Max Number is: ",ans)

if __name__=="__main__":
    main()