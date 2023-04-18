# Клас, який описує людину
class Person:
 # Перший аргумент, який вказує на поточний екземпляр класу,
 # прийнято називати self
 def print_info(self):
    print(self.name, 'is', self.age)
# Створення екземплярів класу
alex=Person(); alex.name='Alex'; alex.age=18
john = Person(); john.name = 'John'; john.age = 20
# Перевіримо, чим є атрибут-функція print_info класу Person
print(type(Person.print_info)) # функція (<class 'function'>)
# Викличемо його для об‘єктів alex і john
Person.print_info(alex)
Person.print_info(john)
# Метод – функція, зв‘язана з об‘єктом. Всі атрибути класу, які є
# функціями, описують відповідні методи екземплярів даного класу
print(type(alex.print_info)) # метод (<class 'method'>)
# Виклик методу print_info
alex.print_info()
john.print_info()
