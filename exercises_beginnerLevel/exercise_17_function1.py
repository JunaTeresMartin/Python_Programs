#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to calculate the number of cans needed to paint a wall with given height and width
#DATE     :  15-03-2023

def paint_calc(height,width,cover):
    no_of_cans=math.ceil(height*width/cover)
    print(f"You'll need {no_of_cans} cans of paint.")
import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)