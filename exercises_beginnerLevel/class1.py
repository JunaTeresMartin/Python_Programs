class Students:
    total=0 #class variable
    def __init__(self,name,roll,total_marks=0):
        self.name=name
        self.roll=roll
        #self.total_marks=total_marks
        Students.total+=1
        print(f'A new student {self.name} is added with roll no {self.roll}')
        print(f'total number of student is {Students.total}')
    def getmarks(self,marks):
        for m in marks:
            self.total_marks+=m
        self.avg=self.total_marks/len(marks)
    def average(self):
        return self.avg


s1=Students('juna',36,0)
s2=Students('Johns',10)

s1.getmarks([25,12,22])
print('total marks:',s1.total_marks)
print('average mark:',s1.average())
print(s1.name)
print('location:',s1)
