from sys import argv
def addition(a,b):
    ans=0
    ans=a+b
    return ans

def main():
    print("Welcome to the application:",argv[0])

    if (len(argv)==2):
        if(argv[1]=="--U"):
            print("use the application as: ")
            print("Python Name_of_application First_number Second_number")
            exit()
        if(argv[1]=="--H"):
            print("Help: This application is used to perform addition of 2 numbers")
            exit()
    if (len(argv)!=3):
        print("Invalid number of arguments")
        print("please use --U flag to get the usage and --H to get the help flag for perform")
        exit()
    ret=addition(int(argv[1]),int(argv[2]))
    print("Addition is :",ret)
    print("Thankyou for using the application")
if __name__=="__main__":
    main()