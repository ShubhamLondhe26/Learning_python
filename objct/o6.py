class Mobile:
    def __init__(self,model,color,ram):
        self.model=model
        self.color=color
        self.ram=ram
    def display(self):
        print("Mobile Spcification:\n",self.model,self.color,self.ram)

object1=Mobile("Realme","White","8GB")
object1.display()
    
        