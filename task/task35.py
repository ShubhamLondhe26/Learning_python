from functools import reduce
def main():
    size=int(input("Enter the size of the list:"))
    lst=[]
    print("Enter the value:")
    for i in range (0,size):
        value=int(input())
        lst.append(value)
    print(lst)
    filtering=list(filter(lambda num:num%2!=0,lst))
    print("after filtering:",filtering)
    mapping=list(map(lambda num:num+2,filtering))
    print("after mapping: ",mapping)
    reducing=reduce(lambda x,y: max(x,y) ,mapping)
    print("after reducing: ",reducing)
if __name__=="__main__":
    main()