#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to find the average of heights of students using for loop in list
#DATE     :  08-03-2023

heights=input("Enter the heights in space: ").split()
for h in range(0,len(heights)):
    heights[h]=int(heights[h])
print(heights)
sum=0
for h in heights:
    sum+=h
print(f"Average= {round(sum/len(heights))}")