class MyClass:
 int_field = 8
 str_field = 'a string'
# Звернення до атрибутів класу
print (MyClass.int_field); print (MyClass.str_field)
# Створення двох екземплярів класу
object1 = MyClass (); object2 = MyClass ()
# Звернення до атрибутів класу через його екземпляри
print (object1.int_field); print (object2.str_field)
# Всі перераховані вище звернення до атрибутів насправді відносяться
# до двох одних і тих самих змінних
# Зміна значення атрибута класу
MyClass.int_field = 10
print (MyClass.int_field); print (object1.int_field); print
(object2.int_field)
# Однак, аналогічно до глобальних і локальних змінних,
# присвоєння значення атрибуту об'єкта не змінює значення
# атрибута класу, а веде до створення атрибута даних (нестатичного поля)
object1.str_field = 'another string'
print(MyClass.str_field); print(object1.str_field);
print(object2.str_field)
