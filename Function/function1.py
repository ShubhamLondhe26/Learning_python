#print(__name__)
#output
#__main__

def Demo():
    print('Good morning everyone')
def Demo1(value):
    print("inside demo1 arguments:",value)
    
def Demo2(value):
    print('inside demo2 arguments:',value)
    return value-5

def main():
    Demo()
    Demo1("String")
    ans=Demo2(10)
    print('return value of demo2: ',ans)

if __name__ == '__main__':#start of the program
    main()
