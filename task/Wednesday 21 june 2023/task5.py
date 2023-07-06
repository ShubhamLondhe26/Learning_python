#5) Write a program which contains one lambda function which accepts one parameter and return power of two

power_of_two=lambda x:x**2
def main():
    value = int(input("Enter a number: "))
    result = power_of_two(value)
    print(f"The power of two of {value} is {result}")
if __name__=="__main__":
    main()