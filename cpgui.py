from Tkinter import *
import tkMessageBox
root = Tk()
frame = Frame(root, width=100, height=100)
w0 = Label(root,text = "Select your current education:")
w0.pack()
listbox1 = Listbox(root)
listbox1.pack()
listbox1.insert(END,"High School")
listbox1.insert(END,"Bachelors")
#print listbox1[ACTIVE]
w = Label(root,text = "Enter your target profession:")
w.pack()
e = Entry(root)
e.pack()
def callback():
    tkMessageBox.showinfo(
        "INFORMATION",
        "You entered" + str(listbox1.curselection())
        )
    return
b = Button(root,text="get",width=10,command=callback)
b.pack()
if listbox1.curselection == "('0',)":
    print "ZERO SELECTED"
elif listbox1.curselection == "('1',)":
    print "ONE SELECTED"
root.mainloop()
