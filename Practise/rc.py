def count(num):
    if num>0:
        print("*",end=" ")
        count(num-1)
count(5)