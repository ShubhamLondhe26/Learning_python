from functools import reduce
def reducing(x,y):
    return max(x,y)
def Mapping(number):
    return number*2
def filter1(num):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def main():
    size = int(input("Enter the size of the list: "))
    lst = []
    print("Enter the values: \n")
    for _ in range(size):
        value = int(input())
        lst.append(value)
    print(lst)
    output = filter(filter1, lst)
    count = list(output)
    print("After filteration for Prime Numbers:",count)
    point=map(Mapping,count)
    point1=list(point)
    print("after mapping:",point1)
    intro=reduce(reducing,point1)
    print("The maximum number is : ",intro)

if __name__ == "__main__":
    main()
