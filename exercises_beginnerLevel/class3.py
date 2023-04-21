class Rectagle:
    def __init__(self,l,b):
        self.lenght=l
        self.breadth=b
    def area(self):
        RectArea=self.lenght*self.breadth
        return RectArea
    
RectLength=float(input("Enter the length of the rectangle: "))
RectBreadth=float(input("Enter the breadth of the rectangle: "))
r=Rectagle(RectLength,RectBreadth)

print('Area of the rectangle is',r.area())