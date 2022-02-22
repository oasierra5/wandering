class Location:
    
    def __init__(self):
        self.Location_Wandering ={}
    
    def add_Wandering(self, wandering, track):
        self.Location_Wandering[wandering] = track
        
    def move_Wandering(self, wandering):
        delta_x, delta_y = wandering.walk()
        location_now = self.Location_Wandering[wandering]
        new_Location = location_now.move(delta_x, delta_y)
        
        self.Location_Wandering[wandering] = new_Location
        
    def get_Location(self, wandering):
        return self.Location_Wandering[wandering]
    
