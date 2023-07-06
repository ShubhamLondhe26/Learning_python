from functools import reduce
def intro(num):
    if num%2!=0:
        return intro
def mapping(num):
    return num+2
def reducing(x,y):
    return max(x,y)
def main():
    size=int(input("Enter the size of the list:"))
    lst=[]
    print("Enter the value:")
    for i in range (0,size):
        value=int(input())
        lst.append(value)
    print(lst)
    filtering=list(filter(intro,lst))
    print(filtering)
    mapping1=list(map(mapping,filtering))
    print(mapping1)
    reducing1=reduce(reducing,mapping1)
    print(reducing1)



if __name__=="__main__":
    main()