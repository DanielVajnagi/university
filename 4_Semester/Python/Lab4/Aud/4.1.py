from tkinter import *
def printer(event):
 x = var.get()
 print(x)
root = Tk()
var = IntVar()
var.set(5)
sca1 = Scale(root,orient=VERTICAL,length=200,
 from_=0,to=10,tickinterval=2,resolution=1,
 variable=var)
sca2 = Scale(root,orient=HORIZONTAL,length=200,
 from_=0,to=10,tickinterval=2,resolution=1,
 variable=var)
lab=Label(root, text='Лабораторна робота \n Graphical User Interface',
 font='Arial 18')
but=Button(root, text='Get Variable',width=30,height=3,
 bg='grey',fg='red',font='Arial 12')
but.bind('<Button-1>',printer)
lab.pack()
sca1.pack()
sca2.pack()
but.pack()
root.mainloop()