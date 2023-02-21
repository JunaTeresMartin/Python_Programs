#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#DATE     :  21-02-2023


age = input("What is your current age? ")
a=int(age)
years_remaining=90-a
months=years_remaining*12
days=years_remaining*365
weeks=years_remaining*52
print(f"You have {days} days, {weeks} weeks, and {months} months left.")




