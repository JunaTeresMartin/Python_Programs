# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 24/07/2022
# _Description_: program to check leap year or not

year=int(input("Enter a year: "))
if year%400==0 or year%100!=0 and year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
