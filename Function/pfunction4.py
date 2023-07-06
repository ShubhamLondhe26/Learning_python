from module import check_prime
def ListPrime(Numbers):
    Prime_Numbers=[]
    for Num in Numbers:
        if (Num == 0 or Num ==1):
            continue
        ret=check_prime(Num)
        if (ret == True):
            Prime_Numbers.append(Num)
    return Prime_Numbers
def main():
    num=int(input("Enter the number: "))

    data_input=[]
    print("Enter the data: ")

    for i in range(0,num):
        Num=int(input())
        data_input.append(Num)
    print("List given by user: ",data_input)
    List_Of_Prime=ListPrime(data_input)
    print("list of prime numbers:",List_Of_Prime)

if __name__=="__main__":
    main()