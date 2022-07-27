# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 27/07/2022
# _Description_: Python Program to check whether a string is palindrome or not


string=input("Enter the string: ")

if string[::-1]==string:
    print("Is palindrome")
else:
    print("not palindrome")