class Bird:
    def fly(self):
        print('I am flying.')
  
  
class Horse:
    def run(self):
        print('I am running.')
  

class Pegasus(Horse, Bird):
    pass


def main():
    bird = Bird()
    horse = Horse()
    pegasus = Pegasus()
    
    bird.fly()
    # bird.run() # Raises an error
    print()
    # horse.fly() # Raises an error
    horse.run()
    print()
    pegasus.fly()
    pegasus.run()
    
    
if __name__ == '__main__':
    main()