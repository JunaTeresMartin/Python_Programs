f=open("myfile.txt",'w')
f.write("First line\nSecond line")
f.close()
f=open("myfile.txt",'r')
output=f.read()
print(output)
f.close()