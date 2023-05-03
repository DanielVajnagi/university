class First:
 color = "red"
 def out(self): print (self.color + "!")

obj1 = First(); obj2 = First()
# Обидва об‘єкта (obj1, obj2) мають два однакових атрибута:
# color - у вигляді властивості й printer (у вигляді методу)
print (obj1.color); print (obj2.color)
obj1.out(); obj2.out()