# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 23/08/2022
# _Description_: Program to display calendar of the given month and year

import calendar

yr=int(input("Enter Year: "))
mm=int(input("Enter Month: "))

print(calendar.month(yr,mm))


