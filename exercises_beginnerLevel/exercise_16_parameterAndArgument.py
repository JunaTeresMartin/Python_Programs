#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to demonstrate a function with parameters
#DATE     :  13-03-2023

def greet_with(name,location): #name and location are called parameters
    print(f"Hello {name}!")
    print(f"How is it in {location}")

greet_with("juna","tvm") #passing arguments
greet_with(location="tvm",name="Joe")