##2)Create on module named ad Arithmetic which contains 4 functions as Add() for addition, Sub() for Subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user
import Q_2Module
def main():
    output=Q_2Module.addition(10,20)
    print("addition is ",output)
    output=Q_2Module.multiplication(10,20)
    print("multiplication is ",output)
    output=Q_2Module.divison(10,20)
    print("divison is ",output)
    output=Q_2Module.subtraction(10,20)
    print("subtraction is ",output)
if __name__=="__main__":
    main()