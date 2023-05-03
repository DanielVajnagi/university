# Файл makedb.py: зберігає об‘єкти Person у сховищі
import dbm
from person import Person, Manager # імпортує класи

bob=Person('Bob Smith') # створення об‘єктів для зберігання
sue=Person('Sue Jones', job='dev', pay=100000)
tom=Manager('Tom Jones', 50000)
db = dbm.open('persondb','n') # ім‘я файлу у сховищі
for object in (bob,sue,tom): # як ключ використати атрибут
    print(object)
    db[object.name]=str(object) # зберегти об‘єкт у сховищі
    
print(len(db))
# db.close() # закрити після внесення змін