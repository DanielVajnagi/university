# Додано підклас, який адаптує поведінку суперкласу
class Person:
 def __init__(self, name, job=None, pay=0):
  self.name = name; self.job = job; self.pay = pay
 def lastName(self):
  return self.name.split()[-1]
 def giveRaise(self, percent):
  self.pay = int(self.pay*(1+percent))
 def __str__(self):
  return  '[Person: %s, %s]' % (self.name, self.pay)
class Manager(Person):
 def giveRaise(self, percent, bonus=.10): # Перевизначення метода
  Person.giveRaise(self,percent+bonus) #Виклик м-ду з класу Person

if __name__ == '__main__':
 bob = Person('Bob Smith')
 sue = Person('Sue Jones',job='dev',pay=100000)
 print(bob);print(sue);print(bob.lastName(),sue.lastName())
 sue.giveRaise(.10); print(sue)
 tom = Manager('Tom Jones',  'mgr', 50000)
 # екземпляр Manager: __init__
 tom.giveRaise(.10) # Виклик адаптованої версії
 print(tom.lastName()) # Виклик успадкованого метода
 print(tom) # Виклик успадкованого __str__
 
if __name__== '__main__':
    print('--All three--')
    for object in (bob, sue, tom):
       # Обробка об‘єктів узагальненим способом
       object.giveRaise(.10) #викличе метод giveRaise цього об‘єту
       print(object) #викличе  метод __str__