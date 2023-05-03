# Клас, який описує людину
class Person: pass
# Створення екземплярів класу
alex = Person()
alex.name = 'Alex'; alex.age = 18
john = Person()
john.name = 'John'; john.age = 20
# Атрибути-дані відносять тільки до окремих екземплярів класу
# і ніяк не впливають на значення відповідних атрибутів-даних
#інших екземплярів
print(alex.name, 'is', alex.age); print(john.name, 'is', john.age)
