#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program that automatically prints the solution to the FizzBuzz game
#DATE     :  09-03-2023

for i in range(1,101):
    if i%15==0:
        #first check the divisibility with 15 as eg:15 can be divisible with 3 and prints "fizz" if we put it first
        #logic of the program
        #if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
        print("FizzBuzz")
    elif i%5==0:
        #When the number is divisible by 5, then instead of printing the number it should print "Buzz".
        print("Buzz")
    elif i%3==0:
        #When the number is divisible by 3 then instead of printing the number it should print "Fizz".
        print("Fizz")
    else:
        print(i)