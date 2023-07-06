def check_even(No):
    return (No%2==0)
    
def filterX(helper_function,data):
    result=[]
    for No in data:
        if(helper_function(No)==True):
            result.append(No)
    return result
def chck_num1(num):
    return num*num
def MapX(helper_map,data):
    result=[]
    for num in data:
        value=helper_map(num)
        result.append(value)
    return result
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
    output=MapX(chck_num1,lst)
    print(output)
    output=filterX(check_even,lst)
    print("-"*50)
    print("After using user defined function:",output)
if __name__=="__main__":
    main()