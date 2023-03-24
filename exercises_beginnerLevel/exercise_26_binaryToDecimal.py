#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Converts a string of bits to a decimal integer
#LAST DATE MODIFIED  :  24-03-2023

binaryNumber=input("Enter a binary number: ")
decimal=0
count=len(binaryNumber)-1
#eg: 1010 to 10
for digit in binaryNumber:
    decimal=decimal+int(digit)*2**count
    count-=1
print("Decima of",binaryNumber,"is",decimal)
