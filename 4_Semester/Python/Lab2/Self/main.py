class Houses:
    def __init__(self):
        pass
    def print_attr(self):
        print(f"{self.__class__.__name__}:")
        print(vars(self))
    
class with_land(Houses):
    def __init__(self):
        super().__init__()
        self.land=True
    def print_land(self):
        print("with land")
class without_land(Houses):
    def __init__(self):
        super().__init__()
        self.land=False
    def print_land(self):
        print("without land")
class For_many_families(Houses):
    def __init__(self):
        super().__init__()
        self.many_families=True
    def print_families(self):
        print("for many families")    
class For_one_family(Houses):
    def __init__(self):
        super().__init__()
        self.many_families=False        
    def print_families(self):
        print("for one family")

class Villa(with_land,For_one_family):
    def __init__(self):
        super().__init__()
        self.pool=True
    def print_info(self):
        print(f"{self.__class__.__name__}:")
        super().print_land()
        super().print_families()    
        print("With Pool")
class Apartments(without_land,For_one_family):
    
    def print_info(self):
        print(f"{self.__class__.__name__}:")
        super().print_land()
        super().print_families()
        
class Townhouse(without_land,For_one_family):
    def __init__(self):
        super().__init__()
        self.floors=2
    def print_info(self):
        print(f"{self.__class__.__name__}:")
        super().print_land()
        print("With 2 floors")
        super().print_families()
class Villets(Villa,Townhouse):
    def print_info(self):
        print(f"{self.__class__.__name__}:")
        super().print_info()

apart=Apartments()
apart.print_attr() 

villets=Villets()
villets.print_attr()

