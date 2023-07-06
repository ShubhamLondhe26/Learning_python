def AreaofCircle(radius,pi=3.14):
    result=pi*radius*radius
    return result
def main():
    pivalue=3.14
    rvalue=10.5
#positional arguments
    ans=AreaofCircle(rvalue,pivalue)
    print("Area of Circle",ans)
#keyword arguments
    ans=AreaofCircle(pi=pivalue,radius=rvalue)
    print("Area of Circle",ans)
if __name__=="__main__":
    main()