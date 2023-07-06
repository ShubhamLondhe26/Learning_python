from sys import *
def multiplication(x,y):
    ans=1
    ans=x*y
    return ans
def main():
    print("Welcome to the Appllication: ",argv[0])

    if(len(argv)==2):
        if(argv[1]=="--U" or "--u"):
            print("use the application as: ")
            print("Python Name_of_application First_number Second_number")
            exit()
        if (argv[1]=="--H"or "--h"):
            print("Help:the program is used to multiply 2 numbers")
            exit()
    if(len(argv)!=3):
        print("Invalid numbers of arguments:")
        print("please use --U flag to get the usage and --H to get the help flag for perform")
        exit()
    result=multiplication(int(argv[1]),int(argv[2]))
    print("Multiplication is :",result)
    print("Thankyou for using the application")


if __name__=="__main__":
    main()