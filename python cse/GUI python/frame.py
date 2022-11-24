from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()

buttonframe=Frame(root)
buttonframe.pack(side=BOTTOM)
redbutton = Button(frame,text="Red",fg="red")
redbutton.pack(side = LEFT)
greenbutton =Button(frame,text="Brown",fg="brown")
greenbutton.pack(side=LEFT)
bluebutton =Button(frame,text="Blue",fg="blue")
bluebutton.pack(side=LEFT)
pinkbutton =Button(frame,text="pink",fg="pink")
pinkbutton.pack(side=LEFT)
root.mainloop()



 
