def display(no):
    if(no<5):
        no=no+1
        print(no)
        display(no)
display(0)

def display1(num):
    count=0
    while(num<5):
        count=count+1
    print(count)
display(0)
