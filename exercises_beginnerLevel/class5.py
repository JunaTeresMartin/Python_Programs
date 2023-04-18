class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def dataprint(self):
        print(self.name,self.roll)

student1=Student("Juna",36)
student1.dataprint()
student2=Student('Joe',10)
student2.dataprint()