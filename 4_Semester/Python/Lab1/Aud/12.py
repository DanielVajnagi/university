class MyClass:
 def __init__(self):
    self.password = None
 
 """Метод __getattribute__ викливають при отриманні
атрибутів"""
 # Якщо поле-запит secret_field і пароль правильний
 def __getattribute__(self, item):
    if item == 'secret_field' and self.password == '9ea)fc':
 
        return 'secret value'
    else:
        return object.__getattribute__(self, item)
        # то повертаємо значення
 # инакше викликаємо метод __getattribute__ класу object

 
obj = MyClass()# Створення екземпляру класу
# Розблокування секретного поля
# obj.password = '9ea)fc'
# Виведення значення secret field.
# Значення буде отримано, якщо розкоментувати попередній
# рядок програмного коду, інакш отримаємо помилку
print(obj.secret_field)
