class Base:
    attr = 'Base attribute'
    
    def method(self):
        print('Base method, current class is', self.__class__.__name__)
        
        
class Child(Base):
    attr = 'Redefined attribute'
    
    @staticmethod
    def get_superclass_attr():
        return Base.attr  # getting the attribute of the Base class
    
    def method(self):  # overriding the method
        Base.method(self)  # calling the superclass method
        print('Child method, current class is', self.__class__.__name__)
        
            
def main():
    print('Base:')
    print(Base.attr)
    base_instance = Base()
    base_instance.method()
    
    print()
    
    print('Child:')
    print(Child.attr)
    print(Child.get_superclass_attr())
    child_instance = Child()
    child_instance.method()
    
    
if __name__ == '__main__':
    main()
