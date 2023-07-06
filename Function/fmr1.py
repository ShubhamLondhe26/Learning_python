
from functools import reduce
def product(num1,num2):#for reducing
    num3=num1*num2
    return num3

def increament(num):#for mapping
    num=num+10
    return num
def check_num(num):#for filteration
    if num>=70 and num<=90:
        return True
    return False
def main():
    size=int(input("Enter the number: "))
    lst=[]
    print("Enter the value: ")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print("user defined list: ",lst)
    print("-"*50)
    number_list=list(filter(check_num,lst))
    print("After filteration using lambda function: ",number_list)
    increament_list=list(map(increament,number_list))
    print("-"*50)
    print("After mapping using lambda function: ",increament_list)
    multiplication=reduce(product,increament_list)
    print("-"*50)
    print("After reducing using lambda function: ",multiplication)



if __name__=="__main__":
    main()