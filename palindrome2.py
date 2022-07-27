# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 27/07/2022
# _Description_: Python Program to check whether a string is palindrome or not

def palindrome(s):
    count=0
    for i in range (0,int(len(s)/2)):
        if(s[i]==s[len(s)-i-1]):
            count=count+1
    if count==0:
        print("The given string is not a palindrome")   
    else:
        print("The given string is a palindrome") 

string=input("Enter a string: ")
palindrome(string)