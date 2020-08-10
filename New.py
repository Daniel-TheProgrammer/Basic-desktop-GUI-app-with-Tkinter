from tkinter import*
import os


root=Tk()
root.title('Daniel.com-Code daily!')
root.geometry("400x600")

def Hello():
    Hello_label= Label(root, text="Hello " + myTextbox.get())
    Hello_label.pack()

myLabel = Label(root,text="Enter your first name:")
myLabel.pack()


myTextbox = Entry(root,width=30)
myTextbox.pack()

myButton = Button(root,text="Submit",command=Hello)
myButton.pack()



root.mainloop()
