# Клас, який описує людину
class Person:
 # Конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age
 # Метод з попереднього прикладу
    def print_info(self):
        print(self.name, 'is', self.age)
# Створення екземплярів классу
alex = Person('Alex', 18)
john = Person('John', 20)
# Виклик метода print_info
alex.print_info()
john.print_info()
