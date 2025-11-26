# Day 13: Shortest Path Algorithms

## Dijkstra's Algorithm

### Khái niệm
Dijkstra's algorithm tìm đường đi ngắn nhất từ một đỉnh nguồn đến tất cả các đỉnh khác trong weighted graph với trọng số không âm.

### Basic Implementation
```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Dijkstra's algorithm
    Time: O((V + E) log V), Space: O(V)
    graph: adjacency list {u: [(v, weight), ...]}
    """
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        # Skip if already processed
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Update neighbors
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return distances

# Test Dijkstra
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

distances = dijkstra(graph, 'A')
print("Shortest distances from A:", distances)
```

### Dijkstra with Path Reconstruction
```python
def dijkstra_with_path(graph, start, end=None):
    """
    Dijkstra với reconstruct path
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous = {vertex: None for vertex in graph}
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        # Early termination if we found target
        if end and current_vertex == end:
            break
        
        for neighbor, weight in graph[current_vertex]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (new_dist, neighbor))
    
    def reconstruct_path(target):
        """Reconstruct path from start to target"""
        if distances[target] == float('inf'):
            return None
        
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = previous[current]
        
        return path[::-1]
    
    if end:
        return distances[end], reconstruct_path(end)
    else:
        return distances, previous

# Test with path reconstruction
distance, path = dijkstra_with_path(graph, 'A', 'E')
print(f"Shortest distance A->E: {distance}")
print(f"Path: {' -> '.join(path)}")
```

### Dijkstra for Grid
```python
def dijkstra_grid(grid, start, end):
    """
    Dijkstra cho grid 2D
    grid[i][j] = cost để đi qua cell (i, j)
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Distance matrix
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = grid[start[0]][start[1]]
    
    # Priority queue: (distance, row, col)
    pq = [(grid[start[0]][start[1]], start[0], start[1])]
    visited = set()
    
    while pq:
        current_dist, row, col = heapq.heappop(pq)
        
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        
        if (row, col) == end:
            return current_dist
        
        # Check all 4 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                (new_row, new_col) not in visited):
                
                new_dist = current_dist + grid[new_row][new_col]
                
                if new_dist < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_dist
                    heapq.heappush(pq, (new_dist, new_row, new_col))
    
    return float('inf')  # No path found

# Test grid Dijkstra
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
min_cost = dijkstra_grid(grid, (0, 0), (2, 2))
print(f"Minimum cost path: {min_cost}")
```

## Floyd-Warshall Algorithm

### Basic Implementation
```python
def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm - All pairs shortest path
    Time: O(V³), Space: O(V²)
    graph: adjacency matrix
    """
    n = len(graph)
    
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Copy graph to distance matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Floyd-Warshall main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def floyd_warshall_with_path(graph):
    """
    Floyd-Warshall với path reconstruction
    """
    n = len(graph)
    
    # Distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    next_vertex = [[None] * n for _ in range(n)]
    
    # Initialize
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                next_vertex[i][j] = j
    
    # Main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]
    
    def reconstruct_path(start, end):
        """Reconstruct path from start to end"""
        if next_vertex[start][end] is None:
            return None
        
        path = [start]
        current = start
        
        while current != end:
            current = next_vertex[current][end]
            path.append(current)
        
        return path
    
    return dist, reconstruct_path

# Test Floyd-Warshall
# Graph as adjacency matrix
graph_matrix = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

distances, get_path = floyd_warshall_with_path(graph_matrix)
print("All pairs shortest distances:")
for i in range(len(distances)):
    print(distances[i])

print(f"Path from 0 to 3: {get_path(0, 3)}")
```

### Detecting Negative Cycles
```python
def floyd_warshall_negative_cycle(graph):
    """
    Floyd-Warshall với phát hiện negative cycle
    """
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
    
    # Main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Check for negative cycles
    has_negative_cycle = False
    for i in range(n):
        if dist[i][i] < 0:
            has_negative_cycle = True
            break
    
    return dist, has_negative_cycle

def find_negative_cycle_vertices(graph):
    """
    Tìm các đỉnh bị ảnh hưởng bởi negative cycle
    """
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Initialize
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Mark vertices affected by negative cycles
    affected = [[False] * n for _ in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = float('-inf')
                    affected[i][j] = True
    
    return dist, affected
```

## Single Source vs All Pairs

### When to Use Each Algorithm

```python
def choose_shortest_path_algorithm(num_vertices, num_edges, has_negative_weights, need_all_pairs):
    """
    Hướng dẫn chọn thuật toán shortest path
    """
    
    if need_all_pairs:
        if num_vertices <= 400:  # Floyd-Warshall feasible
            return "Floyd-Warshall O(V³)"
        else:
            return "Run Dijkstra from each vertex O(V²log V + VE)"
    
    else:  # Single source
        if has_negative_weights:
            return "Bellman-Ford O(VE)"
        else:
            if num_edges <= num_vertices * num_vertices // 4:
                return "Dijkstra with binary heap O((V+E)log V)"
            else:
                return "Dijkstra with Fibonacci heap O(E + V log V)"

# Comparison table
algorithms_comparison = {
    "Dijkstra": {
        "Time": "O((V+E) log V)",
        "Space": "O(V)",
        "Negative weights": "No",
        "Single source": "Yes",
        "All pairs": "Run V times"
    },
    "Bellman-Ford": {
        "Time": "O(VE)",
        "Space": "O(V)",
        "Negative weights": "Yes",
        "Single source": "Yes",
        "All pairs": "Run V times"
    },
    "Floyd-Warshall": {
        "Time": "O(V³)",
        "Space": "O(V²)",
        "Negative weights": "Yes (detects cycles)",
        "Single source": "Overkill",
        "All pairs": "Yes"
    }
}
```

### Bellman-Ford Algorithm
```python
def bellman_ford(graph, start):
    """
    Bellman-Ford algorithm - handles negative weights
    Time: O(VE), Space: O(V)
    """
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Get all vertices
    vertices = list(graph.keys())
    
    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for vertex in vertices:
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
    
    # Check for negative cycles
    for vertex in vertices:
        for neighbor, weight in graph[vertex]:
            if distances[vertex] + weight < distances[neighbor]:
                return None, "Negative cycle detected"
    
    return distances, None

# Test Bellman-Ford with negative weights
graph_negative = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', -3), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}

distances, error = bellman_ford(graph_negative, 'A')
if error:
    print(error)
else:
    print("Distances with negative weights:", distances)
```

## Implementation với Priority Queue

### Optimized Dijkstra
```python
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
    
    def dijkstra_optimized(self, start):
        """
        Optimized Dijkstra với early termination và better data structures
        """
        distances = defaultdict(lambda: float('inf'))
        distances[start] = 0
        
        # Priority queue: (distance, vertex)
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            
            # Skip if we've seen this vertex with better distance
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            # Process neighbors
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
        
        return dict(distances)
    
    def dijkstra_single_target(self, start, target):
        """
        Dijkstra với early termination khi tìm thấy target
        """
        distances = {start: 0}
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            
            if current_vertex == target:
                return current_dist
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    
                    if neighbor not in distances or new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
        
        return float('inf')  # Target not reachable

# Test optimized Dijkstra
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)

distances = g.dijkstra_optimized('A')
print("Optimized Dijkstra distances:", distances)

single_distance = g.dijkstra_single_target('A', 'E')
print(f"Distance A->E: {single_distance}")
```

### A* Algorithm (Heuristic Search)
```python
def a_star(graph, start, goal, heuristic):
    """
    A* algorithm - Dijkstra với heuristic
    Time: O(b^d) where b=branching factor, d=depth
    """
    # Priority queue: (f_score, vertex)
    # f_score = g_score + h_score
    open_set = [(heuristic(start, goal), start)]
    
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    came_from = {}
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]
        
        for neighbor, weight in graph[current]:
            tentative_g = g_score[current] + weight
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None, float('inf')  # No path found

# Example heuristic for grid (Manhattan distance)
def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# A* for grid pathfinding
def a_star_grid(grid, start, goal):
    """
    A* cho grid với Manhattan distance heuristic
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def heuristic(pos):
        return manhattan_distance(pos, goal)
    
    open_set = [(heuristic(start), start)]
    g_score = {start: 0}
    came_from = {}
    
    while open_set:
        current_f, current = heapq.heappop(open_set)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        row, col = current
        for dr, dc in directions:
            neighbor = (row + dr, col + dc)
            new_row, new_col = neighbor
            
            if (0 <= new_row < rows and 0 <= new_col < cols and
                grid[new_row][new_col] != 1):  # 1 = obstacle
                
                tentative_g = g_score[current] + 1  # Assuming unit cost
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, neighbor))
    
    return None  # No path found
```

## Applications and Variations

### Network Routing
```python
def network_routing_dijkstra(network, source, destination):
    """
    Network routing với Dijkstra
    network: {node: [(neighbor, latency, bandwidth), ...]}
    """
    def cost_function(latency, bandwidth):
        # Custom cost function combining latency and bandwidth
        return latency + (1000 / bandwidth)  # Prefer high bandwidth
    
    distances = {node: float('inf') for node in network}
    distances[source] = 0
    
    pq = [(0, source)]
    previous = {}
    
    while pq:
        current_cost, current_node = heapq.heappop(pq)
        
        if current_node == destination:
            break
        
        for neighbor, latency, bandwidth in network[current_node]:
            new_cost = current_cost + cost_function(latency, bandwidth)
            
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_cost, neighbor))
    
    # Reconstruct path
    path = []
    current = destination
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(source)
    
    return path[::-1], distances[destination]

# Test network routing
network = {
    'A': [('B', 10, 100), ('C', 5, 50)],
    'B': [('D', 15, 200)],
    'C': [('D', 20, 150)],
    'D': []
}

path, cost = network_routing_dijkstra(network, 'A', 'D')
print(f"Best route: {' -> '.join(path)}, Cost: {cost}")
```

### Multi-criteria Shortest Path
```python
def multi_criteria_dijkstra(graph, start, criteria_weights):
    """
    Dijkstra với multiple criteria (time, cost, distance)
    graph: {u: [(v, time, cost, distance), ...]}
    criteria_weights: [w_time, w_cost, w_distance]
    """
    def combined_cost(time, cost, distance):
        return (criteria_weights[0] * time + 
                criteria_weights[1] * cost + 
                criteria_weights[2] * distance)
    
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, time, cost, distance in graph[current_vertex]:
            if neighbor not in visited:
                edge_cost = combined_cost(time, cost, distance)
                new_dist = current_dist + edge_cost
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return dict(distances)
```

## Performance Optimization

### Bidirectional Dijkstra
```python
def bidirectional_dijkstra(graph, start, end):
    """
    Bidirectional Dijkstra - search from both ends
    Faster for single pair shortest path
    """
    # Forward search from start
    forward_dist = {start: 0}
    forward_pq = [(0, start)]
    forward_visited = set()
    
    # Backward search from end (need reverse graph)
    reverse_graph = defaultdict(list)
    for u in graph:
        for v, weight in graph[u]:
            reverse_graph[v].append((u, weight))
    
    backward_dist = {end: 0}
    backward_pq = [(0, end)]
    backward_visited = set()
    
    best_distance = float('inf')
    meeting_point = None
    
    while forward_pq or backward_pq:
        # Forward step
        if forward_pq:
            f_dist, f_vertex = heapq.heappop(forward_pq)
            
            if f_vertex not in forward_visited:
                forward_visited.add(f_vertex)
                
                if f_vertex in backward_visited:
                    total_dist = forward_dist[f_vertex] + backward_dist[f_vertex]
                    if total_dist < best_distance:
                        best_distance = total_dist
                        meeting_point = f_vertex
                
                for neighbor, weight in graph[f_vertex]:
                    if neighbor not in forward_visited:
                        new_dist = f_dist + weight
                        if neighbor not in forward_dist or new_dist < forward_dist[neighbor]:
                            forward_dist[neighbor] = new_dist
                            heapq.heappush(forward_pq, (new_dist, neighbor))
        
        # Backward step
        if backward_pq:
            b_dist, b_vertex = heapq.heappop(backward_pq)
            
            if b_vertex not in backward_visited:
                backward_visited.add(b_vertex)
                
                if b_vertex in forward_visited:
                    total_dist = forward_dist[b_vertex] + backward_dist[b_vertex]
                    if total_dist < best_distance:
                        best_distance = total_dist
                        meeting_point = b_vertex
                
                for neighbor, weight in reverse_graph[b_vertex]:
                    if neighbor not in backward_visited:
                        new_dist = b_dist + weight
                        if neighbor not in backward_dist or new_dist < backward_dist[neighbor]:
                            backward_dist[neighbor] = new_dist
                            heapq.heappush(backward_pq, (new_dist, neighbor))
        
        # Early termination condition
        if (forward_pq and backward_pq and
            min(forward_pq[0][0], backward_pq[0][0]) >= best_distance):
            break
    
    return best_distance if meeting_point else float('inf')
```

## Best Practices

1. **Choose Right Algorithm**: Dijkstra cho non-negative, Bellman-Ford cho negative weights
2. **Use Appropriate Data Structures**: Priority queue cho Dijkstra
3. **Early Termination**: Stop khi tìm thấy target (single pair)
4. **Preprocessing**: Precompute cho multiple queries
5. **Memory Optimization**: Chỉ lưu cần thiết
6. **Handle Edge Cases**: Disconnected graph, self-loops
7. **Bidirectional Search**: Cho single pair queries lớn