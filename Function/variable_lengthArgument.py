#Variable Length argument
#1)Non-Keyword argument-(*args)
#2)keyword argument-(**Kwargs)

#Non-Keyword argument-

def additon(*values):
    Sum=0
    for no in range(len(values)):
       Sum=Sum+values[no]
    return Sum
def multiplication(*values):
    Sum=1
    for no in range(len(values)):
       Sum=Sum*values[no]
    return Sum
def main():
    ans=additon(1,2,3,4,5,6)
    print("Addition is: ",ans)
    ans=multiplication(1,2,3,4,5,6)
    print("Multiplication is: ",ans)

if __name__=="__main__":
   main()