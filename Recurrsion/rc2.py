#factorial

def factorial(num):
    if num==1:
        return 1
    elif num==0:
        return 1
    else:
        return(num*factorial(num-1))

def main():
    num=int(input("Ente the number: "))
    num1=num
    output=factorial(num)
    print(f"The factorial of {num1} is ",output)

if __name__=="__main__":
    main()
