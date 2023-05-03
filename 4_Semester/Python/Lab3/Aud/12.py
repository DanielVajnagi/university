import dbm
db=dbm.open('persondb', 'r') # відкрити сховище
k=len(db) # у сховищі маємо три  ̳рядки-записи‘
print(k)
print(list(db.keys())) # keys – це заголовок
a=list(db.keys())
while k>0: # звернення до записів БД
    f1=db[a[k-1]].decode()
    print(f1);  k-=1
print()
for key in db:
    print(key)
    # print(key, '=>', db[key])
print()
    
for key in sorted(db):
    print(key, '=>', db[key]) # Ітерації через відсортований
# список ключів
db.close() # закрити після внесення змін