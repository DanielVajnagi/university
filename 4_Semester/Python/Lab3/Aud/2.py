class Person:
 def __init__(self, name, job=None, pay=0):
  self.name=name; self.job=job; self.pay=pay
if __name__ ==  '__main__':
# коли файл запускають для тестування
 bob = Person( 'Bob Smith')
 sue = Person( 'Sue Jones', job='dev', pay=100000)
 print(bob.name, bob.pay); print(sue.name, sue.pay)
 print( '{0} {1}' .format(bob.name, bob.pay)) # метод format
 print( '%s %s' %(bob.name, bob.pay)) # вираз форматування

