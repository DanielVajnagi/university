# Файл makedb.py: зберігає об‘єкти Person у сховищі
from person import Person, Manager # імпортує класи
bob = Person('Bob Smith') # створення об‘єктів для зберігання
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)
import shelve
db = shelve.open('persondb') # ім‘я файлу у сховищі
for object in (bob, sue, tom): # як ключ використати атрибут name    
    db[object.name] = object # зберегти об‘єкт у сховищі
    # db.close() # закрити після внесення змін