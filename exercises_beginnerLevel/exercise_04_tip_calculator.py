#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Tip Calculator
#DATE     :  21-02-2023

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


bill=float(input("Enter yoy bill amount: "))
tip=int(input("Tip percentage you would like to give:"))
n=int(input("number of people to split: "))
amount_with_tip=tip/100*bill + bill
bill_per_person=amount_with_tip/n
amount="%.2f" % round(bill_per_person,2)
print(f"Amount to be paid by each person is {amount}")