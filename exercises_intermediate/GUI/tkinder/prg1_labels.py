from tkinter import *
root= Tk() #root widget
#adding label to the root widget
myLabel1=Label(root,text="Hello World")
myLabel1.grid(row=1,column=0)
myLabel3=Label(root,text="                                ")
myLabel3.grid(row=1,column=5)
myLabel2=Label(root,text="This is python programming")
myLabel2.grid(row=2,column=1) #relative positioning
# myLabel.pack() #fitting it to the root widget
root.mainloop()
