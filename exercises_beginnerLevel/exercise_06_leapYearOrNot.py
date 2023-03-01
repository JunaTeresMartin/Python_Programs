#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that finds out whether if a given year is a leap year.
#DATE     :  26-02-2023


year = int(input("Which year do you want to check? "))

if year%4==0:
    if year%100:
        if year%400==0:
           print("Leap year")
        else:
           print("Not leap year.")
    else:
        print("Leap year.") 
else:
    print("Not leap year.")


