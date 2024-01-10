class Emp:
    raise_amount=0  
    @classmethod
    def set_raise_amount(cls):
        incr=float(input("enter the raise amount"))

    def __init__(self,name,age,sal):
        self.name=name 
        self.age=age
        self.sal=sal 
   
    def increase_sal(self):
        self.sal=self.sal*(incr/100)+self.sal 
        
    def display(self):
        print(self.name,self.age,self.sal) 

e1=Emp("gopi",20,100)  

e2=Emp("sai",21,200)   
print("before inc")  
print("__________________________")
e1.display() 
e2.display() 
print("after the increment ") 
e1.increase_sal() 
e1.display() 
e2.display()

