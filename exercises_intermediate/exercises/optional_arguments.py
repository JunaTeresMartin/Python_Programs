def myfunction(name='George'):
    print("Hello",name)
myfunction('James') #In this case, we don't need to specify the name of the argument, because it's unambiguous
myfunction(name='Lilly')
myfunction()