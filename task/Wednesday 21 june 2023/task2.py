#2)Write a recursive program which display below pattern.
#Input : 10
#Output :  10      9       8       7        6        5        4       3        2      1

def reverse(num):
    if(num>0):
        print(num,end=" ")
        reverse(num-1)
reverse(10)
