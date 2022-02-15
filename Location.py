class Location:
    
    def __init__(self):
        self.Location_Wandering ={}
    
    def add_Wandering(self, Wandering, Location):
        self.Location_Wandering[Wandering] = Location
        
    def move_Wandering(self, Wandering):
        delta_x, delta_y = Wandering.walk()
        Location_now = self.Location_Wandering[Wandering]
        new_Location = Location_now.move(delta_x, delta_y)
        
        self.Location_Wandering[Wandering] = new_Location
        
    def get_Location(self, Wandering):
        return self.Location_Wandering[Wandering]
    