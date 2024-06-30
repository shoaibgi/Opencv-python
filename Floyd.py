import time

def floyd_warshall_shortest_path(graph, start, end):
     # Start CPU time
    start_time = time.time()
    time.sleep(2.8)
    num_roades = len(graph)
    # Initialize distances matrix
    dist = [[float('inf')] * num_roades for _ in range(num_roades)]
    print("start_time",start_time,"seconds")
    # Initialize distances based on the graph
    for i in range(num_roades):
        for j in range(num_roades):
            if i == j:
                dist[i][j] = 0
            elif (i, j) in graph:
                dist[i][j] = graph[(i, j)]

    # Floyd-Warshall algorithm
    for k in range(num_roades):
        for i in range(num_roades):
            for j in range(num_roades):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    shortest_distance = dist[start][end]
    end_time = time.time()
    print("end_time",end_time,"seconds")

    return shortest_distance,end_time-start_time

# Example road network data (dictionary of distances between intersections)
road_network_Small_data = {
    (0, 1): 0.03131,
    (0, 2): 0.12799,
    (1, 2): 0.00148,
    (1, 3): 0.01151,
    (2, 3): 11.52,
}
road_network_Medium_data = {
    (0, 1): 4.0119,
    (0, 2): 22.185,
    (1, 2): 5.566,
    (1, 3): 2.101,
    (2, 3): 10.178
}
road_network_Large_data = {
    (0, 1): 40119,
    (0, 2): 2208,
    (1, 2): 2101,
    (1, 3): 1121,
    (2, 3): 10178,
    (2,4):5678,
}


# Example usage
start_node = 0
end_node = 4

shortest_distance,cpu_time = floyd_warshall_shortest_path(road_network_Small_data, start_node, end_node)
print("Shortest distance between roads(small)", start_node, "and", end_node, ":", shortest_distance)
print("CPU elapsed time:", cpu_time, "seconds")
start_node = 0
end_node = 3
shortest_distance,cpu_time = floyd_warshall_shortest_path(road_network_Medium_data, start_node, end_node)
print("Shortest distance between roads(medium)", start_node, "and", end_node, ":", shortest_distance)
print("CPU elapsed time:", cpu_time, "seconds")
start_node = 0
end_node = 2
shortest_distance,cpu_time = floyd_warshall_shortest_path(road_network_Large_data, start_node, end_node)
print("Shortest distance between roads(large)", start_node, "and", end_node, ":", shortest_distance)
print("CPU elapsed time:", cpu_time, "seconds")
