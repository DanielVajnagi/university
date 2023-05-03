class Person:
     def __init__(self, name, job=None, pay=0):
      self.name=name; self.job=job; self.pay = pay


bob = Person( 'Bob Smith') # Тестування класу
sue = Person( 'Sue Jones', job='dev', pay=100000)
# автоматично запустить __init__
print(bob.name, bob.pay); print(sue.name, sue.pay)
# атрибути в об‘єктах bob, sue різняться

