#without name
#Anonymous function
#lambda as a keyword
#syntax-lambda arguments:expression

add=lambda a,b,c:a+b+c
#add(12,12,12)
#print("Addition using lambda function:",add)
Ans=add(12,13,14)
print("Addition using lambda function:",Ans)
print("Data type of lambda function:",type(add))

add=lambda a,b,c:print(a+b+c)
print(type(add))
add(12,13,14)

#square
print("Squarring the number:")
num=[1,2,3,4,5,6]
square=[]
for i in num:
    sq_num=lambda i:i*i
    square.append(sq_num(i))
print(num,"of given list",square)

#even odd
check_num=lambda num :print(num,"is even") if (num%2==0) else print(num,"is odd")
check_num(23)

#max digit
check_digit=lambda num: print(num) 


# using main function:
def main():
    num1=int(input("Enter the First Number: "))
    num2=int(input("Enter the Second Number: "))
    multi=lambda num1,num2:num1*num2
    ans=multi(num1,num2)
    print("Mulitplication is",ans)
if __name__=="__main__":
    main()

