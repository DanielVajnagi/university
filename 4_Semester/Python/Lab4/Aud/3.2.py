from tkinter import *
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *
def close_win():
    if askyesno("Exit", "Do you want to quit?"):
        root.destroy()
def about():
 showinfo("Editor", "This is text editor.\n(test version)")
def _open():
 op = askopenfilename()
 for l in fileinput.input(op):
    txt.insert(END,l)
def _save():
 sa = asksaveasfilename()
 letter = txt.get(1.0,END)
 f = open(sa,"w")
 f.write(letter)
 f.close()
root = Tk()
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open...",command=_open)
fm.add_command(label="Save...",command=_save)
fm.add_command(label="Exit",command=close_win)
hm = Menu(m)
m.add_cascade(label="Help",menu=hm)
hm.add_command(label="About",command=about)
txt = Text(root,width=40,height=15,font="12")
txt.pack()
root.mainloop()
