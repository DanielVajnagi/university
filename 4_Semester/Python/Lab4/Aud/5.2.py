def add_triangle(event):
    coords = [(50,130,290,40,170,250),(10,10,290,30,200,250),(30,280,330,60,300,200),(50,200,340,200,110,60)]
    colors = ['red','green','blue','yellow']
    global i
    canvas.itemconfig(t,fill=colors[i],outline='white')
    canvas.coords(t,coords[i])
    i += 1
    if i == 4:
        i = 0
def triangle():
    canvas.coords(r,(0,0,0,0))
    canvas.itemconfig(t,fill='yellow',outline='white')
    canvas.coords(t,(50,200,340,200,110,60))
    text.delete(1.0,END)
    text.insert(1.0,'Tреугольник -\nэто геометрическая фигура, \
образованная тремя отрезками, которые соединяют три не лежащие \
на одной прямой точки.')
    text.tag_add('title','1.0','1.end')
    text.tag_config('title',font=('Times',14),foreground='red')
def rectangle():
    canvas.coords(t,(0,0,0,0,0,0))
    canvas.itemconfig(r,fill='lightblue',outline='white')
    canvas.coords(r,(80,50,360,200))
def ellipse():
    pass

from tkinter import *
win = Tk()
b_triangle = Button(text="Треугольник", width=15,command=triangle)
b_rectangle = Button(text="Прямоугольник",
width=15,command=rectangle)
b_ellipse = Button(text="Эллипс", width=15,command=ellipse)
canvas = Canvas(width=400,height=300,bg='#222222')
text = Text(width=55,height=5,bg='#ffffff',wrap=WORD)
t = canvas.create_polygon(0,0,0,0,0,0)
canvas.tag_bind(t,'<Button-1>',add_triangle)
r = canvas.create_rectangle(0,0,0,0)
b_triangle.grid(row=0,column=0)
b_rectangle.grid(row=1,column=0)
b_ellipse.grid(row=2,column=0)
canvas.grid(row=0,column=1,rowspan=10)
text.grid(row=11,column=1,rowspan=3)
win.mainloop()