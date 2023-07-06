def chck_num(num1,num2):
    return num1+num2
def ReduceX(hlper_reduce,data):
    result=0
    for num in data:
        result=hlper_reduce(result,num)
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
    output=ReduceX(chck_num,lst)
    print(output)
if __name__=="__main__":
    main()