#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Local and Global scope
#DATE     :  18-03-2023


#LOCAL SCOPE
def nutrition1():
    nutrient='Fiber'
    print(nutrient) #local variable #function defined inside inside a function
nutrition1()
#print(nutrient) #gives error, NameError: name 'nutrient' is not defined

print()

#GLOBAL SCOPE
#avialable anywhere in the file
nutrient='calcium'
def nutrition2():
    print(nutrient) #Global variable
nutrition2() #Global variable

#BLOCK SCOPE (There is NO block scope)
age=25
if age>15:
    name='john'
    print(name)
print(name) #no error