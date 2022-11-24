from tkinter import*
root=Tk()

#list
Lb1=Listbox(root)
Lb1.insert(1,"python")
Lb1.insert(2,"perl")
Lb1.insert(3,"3")
Lb1.insert(4,"PHP")
Lb1.insert(5,"JSP")
Lb1.insert(6,"Ruby")

Lb1.pack()


#entery
e=Entry(root,width=50)
e.pack()

def myclick():
    label=Label(roottext="Hello! good afternoon "+e.get())
    label.pack()

button=Button(root,text="Submit",command=myclick)
button.pack()

root.mainloop()