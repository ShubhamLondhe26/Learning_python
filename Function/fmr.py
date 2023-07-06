from functools import reduce
check_num= lambda no: no>=70 and no<=90
increament=lambda no:no+10
product=lambda no1,no2:no1*no2
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
    multiplication_list=reduce(product,increament_list)
    print("-"*50)
    print("After reducing using lambda function: ",multiplication_list)


if __name__=="__main__":
    main()