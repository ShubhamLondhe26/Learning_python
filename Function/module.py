def addition(num1,num2):
    add=num1+num2
    return add
def subtraction(num1,num2):
    sub=num1-num2
    return sub
def multiplication(num1,num2):
    multi=num1*num2
    return multiplication
def division(num1,num2):
    divis=num1/num2
    return division

def check_prime(No):
    i=0
    Flag=True
    for i in range(2,int(No/2)+1):
        if(No%i==0):
            Flag=False
            break
    return Flag

def addition1(A,B):
    return A+B
