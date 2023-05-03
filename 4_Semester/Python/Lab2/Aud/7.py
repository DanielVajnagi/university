class Base:
    attr = 'Base attribute'
    
    def method(self):
        print('Base method, current class is', self.__class__.__name__)

class Child(Base):
    attr = 'Redefined attribute'
    
    def get_superclass_attr(self):
        return super().attr  # отримання атрибуту класа Base
    
    def method(self):  # перевизначення методу
        super().method()  # виклик метода суперкласу
        print('Child method, current class is', self.__class__.__name__)

def main():
    print('Base:')
    print(Base.attr)
    base_instance = Base()
    base_instance.method()
    print()

    print('Child:')
    print(Child.attr)
    child_instance = Child()
    print(child_instance.get_superclass_attr())
    child_instance.method()
    print()

    # super можна викликати де завгодно, навіть за межами класу
    super(Child, child_instance).method()

if __name__ == '__main__':
    main()
