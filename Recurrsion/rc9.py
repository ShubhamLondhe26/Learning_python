
def Prime_number(No):
    if No>1:
        for i in range(2,No):
            if No%i==0:
                return False
        return True
    
def filterX(helper_function,data):
    result=[]
    for No in data:
        if(helper_function(No)==True):
            result.append(No)
    return result
def multiplication(No):
    return No*No

def MapX(helper_map,data):
    result=[]
    for num in data:
        value=helper_map(num)
        result.append(value)
    return result
def highest_number(x,y):
    if x>y:
        return x
    return y

def ReduceX(hlper_reduce,data):
    result=0
    for num in data:
        result=hlper_reduce(result,num)
    return result
def main():
    size=int(input("Enter the size of list:"))
    lst=[]
    print("Enter the values:")
    for i in range(0,size):
        value=int(input())
        lst.append(value)
    print(lst)
    output=filterX(Prime_number,lst)
    output1=list(output)
    print(output1)
    intro=MapX(multiplication,output1)
    intro1=list(intro)
    print(intro1)
    count=ReduceX(highest_number,intro1)
    print(count)

if __name__=="__main__":
    main()