def check_even(No):
    return (No%2==0)
    
def filterX(helper_function,data):
    result=[]
    for No in data:
        if(helper_function(No)==True):
            result.append(No)
    return result


def main():
    size=int(input("Enter the number: "))
    lst=[]
    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print("user defined list: ",lst)
    output=filterX(check_even,lst)
    print("-"*50)
    print("After using user defined function:",output)

if __name__=="__main__":
    main()