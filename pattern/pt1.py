#factors

#Method1
num=int(input("enter the number: "))
#for i in range(1,int(num/2)+1):
    #print(i)
#Method2
#for i in range(1,int(num*0.5)):
    #print(i)
#Method3
#for i in range(1,num+1):
    #if (num % i==0):
        #print(i)
i=1
while(i<=int(num/2)):
    if(num%i==0):
        print(i)
    i=i+1

#task ways to solve above
