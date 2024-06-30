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
start_node = 'roadH'
print("start_point",start_node)
end_node = 'roadC'
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

