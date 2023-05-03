class Animal:
    """Base class for all animals."""
    def __init__(self):
        self.can_fly = False
        self.can_run = False
        
    def print_abilities(self):
        """Prints the abilities of the animal."""
        print(f"{self.__class__.__name__}:")
        print(f"Can fly: {self.can_fly}")
        print(f"Can run: {self.can_run}\n")

class Bird(Animal):
    """Class for birds, inherits from Animal."""
    def __init__(self):
        super().__init__()
        self.can_fly = True

class Horse(Animal):
    """Class for horses, inherits from Animal."""
    def __init__(self):
        super().__init__()
        self.can_run = True

class Pegasus(Horse, Bird):
    """Class for Pegasus, inherits from Horse and Bird."""
    pass

def main():
    bird = Bird()
    bird.print_abilities()
    
    horse = Horse()
    horse.print_abilities()
    
    pegasus = Pegasus()
    pegasus.print_abilities()

if __name__ == '__main__':
    main()
