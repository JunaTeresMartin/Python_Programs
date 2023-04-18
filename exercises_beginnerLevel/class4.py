class Car:
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def cost(self):
        print('Price of the car is',self.price)

c1=Car('Audi',1001,10000000)
c1.cost()
c2=Car('BMW',7601,9500000)
c2.cost()