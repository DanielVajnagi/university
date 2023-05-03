class A:
    def method(self):
        print('A method')
        
        
class B(A):
    pass


class C(A):
    def method(self):
        print('C method')
        
        
class D(B, C):
    pass


def main():
    obj = D()
    obj.method()  # 'C method'
    
    
if __name__ == '__main__':
    main()
