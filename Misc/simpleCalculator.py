    
print("choose the opraters :")
print("-"*20)
print("1. Addition ")
print("2. subtraction ")
print("3. multiplication")
print("4. division")
print("5. modules ")
print("6. floor division ")
print("7. exponent ")

print("Please select option :",end="")
option=int(input())

print("Enter frist number :",end="")
num1=int(input())
print("Enter second number :",end="")
num2=int(input())

if(option<1 and option>7):
    print("Invalid choice : please select option 1 to 7")
    
elif(option==1):
    result=num1+num2
    print(f"addition of {num1} and {num2}is :",result)
    
elif(option==2):
    result=num1-num2
    print(f"subtraction of {num1} and {num2}is :",result)

elif(option==3):
    result=num1*num2
    print(f"multiplication of {num1} and {num2}is :",result)
    
elif(option==4):
    result=num1/num2
    print(f"division of {num1} and {num2}is :",result)
    
elif(option==5):
    result=num1%num2
    print(f"remainder of {num1} and {num2}is :",result)
    
elif(option==6):
    result=num1//num2
    print(f"floor division of {num1} and {num2}is :",result)
    
elif(option==7):
    result=num1**num2
    print(f"exponent of {num1} and {num2}is :",result)
    print()
        

