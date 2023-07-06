def pattern(num):
    if num>0:
        print(num,end=" ")
        pattern(num-1)
pattern(7)