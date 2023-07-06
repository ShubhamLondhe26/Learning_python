def pattern(num):
    if num>0:
        print(num, end=" ")
        num=num-1
        pattern(num)
pattern(5)



