def factorial(num):
    if (num==1):
        return 1
    elif(num==0):
        return 1
    else:
        return(num*factorial(num-1))


def main():
    num=int(input("Enter the number: "))
    output=factorial(num)
    print("factorial of given number: ",output)

if __name__=="__main__":
    main()