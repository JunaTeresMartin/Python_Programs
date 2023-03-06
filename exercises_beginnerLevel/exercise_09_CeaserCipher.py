#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program to do ceaser cipher of a string to encrypt/encode the message
#DATE     :  06-03-2023

string=input("Enter a string: ")
cipher_string=""
distance=int(input("Enter a distance: "))
for i in string:
    asci=ord(i)
    if asci>=ord("a") and asci<=ord("z"):
        cipher_value=asci+distance
        if cipher_value>ord("z"):
            cipher_value=(cipher_value-ord("z"))+(ord("a")-1)
            cipher_string+=chr(cipher_value)
        else:
            cipher_string+=chr(cipher_value)
    elif asci>=ord("A") and asci<=ord("Z"):
        cipher_value=asci+distance
        if cipher_value>ord("Z"):
            cipher_value=(cipher_value-ord("Z"))+(ord("A")-1)
            cipher_string+=chr(cipher_value)
        else:
            cipher_string+=chr(cipher_value)
print(cipher_string)
