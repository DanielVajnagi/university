class Rectangle:
 """ Клас, який описує прямокутник """
 
 """ Конструктор класу
 :param side_a: перша сторона
 :param side_b: друга сторона """
 def __init__(self, side_a, side_b):
    self.side_a = side_a
    self.side_b = side_b
   
 """Метод, який повертає подання об'єкта у вигляді рядка """
 def __repr__(self):
    return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)
class Circle:
 """ Клас, який описує коло """
 def __init__(self, radius):
    self.radius = radius
 def __repr__(self):
    return 'Circle(%.1f)' % self.radius
 

 @classmethod

 def from_rectangle(cls, rectangle):
  """ Ми використовуємо метод класу в якості фабричного  методу,
 який створює екземпляр класу Circle з екземпляру
 класу Rectangle як коло, що вписане у цей прямокутник.
 :param rectangle: Rectangle instance
 :return: Circle instance """
  radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
  return cls(radius)
def main():
 rectangle = Rectangle(3, 4)
 print(rectangle)
 circle1 = Circle(1)
 print(circle1)
 circle2 = Circle.from_rectangle(rectangle)
 print(circle2)
if __name__ == '__main__': main()