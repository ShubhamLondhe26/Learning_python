def pattern(num):
    if(num>0):
        print("*",end=" ")
        pattern(num-1)
pattern(5)

