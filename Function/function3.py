def addition(value1,value2):
    print("addition",value1,value2)
    add=value1+value2
    return add
    
def subtraction(no1,no2):
    print("subtraction",no1,no2)
    sub=no1-no2
    return sub

def main():
    value1=30
    add1=addition(12,10)
    print(add1)
    sub1=subtraction(12,10)
    print(sub1)

if __name__=="__main__":
    main()