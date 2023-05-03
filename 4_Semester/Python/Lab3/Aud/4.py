# Додано методи, які інкапсулюють операції
class Person:
 def __init__(self, name, job=None, pay=0):
  self.name = name; self.job = job
  self.pay = pay
 # метод «виведення прізвища»
 def lastName(self): #методи, які реалізують поведінку екземплярів
  return self.name.split()[-1] # self – екземпляр
 # метод «зміна зарплати»
 def giveRaise(self, percent):
  self.pay=int(self.pay*(1+percent)) # внесення змін
if __name__ ==  '__main__':
    bob = Person( 'Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay); print(sue.name, sue.pay)
    # використовують методи
    print(bob.lastName(),';', sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)