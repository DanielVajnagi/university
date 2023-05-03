class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def print_table_dimensions(self):
        print(f"Table dimensions: length={self.length}, width={self.width}, height={self.height}")


class Kitchen(Table):
    def set_number_of_places(self, n):
        if n < 2:
            print("Error: It is not a kitchen table")
        else:
            self.places = n
            
    def print_number_of_places(self):
        print(f"Number of places: {self.places}")
        

t_room1 = Kitchen(2, 1, 0.5)
t_room1.print_table_dimensions()
t_room1.set_number_of_places(5)
t_room1.print_number_of_places()

t_2 = Table(1, 3, 0.7)
t_2.print_table_dimensions()
