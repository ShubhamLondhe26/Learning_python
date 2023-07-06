#if....else statement
print("-"*50)

print("Check whether the given number is odd or even")
print("Enter Number :", end = " ")
num = int(input())
if ((num % 2)== 0):
    print("even number".upper())
else :
    print("odd number ".title())
    print(f"{num} is odd number")

print("-"*50)

print("Check eligibility:")
print("Enter age:", end = " ")
age = int(input())
if (age >= 18) :
    print("You are Eligible for voting")
else:
    print("You are not Eligible for voting")

print("-"*50)

print("Check the number is divisible by 5")
print("Enter Number :",end= "")
Num = int(input()) 
if (Num % 5 ) == 0 :
    print("Is number is divisible by 5 :", True)
else :
    print("Is number is divisible by 5 :", False)

