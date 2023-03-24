#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Converts a decimal integer to its binary number
#LAST DATE MODIFIED  :  24-03-2023

decimalNumber=int(input("Enter a decimal number: "))
binary=""
if decimalNumber==0:
    print(0)
else:
    while decimalNumber>0:
        remainder=decimalNumber%2
        #print(remainder)
        decimalNumber//=2
        binary=str(remainder)+binary
print(binary)