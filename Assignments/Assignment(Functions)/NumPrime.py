def Check_Prime(No):
    i=0
    Flag=True
    for i in range(2,int(No/2)+1):
        if(No%i==0):
            Flag=False
            break
    return Flag