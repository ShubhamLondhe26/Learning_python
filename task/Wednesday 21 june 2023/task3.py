#3)Write a recursive program which accept number from user and return summation of its digits.
#Input : 879
#Output :  24

def sum_of_digits(num):
    if num==0:
        return 0
    else:
        return (num%10+sum_of_digits(num//10))
    

def main():
    value=int(input("Enter the number: "))
    value1=value #value1 is used to store the value of user
    sum=sum_of_digits(value)
    print(f"The sum of digits of {value1} is {sum}")

if __name__=="__main__":
    main()