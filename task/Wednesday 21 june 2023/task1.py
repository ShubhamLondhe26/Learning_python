#1)Write a recursive program which display below pattern.
#Input : 5
#Output :  *	    *       *	 *        *  

def pattern(num):
    if(num>0):
        print("*",end=" ")
        pattern(num-1)
pattern(5)