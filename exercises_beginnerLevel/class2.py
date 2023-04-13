class Arith:
    def read(self):
        print("Enter 2 numbers: ")
        self.n1=int(input())
        self.n2=int(input())
    def add(self):
        self.sum=self.n1+self.n2
        return (self.sum)
a=Arith()
a.read()
s=a.add()
print('Sum: ',s)
