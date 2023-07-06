#Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
#There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
#ChkPrime() method will returns true if number is prime otherwise return false
#ChkPerfect () method will returns true if number is perfect otherwise return false.
#Factors () method will display all factors of instance variable.
#SumFactors() method will return addition of all factors. Use this method in any another method
#As a helper method if required.
#After Designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self,value):
        self.value=value
    def check_prime(self):
        if self.value<2:
            return False
        for i in range(2,int(self.value**0.5)+1):
            if self.value%i==0:
                return False
            return True
    def ChkPerfect(self):
        if self.value < 6:
            return False
        factors_sum = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                factors_sum += i
        return factors_sum == self.value
    def factors(self):
        factor=[]
        for i in range(1,self.value):
            if self.value%i==0:
                factor.append(i)
            return factor

    def SumFactors(self):
        pass
    
def main():
    value=int(input("Enter the number:"))
    obj=Numbers(value)
    print("Prime",obj.check_prime())
    print("Perfect",obj.ChkPerfect())
    print("Factors",obj.factors())
    print("Sum of factors",obj.SumFactors)
if __name__=="__main__":
    main()
