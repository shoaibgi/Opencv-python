import time
import heapq

def dijkstra(graph, start, end):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes to visit, sorted by distance
    priority_queue = [(0, start)]

    # Track visited nodes
    visited = set()

    # Track the shortest path from each node
    shortest_path = {}

    # Start CPU time
    start_time = time.time()
    print("start_time",start_time,"seconds")
    time.sleep(1.1)
    while priority_queue:
        distance, current_node = heapq.heappop(priority_queue)

        # If the current node is the end node, break
        if current_node == end:
            break
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                total_distance = distance + weight
                if total_distance < distances[neighbor]:
                    distances[neighbor] = total_distance
                    shortest_path[neighbor] = current_node
                    heapq.heappush(priority_queue, (total_distance, neighbor))
                    # End CPU time
    end_time = time.time()
    print("end_time",end_time,"seconds")

    # Reconstruct the shortest path
    path = []
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        current_node = shortest_path[current_node]
    path.insert(0, start)
    return distances[end], path, end_time - start_time

    
# Example graph representation (adjacency list)
road_network_Large_data = {
    '0': {'12': 0.47, '23': 0.29},
    '1': {'4': 0.32, '15': 0.51},
    '2': {'17': 0.24, '28': 0.39},
    '3': {'20': 0.58, '31': 0.42},
    '4': {'1': 0.32, '25': 0.26, '34': 0.48},
    '5': {'14': 0.35, '27': 0.41},
    '6': {'36': 0.52, '45': 0.29},
    '7': {'18': 0.37, '29': 0.44},
    '8': {'21': 0.28, '38': 0.55},
    '9': {'30': 0.49, '42': 0.36},
    '10': {'22': 0.31, '33': 0.57},
    '11': {'44': 0.25, '35': 0.43},
    '12': {'0': 0.47, '24': 0.38},
    '13': {'37': 0.59, '46': 0.26},
    '14': {'5': 0.35, '26': 0.47},
    '15': {'1': 0.51, '39': 0.33},
    '16': {'28': 0.27, '48': 0.54},
    '17': {'2': 0.24, '40': 0.46},
    '18': {'7': 0.37, '41': 0.29},
    '19': {'32': 0.53, '49': 0.34},
    '20': {'3': 0.58, '23': 0.41},
    '21': {'8': 0.28, '43': 0.56},
    '22': {'10': 0.31, '34': 0.45},
    '23': {'0': 0.29, '20': 0.41},
    '24': {'12': 0.38, '46': 0.50},
    '25': {'4': 0.26, '37': 0.39},
    '26': {'14': 0.47, '48': 0.32}, 
    '27': {'5': 0.41, '39': 0.25},
    '28': {'2': 0.39, '16': 0.27},
    '29': {'7': 0.44, '41': 0.51},
    '30': {'9': 0.49, '42': 0.28},
    '31': {'3': 0.42, '43': 0.37},
    '32': {'19': 0.53, '45': 0.46},
    '33': {'10': 0.57, '46': 0.34},
    '34': {'4': 0.48, '22': 0.45}, 
    '35': {'11': 0.43, '47': 0.29},
    '36': {'6': 0.52, '48': 0.40},
    '37': {'13': 0.59, '25': 0.39},
    '38': {'8': 0.55, '49': 0.42},
    '39': {'15': 0.33, '27': 0.25},
    '40': {'17': 0.46, '50': 0.31},
    '41': {'18': 0.29, '29': 0.51}, 
    '42': {'9': 0.36, '30': 0.28},
    '43': {'21': 0.56, '31': 0.37},
    '44': {'11': 0.25, '50': 0.48},
    '45': {'6': 0.29, '32': 0.46},
    '46': {'13': 0.26, '24': 0.50, '33': 0.34},
    '47': {'35': 0.29, '49': 0.53},
    '48': {'16': 0.54, '26': 0.32, '36': 0.40},
    '49': {'19': 0.34, '38': 0.42, '47': 0.53},
    '50': {'40': 0.31, '44': 0.48} 
}

road_network_Medium_data = {
    'roadA': {'roadB': 4.0119, 'roadC': 22.018},
    'roadB': {'roadA': 2.101, 'roadC': 1.151, 'roadD': 1.160},
    'roadC': {'roadA': 1.121, 'roadB': 11.52, 'roadD': 11.31},
    'roadD': {'roadB': 10.178, 'roadC': 1.2366},
    'roadE': {'roadD': 10178, 'roadA': 12366}

}
road_network_Small_data = {
    'roadA': {'roadB': 0.03131, 'roadC': 0.012279},                                   
    'roadB': {'roadA': 0.001408, 'roadC': 0.11151, 'roadD': 1.1160},
    'roadC': {'roadA': 1.121, 'roadB': 11.52, 'roadD': 11.31},
    'roadD': {'roadB': 101.78, 'roadC': 123.66},
}

# Example usage
start_node = '0'
print("start_point",start_node)
end_node = '50'
print("end_point",end_node)
shortest_distance, shortest_path, cpu_time = dijkstra(road_network_Large_data, start_node, end_node)
print("Shortest distance(large):", shortest_distance)
print("Shortest path(large):", ' -> '.join(shortest_path))
print("CPU elapsed time:", cpu_time, "seconds")


start_node = 'roadA'
time.sleep(0.1)
print("start_point",start_node)
end_node = 'roadD'
print("end_point",end_node)
shortest_distance, shortest_path, cpu_time = dijkstra(road_network_Medium_data, start_node, end_node)
print("Shortest distance(medium):", shortest_distance)
print("Shortest path(medium):", ' -> '.join(shortest_path))
print("CPU elapsed time:", cpu_time, "seconds")

start_node = 'roadA'
time.sleep(0.3)
print("start_point",start_node)
end_node = 'roadC'
print("end_point",end_node)
shortest_distance, shortest_path, cpu_time = dijkstra(road_network_Small_data, start_node, end_node)
print("Shortest distance(small):", shortest_distance)
print("Shortest path(small):", ' -> '.join(shortest_path))
print("CPU elapsed time:", cpu_time, "seconds")


