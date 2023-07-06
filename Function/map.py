#map
#syntax->map(function,sequence)
def square(number):
    return number*number

def main():
    size=int(input("enter the number: "))
    lst=[]
    print("Enter the values:")
    for i in range(0,size):
        values=int(input())
        lst.append(values)
    print(lst)
    square1=map(square,lst)
    output=list(square1)
    print("After mapping: ",output)

if __name__=="__main__":
    main()