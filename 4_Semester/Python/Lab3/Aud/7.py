# Файл person.py - опис класів
class Person:
    def __init__(self, name, job=None, pay=0): 
        self.name=name
        self.job=job
        self.pay=float(pay)
        
    def lastName(self): #методи, які реалізують екземплярів
        return (self.name.split()[-1]) # self – екземпляр
    def giveRaise(self, percent):
        self.pay=int(self.pay*(1+percent)) # внесення змін 
    def __str__(self): 
        return ('%s, %s, %s' %(self.name,self.job, self.pay))
       # рядок для виведення
class Manager(Person):
    def __init__(self,name,pay): # перевизначений конструктор
       Person.__init__(self,name,'mgr',pay)
    # Виклик конструктора зі значенням job= ̳mgr‘
    def giveRaise(self, percent, bonus=.10):
       Person.giveRaise(self, percent+bonus)
if __name__=='__main__':  # файл запускають для тестування
    bob = Person('Bob Smith')
    sue=Person('Sue Jones', job='dev', pay=100000)
    print(bob); print(sue)
    print(bob.lastName(),';', sue.lastName())
    sue.giveRaise(.10) # використовують методи
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10) # Виклик адаптованої версії
    print(tom.lastName()) # Виклик успадкованого метода
    print(tom) # Виклик успадкованого __str__
