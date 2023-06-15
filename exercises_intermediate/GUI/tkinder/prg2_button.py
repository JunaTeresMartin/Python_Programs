from tkinter import *
root=Tk()

#text/input box
# myEntry=Entry(root,width=20,fg='white',bg='red')
myEntry=Entry()
myEntry.insert(0,"Enter your name here")
myEntry.pack()

def myClick():
    myLabel=Label(root,text="You have clicked a button")
    myLabel.pack()
def myInput():
    myType=Label(root,text="You typed: "+myEntry.get())
    myType.pack()
myButton=Button(root,text="Click here",pady=10,padx=15,command=myInput ,foreground='blue',background='green')#NOTE: NO NEED OF PARENTHESIS IN COMMAND FUNCTION
'''
foreground: color of text
background: color of button
command: don't put ()

'''
#disabling the button
# myButton=Button(root,text="Click here",state=DISABLED)
myButton.pack()
root.mainloop()
