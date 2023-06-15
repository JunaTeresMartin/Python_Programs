from tkinter import *
root= Tk() #root widget

myLabel1=Label(root,text="Enter first number:")
myEntry1=Entry(root,width=5)
myLabel2=Label(root,text="Enter second number:")
myEntry2=Entry(root,width=5)
myLabel1.pack()
myEntry1.pack()
myLabel2.pack()
myEntry2.pack()
# myLabel1.grid(row=1,column=1)
# myLabel2.grid(row=3,column=1)
# myEntry1.grid(row=2,column=1)
# myEntry2.grid(row=4,column=1)
def clicked():
    sum=int(myEntry1.get())+int(myEntry2.get())
    label=Label(root,text="Sum= "+str(sum))
    label.pack()

myButton=Button(root,text="calculate sum",command=clicked)
myButton.pack()
root.mainloop()
