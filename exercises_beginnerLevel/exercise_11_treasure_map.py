#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  write a program that allows you to mark a square on the map using a two-digit system. 
#DATE     :  08-03-2023


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

a=int(position[0])
b=int(position[1])
map[b-1][a-1]="x"
#display
print(f"{row1}\n{row2}\n{row3}")

