from tkinter import *
root = Tk()
def sq1():
 fra.config(width=200,height=200)
 print('200x200')
def sq2():
 fra.config(width=400,height=400)
 print('4000x4000')
fra = Frame(root,width=300,height=100,bg="Black")
fra.pack()
m = Menu(root)
root.config(menu=m)
cm = Menu(m)
m.add_cascade(label="File",menu=cm)
sm = Menu(m)
m.add_cascade(label="Edit",menu=sm)
sm.add_command(label="200x200",command=sq1)
sm.add_command(label="4000x4000",command=sq2)
root.mainloop()
