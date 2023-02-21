#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that calculates the Body Mass Index (BMI) from a user's weight and height
#DATE     :  21-02-2023


#The BMI is a measure of someone's weight taking into account their height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi=int(weight)/float(height)**2
print(int(bmi))