# Day 8: Graph Traversal

## BFS Algorithm và Queue

### Breadth-First Search (BFS) Concept
BFS duyệt graph theo "lớp" - thăm tất cả đỉnh ở khoảng cách k trước khi thăm đỉnh ở khoảng cách k+1.

### BFS Implementation
```python
from collections import deque

def bfs(graph, start):
    """
    BFS traversal
    Time complexity: O(V + E)
    Space complexity: O(V)
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Thăm tất cả neighbors chưa được visited
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# Ví dụ sử dụng
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected
    
    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

# Test
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')

print(bfs(g, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

### BFS with Distance Tracking
```python
def bfs_with_distance(graph, start):
    """BFS với theo dõi khoảng cách"""
    visited = set()
    queue = deque([(start, 0)])  # (vertex, distance)
    visited.add(start)
    distances = {start: 0}
    
    while queue:
        vertex, dist = queue.popleft()
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    
    return distances

# Test
distances = bfs_with_distance(g, 'A')
print(distances)  # {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 3}
```

### BFS for Shortest Path (Unweighted)
```python
def bfs_shortest_path(graph, start, end):
    """
    Tìm đường đi ngắn nhất trong unweighted graph
    """
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])  # (vertex, path)
    visited.add(start)
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Không tìm thấy đường đi

# Test
path = bfs_shortest_path(g, 'A', 'F')
print(f"Shortest path from A to F: {path}")  # ['A', 'B', 'D', 'F']
```

## DFS Algorithm và Stack

### Depth-First Search (DFS) Concept
DFS đi sâu vào graph - thăm một đỉnh rồi đi sâu vào neighbors của nó trước khi quay lại.

### DFS Implementation (Recursive)
```python
def dfs_recursive(graph, start, visited=None):
    """
    DFS recursive implementation
    Time complexity: O(V + E)
    Space complexity: O(V) - recursion stack
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

# Test
print(dfs_recursive(g, 'A'))  # ['A', 'B', 'D', 'F', 'C', 'E']
```

### DFS Implementation (Iterative with Stack)
```python
def dfs_iterative(graph, start):
    """
    DFS iterative implementation using stack
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Thêm neighbors vào stack (reverse order để giữ thứ tự)
            neighbors = graph.get_neighbors(vertex)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

# Test
print(dfs_iterative(g, 'A'))
```

### DFS for Path Finding
```python
def dfs_find_path(graph, start, end, path=None):
    """Tìm một đường đi từ start đến end bằng DFS"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return path
    
    for neighbor in graph.get_neighbors(start):
        if neighbor not in path:  # Tránh cycle
            new_path = dfs_find_path(graph, neighbor, end, path)
            if new_path:
                return new_path
    
    return None

def dfs_find_all_paths(graph, start, end, path=None):
    """Tìm tất cả đường đi từ start đến end"""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph.get_neighbors(start):
        if neighbor not in path:
            new_paths = dfs_find_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths

# Test
print(dfs_find_path(g, 'A', 'F'))
print(dfs_find_all_paths(g, 'A', 'E'))
```

## Applications: Shortest Path, Connectivity

### 1. Connected Components (Undirected Graph)
```python
def find_connected_components(graph):
    """Tìm tất cả connected components"""
    visited = set()
    components = []
    
    for vertex in graph.graph.keys():
        if vertex not in visited:
            # BFS để tìm component
            component = []
            queue = deque([vertex])
            visited.add(vertex)
            
            while queue:
                v = queue.popleft()
                component.append(v)
                
                for neighbor in graph.get_neighbors(v):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            components.append(component)
    
    return components

# Test với disconnected graph
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('C', 'D')
g2.add_edge('E', 'F')
g2.add_edge('F', 'G')

components = find_connected_components(g2)
print(f"Connected components: {components}")
# [['A', 'B'], ['C', 'D'], ['E', 'F', 'G']]
```

### 2. Bipartite Graph Check
```python
def is_bipartite(graph):
    """
    Kiểm tra graph có phải bipartite không
    Sử dụng BFS để color vertices
    """
    color = {}
    
    for start in graph.graph.keys():
        if start not in color:
            # BFS coloring
            queue = deque([start])
            color[start] = 0
            
            while queue:
                vertex = queue.popleft()
                
                for neighbor in graph.get_neighbors(vertex):
                    if neighbor not in color:
                        color[neighbor] = 1 - color[vertex]
                        queue.append(neighbor)
                    elif color[neighbor] == color[vertex]:
                        return False  # Conflict - not bipartite
    
    return True

# Test
bipartite_graph = Graph()
bipartite_graph.add_edge('A', 'C')
bipartite_graph.add_edge('A', 'D')
bipartite_graph.add_edge('B', 'C')
bipartite_graph.add_edge('B', 'D')

print(f"Is bipartite: {is_bipartite(bipartite_graph)}")  # True
```

### 3. Cycle Detection
```python
def has_cycle_undirected(graph):
    """Phát hiện cycle trong undirected graph bằng DFS"""
    visited = set()
    
    def dfs_cycle_check(vertex, parent):
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle_check(neighbor, vertex):
                    return True
            elif neighbor != parent:
                return True  # Back edge found - cycle exists
        
        return False
    
    for vertex in graph.graph.keys():
        if vertex not in visited:
            if dfs_cycle_check(vertex, None):
                return True
    
    return False

def has_cycle_directed(graph):
    """Phát hiện cycle trong directed graph"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {}
    
    def dfs_cycle_check(vertex):
        color[vertex] = GRAY
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in color:
                color[neighbor] = WHITE
            
            if color[neighbor] == GRAY:
                return True  # Back edge - cycle found
            elif color[neighbor] == WHITE and dfs_cycle_check(neighbor):
                return True
        
        color[vertex] = BLACK
        return False
    
    # Initialize all vertices as WHITE
    for vertex in graph.graph.keys():
        color[vertex] = WHITE
    
    for vertex in graph.graph.keys():
        if color[vertex] == WHITE:
            if dfs_cycle_check(vertex):
                return True
    
    return False
```

### 4. Topological Sort (Directed Acyclic Graph)
```python
def topological_sort_dfs(graph):
    """
    Topological sort sử dụng DFS
    Chỉ áp dụng cho DAG (Directed Acyclic Graph)
    """
    visited = set()
    stack = []
    
    def dfs_topo(vertex):
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_topo(neighbor)
        
        stack.append(vertex)  # Thêm vào stack sau khi visit xong
    
    for vertex in graph.graph.keys():
        if vertex not in visited:
            dfs_topo(vertex)
    
    return stack[::-1]  # Reverse stack

def topological_sort_bfs(graph):
    """Topological sort sử dụng BFS (Kahn's algorithm)"""
    # Tính in-degree
    in_degree = {}
    for vertex in graph.graph.keys():
        in_degree[vertex] = 0
    
    for vertex in graph.graph.keys():
        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] += 1
    
    # Queue với vertices có in-degree = 0
    queue = deque([v for v in in_degree if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Kiểm tra cycle
    if len(result) != len(graph.graph):
        return None  # Has cycle
    
    return result
```

## Implementation in Python

### Complete Graph Class with Traversal
```python
from collections import deque, defaultdict

class CompleteGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_neighbors(self, vertex):
        return [neighbor for neighbor, _ in self.graph[vertex]]
    
    def get_weighted_neighbors(self, vertex):
        return self.graph[vertex]
    
    def bfs(self, start):
        """BFS traversal"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """DFS traversal"""
        visited = set()
        result = []
        
        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        dfs_helper(start)
        return result
    
    def shortest_path_bfs(self, start, end):
        """Shortest path in unweighted graph"""
        if start == end:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor == end:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def is_connected(self):
        """Kiểm tra graph có connected không"""
        if not self.graph:
            return True
        
        start = next(iter(self.graph))
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == len(self.graph)

# Ví dụ sử dụng
cg = CompleteGraph()
cg.add_edge('A', 'B')
cg.add_edge('A', 'C')
cg.add_edge('B', 'D')
cg.add_edge('C', 'E')

print("BFS:", cg.bfs('A'))
print("DFS:", cg.dfs('A'))
print("Shortest path A->E:", cg.shortest_path_bfs('A', 'E'))
print("Is connected:", cg.is_connected())
```

### Performance Comparison
```python
import time
import random

def performance_comparison():
    # Tạo large graph
    n = 1000
    edges = [(random.randint(0, n-1), random.randint(0, n-1)) 
             for _ in range(5000)]
    
    graph = CompleteGraph()
    for u, v in edges:
        graph.add_edge(u, v)
    
    start_vertex = 0
    
    # BFS performance
    start_time = time.time()
    bfs_result = graph.bfs(start_vertex)
    bfs_time = time.time() - start_time
    
    # DFS performance
    start_time = time.time()
    dfs_result = graph.dfs(start_vertex)
    dfs_time = time.time() - start_time
    
    print(f"BFS visited {len(bfs_result)} vertices in {bfs_time:.4f}s")
    print(f"DFS visited {len(dfs_result)} vertices in {dfs_time:.4f}s")

performance_comparison()
```

## Common Graph Problems

### 1. Number of Islands
```python
def num_islands(grid):
    """
    Đếm số đảo trong grid 2D
    '1' = land, '0' = water
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        
        while queue:
            row, col = queue.popleft()
            
            # Check 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr, nc) not in visited and grid[nr][nc] == '1'):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    
    return islands
```

### 2. Word Ladder
```python
def ladder_length(begin_word, end_word, word_list):
    """
    Tìm độ dài shortest transformation sequence
    """
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, length = queue.popleft()
        
        if word == end_word:
            return length
        
        # Try all possible one-character changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, length + 1))
    
    return 0
```

## Best Practices

1. **Choose appropriate traversal**: BFS cho shortest path, DFS cho path existence
2. **Use appropriate data structures**: deque cho BFS, recursion/stack cho DFS
3. **Track visited vertices**: Tránh infinite loops
4. **Consider space complexity**: DFS có thể gây stack overflow
5. **Handle disconnected graphs**: Iterate qua tất cả vertices
6. **Optimize for specific problems**: Bidirectional search, A* algorithm