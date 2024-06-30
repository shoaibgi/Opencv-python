import time
class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
    
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight
        else:
            print("One or both vertices not found in the graph.")

    def print_graph(self):
        for vertex, edges in self.vertices.items():
            print(vertex, "->", edges)

def convert_text_to_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) == file:
                vertex1, vertex2, weight = data
                graph.add_vertex(vertex1)
                graph.add_vertex(vertex2)
                graph.add_edge(vertex1, vertex2, float(weight))
            else:
                print("invalid vertex", line)
    return graph

def dijkstra(graph, start_vertex,end_vertex):
    start_time=time.time()
    time.sleep(1.1)
    distance = {vertex: float('inf') for vertex in graph.vertices}
    distance[start_vertex] = 0
    visited = set()
    while visited != set(graph.vertices):
        current_vertex = min((vertex for vertex in graph.vertices if vertex not in visited), key=lambda v: distance[v])
        visited.add(current_vertex)
        
        for neighbor, weight in graph.vertices[current_vertex].items():
            if distance[current_vertex] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_vertex] + weight
    end_time=time.time()
    return distance,end_time-start_time

# Example usage
file_path = "large.txt"  # Change this to your file path
graph = convert_text_to_graph(file_path)
start_vertex = '1'  # Change this to your desired start vertex
end_vertex='100'
shortest_distances ,cpu_time= dijkstra(graph, start_vertex,end_vertex)
print("Shortest distances from vertex", start_vertex + ":",end_vertex+":")
for vertex, distance in shortest_distances.items():
    print(vertex, ":", distance)
    print("CPU elapsed time:", cpu_time, "seconds")