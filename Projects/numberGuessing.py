import random

number=random.randint(0,40)

chance=5
print("hint: number between 0 and 40\n")
count=0
#total 5 chances
while(chance>0):
    guess=int(input("Enter a number:"))
    if guess==number:
        print("YOU WON!\n")
        break
    else:
        if(chance!=1):
           print("Sorry!Try again.\n")
           print("Want hint? y/n: ")
           hint=input()
           #3 hints can be given
           if(hint=='y'):
                count+=1

                if(count==1):
                   if(number>15):
                      print("Number is greater than 15")
                   else:
                      print("Number is less than 15")

                elif(count==2):
                   if(number%2==0):
                      print("number is even")
                   else:
                      print("number is odd")

                elif(count==3):
                   if(number<30):
                      print("number is less than 30")
                   else:
                      print("number is greater than 30")

                else:
                    print("No more hints")
          


       #chances is decremented
        chance-=1
        if(chance==1):
            print("One more chance\n")
        if(chance==0):
            print("Sorry!You lose.\n")
