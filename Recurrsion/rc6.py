def pattern1(num):
    if num<6:
        print(num,end=" ")
        pattern1(num+1)
pattern1(1)