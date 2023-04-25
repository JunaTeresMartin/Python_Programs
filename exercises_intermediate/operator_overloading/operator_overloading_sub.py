class Subtraction:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __sub__(self,other): #self takes LHS of - and other takes RHS of -
        result=self.n1-other.n1
        return result

s1=Subtraction(100,5)
s2=Subtraction(5,5)
s=s1-s2
print(s)