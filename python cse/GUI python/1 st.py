from cProfile import label
from this import d
from tkinter import *
root=Tk()

#Canvas
w=Canvas(root,width=40,height=40)
label=Label(root,text="My first tkinter program")
label1=Label(root,text="I know how to use GUI").grid(row=0,column=3)
#label.pack()
label.grid(row=0,column=1)
#x=canvas_width/2
#x1=70
#y1=90
#x2=78
#y2=33
#w.create_line(x1,y1,x2,y2)
w.create_line(100,32,200,32,width=5)
w.grid()
#button
button=Button(root,text="Submit")
button.grid(row=10,column=20)   
#entry
e=Entry(root,width=50,bg="yellow",fg="purple",borderwidth=5)
e.grid(row=1,column=1)


root.mainloop()