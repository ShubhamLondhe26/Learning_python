def sum_of_digits(num):
    if num==0:
        return 0
    else:
        return(num%10)+ sum_of_digits(num//10)

def main():
    num = int(input("Enter the number: "))
    num1 = num
    output = sum_of_digits(num)
    print(f"The sum of digits in {num1} is {output}")

if __name__ == "__main__":
    main()