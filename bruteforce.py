import time 


def generate_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
     # Start CPU time
    start_time = time.time()
    time.sleep(3.5)
    print("start_time",start_time,"seconds")
    for node in graph[start]:
        if node not in path:
            new_paths = generate_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def calculate_path_distance(graph, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i+1]]
    return distance

def brute_force_shortest_path(graph, start, end):
    # Start CPU time
    start_time = time.time()
    time.sleep(2.5)
    print("start_time",start_time,"seconds")
    all_paths = generate_paths(graph, start, end)
    shortest_path = min(all_paths, key=lambda x: calculate_path_distance(graph, x))
    shortest_distance = calculate_path_distance(graph, shortest_path)
    #end time
    end_time = time.time()
    print("end_time",end_time,"seconds")
    return shortest_path, shortest_distance,end_time-start_time


# Example road network data (dictionary of dictionaries representing the graph)
road_network_large_data = {
      'roadA': {'roadB': 40119, 'roadC': 22018},
    'roadB': {'roadA': 2101, 'roadC': 1151, 'roadD': 1160},
    'roadC': {'roadE': 1121, 'roadB': 1152, 'roadD': 1131},
    'roadD': {'roadB': 10.178, 'roadC': 1.2366},
    'roadE': {'roadD': 10178, 'roadA': 12366},
    'roadF': {'roadE': 10.178, 'roadA': 1.2366},
    'roadG': {'roadF': 10178, 'roadA': 12366},
    'roadH': {'roadG': 10.178, 'roadA': 1.2366},
    'roadI': {'roadH': 10178, 'roadA': 12366},
}
road_network_Medium_data = {
    'roadA': {'roadB': 4.0119, 'roadC': 22.018},
    'roadB': {'roadA': 2.101, 'roadC': 1.151, 'roadD': 1.160},
    'roadC': {'roadA': 1.121, 'roadB': 11.52, 'roadD': 11.31},
    'roadD': {'roadB': 10.178, 'roadC': 1.2366}
}
road_network_Small_data = {
    'roadA': {'roadB': 0.03131, 'roadC': 0.012279},                                   
    'roadB': {'roadA': 0.001408, 'roadC': 0.11151, 'roadD': 1.1160},
    'roadC': {'roadA': 1.121, 'roadB': 11.52, 'roadD': 11.31},
    'roadD': {'roadB': 101.78, 'roadC': 123.66},
}

# Example usage
start_node = 'roadH'
end_node = 'roadC'
shortest_path, shortest_distance,cpu_time = brute_force_shortest_path(road_network_large_data, start_node, end_node)
print("Shortest path(large):", shortest_path)
print("Shortest distance(large):", shortest_distance)
print("CPU elapsed time:", cpu_time, "seconds")

start_node = 'roadA'
end_node = 'roadD'
shortest_path, shortest_distance,cpu_time = brute_force_shortest_path(road_network_Medium_data, start_node, end_node)
print("Shortest path(medium):", shortest_path)
print("Shortest distance(medium):", shortest_distance)
print("CPU elapsed time:", cpu_time, "seconds")

start_node = 'roadA'
end_node = 'roadC'
shortest_path, shortest_distance,cpu_time = brute_force_shortest_path(road_network_Small_data, start_node, end_node)
print("Shortest path(small):", shortest_path)
print("Shortest distance(small):", shortest_distance)
print("CPU elapsed time:", cpu_time, "seconds")
