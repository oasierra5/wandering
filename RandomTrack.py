from Wandering import ComunWandering, Wandering, RightWandering, LeftWandering
from Track import Track
from Location import Location 

from bokeh.plotting import figure, output_file, show

def know_type_Wandering(type_Wandering):
    if type_Wandering.__name__ == "ComunWandering":
        return "Errante Común"
    elif type_Wandering.__name__ == "RightWandering":
        return "Errante Derechista"
    else:
        return "Errante Izquierdista"

def Walking(wandering, steps, type_Wandering):
    beginning = [wandering.posicion()]
    
    x_graph = [0]
    y_graph = [0]
    
    for _ in range(steps-1):
        wandering.walk()
        x, y = wandering.posicion()
        x_graph.append(x)
        y_graph.append(y)

    know_type = know_type_Wandering(type_Wandering)
    graph_steps(x_graph, y_graph, know_type, steps)
    return wandering.distance_origin()
      
def simulate_Walk(Steps, number_attemps, type_Wandering):
    wandering = []
    distances = []
    
    for i in range(number_attemps):
        wandering.append(type_Wandering(name=f'Alirio {i}'))
        simulations_Walk = Walking(wandering[i], Steps, type_Wandering)
        distances.append(round(simulations_Walk, 1))
    return distances

def graph_steps(x_graph, y_graph, type_Wandering, steps):
    graphics = figure(title=type_Wandering, x_axis_label='Pasos', y_axis_label='Distancia')
    graphics.line(x_graph, y_graph, legend_label=str(steps)+' pasos')
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    graphics.diamond_cross(0, 0, fill_color ="green", line_color ="green", size = 18)
    graphics.diamond_cross(final_x, final_y, fill_color ="red", line_color ="green", size = 18)
    straight_final_x = [0, final_x]
    straight_final_y = [0, final_y]
    graphics.line(straight_final_x, straight_final_y, line_width = 2, color="red")
    show(graphics)
    
def main(distances_Walk, number_attemps, type_Wandering):
  
    for Steps in distances_Walk:
        distances = simulate_Walk(Steps, number_attemps, type_Wandering)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)

        print(f'{type_Wandering.__name__} Caminata aleatoria de {Steps} pasos')
        print(f'Media = {middle_distance}')
        print(f'Max = {max_distances}')
        print(f'Min = {min_distances}')  
    
if __name__ == '__main__':
    distances_Walk = [100000]
    number_attemps = 1
    main(distances_Walk, number_attemps, ComunWandering)
