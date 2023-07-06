def add(No1,No2):
    print('addition and return',No1,No2)
    add=No1+No2
def sub(No1,No2):
    print('subtraction and return',No1,No2)
    sub=No1-No2
    return sub
def multi(No1,No2):
    print('multiplication and return',No1,No2)
    multi=No1*No2
    return multi

def main():
    ans=add(12,21)
    print('additon of',ans)
    ans1=sub(21,12)
    print('subtraction of',ans1)
    ans2=multi(10,10)
    print('multiplication of ',ans2)
if __name__ == "__main__":
    main()
