import shelve
db = shelve.open('persondb')
# відкрити у сховищі файл з вказаним ім‘ям
for key in sorted(db): # відобразити об‘єкти з БД
 print(key,  '\t=>', db[key]) 
sue=db['Sue Jones'] # витягти об‘єкти за ключем
sue.giveRaise(.10) # змінити об‘єкт у пам‘яті шляхом виклику метода

db['Sue Jones']=sue # присвоїти за ключем,
# щоб оновити об‘єкт у сховищі
db.close() # закрити  файл після внесення змін