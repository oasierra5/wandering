from Wandering import ComunWandering, Wandering
from Track import Track
from Location import Location 

from bokeh.plotting import figure, output_file, show

def Walking(Location, Wandering, Steps):
    beginning = Location.get_Location(Wandering)
    
    for _ in range(Steps):
        Location.move_Wandering(Wandering)
    return beginning.Distance(Location.get_Location(Wandering))
        
def simulate_Walk(Steps, number_attemps, type_Wandering):
    Wandering = type_Wandering(name='Alirio')
    origen = Location(0, 0)
    Distances = []
    
    for _ in range(number_attemps):
        Track = Track
        Track.add_Wandering(Wandering, origen)
        simulations_Walk = Walking(Track, Wandering, Steps)
        Distances.append(round(simulations_Walk, 1))
    return Distances

def graph(x,y):
    graphics = figure(title='Camino del errante', x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x, y, legend='Distancia')
    show(graphics)
    
def main(distances_Walk, number_attemps, type_Wandering):
    average_walking_distance = []
    
    for Steps in distances_Walk:
        distances = simulate_Walk(Steps, number_attemps, type_Wandering)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)
        average_walking_distance.append(middle_distance)
        print(f'{type_Wandering.__name__} Caminata aleatoria de {Steps} pasos')
        print(f'Media = {middle_distance}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')  
    graph(distances_Walk, average_walking_distance)
    
    if __name__ == '__main__':
        distances_Walk = [10, 100, 1000, 10000]
        number_attemps = 100
        main(distances_Walk, number_attemps, ComunWandering)