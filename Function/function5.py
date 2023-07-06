#types of arguments-->positional arguments
def addition(num1,num2):
    print("addition",num1,num2)
    add=num1+num2
    return add

def main():
    num1=int(input("Enter the number: "))
    num2=int(input("Enter the number: "))
    add1=addition(num2,num1)
    print(add1)
if __name__=="__main__":
    main()

#types of arguments-->keyword arguments

def fullname(fname,lname):
    getname =fname+" "+lname
    print(getname)
fullname("rahul","pawar")#positional arguments
fullname("pawar","rahul")#positional arguments
fullname(fname="rahul",lname="pawar")#keyword arguments
fullname(lname="pawar",fname="rahul")#keyword arguments
