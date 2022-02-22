from Wandering import ComunWandering
from Track import Track
from Location import Location 

from bokeh.plotting import figure, output_file, show

def Walking(Location, Wandering, steps):
    beginning = Location.get_Location(Wandering)
    
    for _ in range(steps):
        Location.move_wandering(Wandering)
    return beginning.Distance(Location.get_Location(Wandering))
        