#1)Write a program which contains one function names as Check_Num ( ) which accept one parameter as number. If number is even then it should display “Even Number” herwse display “Odd number” 

def Check_Num(num):
    if num%2==0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    output=Check_Num(3)
    print(output)
    
if __name__=="__main__":
    main()