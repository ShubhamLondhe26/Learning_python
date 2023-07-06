def Square_pattern(num):
    for i in range(0,num):
        for j in range(num):
            print("*", end=" ")
        print("\r")
def Simple_pyramid_pattern(num):
    for i in range(0,num):
        for j in range(i):
            print("*", end=" ")
        print("\r")
def pattern1(num):
    for i in range(0,num):
        for j in range(num-i):
            print("*", end=" ")
        print("\r")
def pattern(num):
    for i in range(0,num):
        for j in range(num-i):
            print(" ", end=" ")
        for k in range(num):
            print("*", end=" ")
        print("\r")
def main():
    num=int(input("Enter the number: "))
    Square_pattern(num)
    Simple_pyramid_pattern(num)
    pattern1(num)
    pattern(num)
 
if __name__=="__main__":
    main()
