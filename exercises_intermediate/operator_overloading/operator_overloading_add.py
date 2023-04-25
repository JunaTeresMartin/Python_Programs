class Complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,o): #add/sub/mul/div
        r=self.a+o.a  #real part
        i=self.b+o.b  #imaginery part
        return Complex(r,i) #returns an object
    def display(self):
        if self.b>0:
            print(f"Complex no: is {self.a} + {self.b}j")
        elif self.b==0:
            print(f"Complex no: is",self.a)
        else:
            print(f"Complex no: is {self.a}{self.b}j")

object1=Complex(2,-5)
object2=Complex(3,4)
c=object1+object2
c.display()
print()
