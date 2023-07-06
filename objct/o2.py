class Name:
    def __init__(self,name,mname,lname):
        self.no1=name
        self.no2=mname
        self.no3=lname
    def Full_name(self):
        return self.no1+self.no2+self.no3
def main():
    obj=Name("Shubham ","Chandrakant ","Londhe")
    ans=obj.Full_name()
    print(ans)

if __name__=="__main__":
    main()