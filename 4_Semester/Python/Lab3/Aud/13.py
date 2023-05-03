import dbm
from person import Person, Manager
def Transform(a): #функция которая переводит строку в список c разделителем ','
    list=a.split(",")
    return list

db=dbm.open('persondb', 'n') # відкрити сховище
k=len(db) #  у сховищі маємо три  ̳записи‘
print(list(db.keys())) # keys – це заголовок
key=list(db.keys())
# відкрити у сховищі запис файлу за вказаним ключем
for i in sorted(key): # відобразити об‘єкти з БД
  print(i, '\t=>', db[i]) # Виведення в необхідному форматі
print()
while k>0: # звертаємося до записів БД
    if key[k-1]==b'Sue Jones':
        sue1=db[b'Sue Jones'].decode() # витягти запис за ключем
    # f1=db[key[k-1]].decode()
        print(sue1)
        break
    k-=1
l=Transform(sue1)
ssue=Person(l[0], l[1], l[2])
ssue.giveRaise(0.10) # змінити об‘єкт у пам‘яті

db[b'Sue Jones']=str(ssue)  

# db.close() # закрити  файл після внесення змін