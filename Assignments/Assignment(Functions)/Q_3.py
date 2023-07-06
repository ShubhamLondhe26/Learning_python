#3)Write a program which accept one number from user and check whether number is prime or not Input:5 Output: Prime number
def Check_prime(num):
    for i in range(2,num):
        if num%i==0:
            return "is not a prime Number"
    return "is a prime number"
        
def main():
    num=int(input("Enter the number: "))
    output=Check_prime(num)
    print(num,output)
if __name__=="__main__":
    main()