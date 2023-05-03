import shelve

db=shelve.open('persondb', 'r') # відкрити сховище
print(len(db)) # у сховищі маємо три  ̳записи‘
print(list(db.keys())) # keys – це заголовок

bob = db['Bob Smith'] # витягти об‘єкт bob за ключем
print(bob) # викличе метод __str__
print(bob.lastName()) # Викличе lastName з класу Person
for key in db: # Ітерації, витягання, виведення
    print(key, '=>', db[key])
for key in sorted(db):
    print(key,'=>',db[key]) #Ітерації через відсортований список
    