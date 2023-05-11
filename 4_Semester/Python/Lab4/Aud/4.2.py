from tkinter import *
root = Tk()
myscrollbar = Scrollbar(root)
myscrollbar.pack(side=RIGHT, fill=Y)
mylistbox = Listbox(root, yscrollcommand = myscrollbar.set)
for a in range(20):
 mylistbox.insert(END,'Lumberjack-' + str(a))
mylistbox.pack(side=LEFT, fill=BOTH)
myscrollbar.config(command=mylistbox.yview)
root.mainloop()
