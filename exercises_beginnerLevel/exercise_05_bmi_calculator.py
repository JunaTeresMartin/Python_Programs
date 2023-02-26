#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  BMI Calculator
#DATE     :  26-02-2023


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m)
bmi=round(weight/height**2)
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>18.5 and bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi>25 and bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>30 and bmi<35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi>35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
