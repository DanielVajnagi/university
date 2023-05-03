class MyClass:
 # Оголошення атрибута класу
 class_attribute = 8
 def __init__(self): # Конструктор
    self.data_attribute = 42
 # Статичний метод (у нього немає параметру) self,
 # оскільки він не зв‘язаний з жодним із екземплярів класу
 # не має доступу до атрибутівм-даних
 @staticmethod
 def static_method():
    print(MyClass.class_attribute)
 def instance_method(self): # звичайний метод
    print(self.data_attribute)
if __name__ == '__main__':
 # Виклик статичного методу
 MyClass.static_method()

 # Інстанціювання об‘єкта
 obj = MyClass()
 # Виклик методу
 obj.instance_method()
 # Аналогічно атрибутам класу, доступ до статичних методів
 # можна отримати й через екземпляр класу
 obj.static_method()