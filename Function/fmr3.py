def chck_num(num):
    return num*num
def MapX(helper_map,data):
    result=[]
    for num in data:
        value=helper_map(num)
        result.append(value)
    return result

def main():
    size=int(input("Enter the number: "))
    lst=[]
    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print("user defined list: ",lst)
    print("-"*50)
    output=MapX(chck_num,lst)
    print(output)
if __name__=="__main__":
    main()