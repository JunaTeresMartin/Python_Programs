# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 09/08/2022
# _Description_: Python program to get IP address

import socket
hostname=socket.gethostname()
IPAddress=socket.gethostbyname(hostname)
print("Your Computer name is: "+hostname)
print("Your Computer IP Address is: "+IPAddress)