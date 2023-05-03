class Person:
    def __call__(self):
        return 'Person '
    

class Student(Person):
    def __call__(self):
        return 'Student '
    

class Chloe(Student):
    def __call__(self):
        return 'Chloe '
    

class Bob(Student):
    def __call__(self):
        return 'Bob '
    

class Peter(Student):
    def __call__(self):
        return 'Peter '
    

class Denis(Bob, Chloe):
    def __init__(self):
        self.name = 'Denis'
        
    def describe(self):
        return Student().__call__() + super().__call__() + f'({super(Bob, self).__call__()}) like {self.name}'
    

class Eelay(Chloe, Peter, Bob):
    def __init__(self):
        self.name = 'Eelay'
        
    def describe(self):
        return Student().__call__() + super().__call__() + f'({super(Chloe, self).__call__()}{super(Peter, self).__call__()}) like {self.name}'
    

class Forth(Peter, Bob):
    def __init__(self):
        self.name = 'Forth'
        
    def describe(self):
        return Student().__call__() + super().__call__() + f'({super(Peter, self).__call__()}) like {self.name}'

    
I1 = Denis()
I2 = Eelay()
I3 = Forth()

print(I1.describe())
print(I2.describe())
print(I3.describe())